import numpy as np
import pandas as pd
import librosa
import scipy
from pychorus import find_and_output_chorus
import pickle
from youtube_search import YoutubeSearch
import yt_dlp
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

trained_pipeline = pickle.load(open('pipeline.pkl','rb'))
SPOTIFY_CLIENT_ID = "a173ef9f25ed4a5ba7735bdf4886dbf4"
SPOTIFY_CLIENT_SECRET = "eccbabdcba6a4b00b42a6f6fb80c01ce"


def get_video_youtube_link_by_name(video_name):
    results = YoutubeSearch(video_name, max_results=1).to_dict()

    if results:
        video_id = results[0]['id']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        return video_link

    return None


def download_audio_from_youtube(video_url, output_file='song'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',
            'preferredquality': '192',
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
             info_dict = ydl.extract_info(video_url, download=False)
             if info_dict.get('duration') and info_dict['duration'] > 480:
                raise ValueError("Audio duration exceeds 8 minutes")
             ydl.download([video_url])
        
    except yt_dlp.utils.DownloadError:
         raise ValueError("Invalid YouTube link")


def get_audio_duration(song_path='song.opus'):
    audio, sr = librosa.load(song_path)
    duration = librosa.get_duration(y=audio, sr=sr)
    return duration

def create_chorus_file(song_path='song.opus',outpath_path='song_chorus.mp3'):
    if get_audio_duration(song_path)>480:
        raise ValueError("Audio duration exceeds 8 minutes")

    chorus_duration = 15
    while chorus_duration > 5:
        chorus_start_sec = find_and_output_chorus(song_path,outpath_path, chorus_duration)
        if chorus_start_sec is not None:
            return chorus_duration

        chorus_duration -= 1

    raise ValueError("No chorus detected")

functions = {
    'mfcc': lambda audio, sr: librosa.feature.mfcc(y=audio, sr=sr),
    'chroma_stft': lambda audio, sr: librosa.feature.chroma_stft(y=audio, sr=sr),
    'chroma_cqt': lambda audio, sr: librosa.feature.chroma_cqt(y=audio, sr=sr),
    'chroma_cens': lambda audio, sr: librosa.feature.chroma_cens(y=audio, sr=sr),
    'rms': lambda audio, sr: librosa.feature.rms(y=audio),
    'spectral_centroid': lambda audio, sr: librosa.feature.spectral_centroid(y=audio, sr=sr),
    'spectral_bandwidth': lambda audio, sr: librosa.feature.spectral_bandwidth(y=audio, sr=sr),
    'spectral_contrast': lambda audio, sr: librosa.feature.spectral_contrast(y=audio, sr=sr),
    'spectral_rolloff': lambda audio, sr: librosa.feature.spectral_rolloff(y=audio, sr=sr),
    'tonnetz': lambda audio, sr: librosa.feature.tonnetz(y=audio, sr=sr),
    'zero_crossing_rate': lambda audio, sr: librosa.feature.zero_crossing_rate(y=audio)
}


def extract_soundtrack_feature_statistics(audio_feature):
    min_val = np.min(audio_feature, axis=1)
    mean_val = np.mean(audio_feature, axis=1)
    median_val = np.median(audio_feature, axis=1)
    max_val = np.max(audio_feature, axis=1)
    std_val = np.std(audio_feature, axis=1)
    skew_val = scipy.stats.skew(audio_feature, axis=1)
    kurtosis_val = scipy.stats.kurtosis(audio_feature, axis=1)
    song_track_features = np.concatenate((min_val, mean_val, median_val, max_val, std_val, skew_val, kurtosis_val), axis=0)
    return song_track_features


def create_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)


def get_song_name_by_spotify_link(spotify_link):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))

    track_id = spotify_link.split('/')[-1]

    try:
        track_info = sp.track(track_id)
        song_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        song_and_artist = f"{song_name} by {artist_name}"
        return song_and_artist
    except spotipy.exceptions.SpotifyException:
        raise ValueError("Invalid Spotify link")

def get_latest_releases(number_of_releases=5):
    sp = create_spotify_client()
    results = sp.new_releases(limit=number_of_releases)
    new_releases = results["albums"]["items"] if "albums" in results else []
    new_releases_names = []
    for release in new_releases:
            new_releases_names.append(f"{release['name']} by {', '.join([artist['name'] for artist in release['artists']])}")
    return  new_releases_names

def extract_sample_from_song_file_in_same_dir(song_file_path = 'song',output_file_name = 'song_chorus'): #make sure to have the audio file named song.opus (the rest of functions make sure to have the same extension)
        song_file_path = song_file_path
        output_file_name = output_file_name
        new_features_dict = {}

        create_chorus_file(f'{song_file_path}.opus',f'{output_file_name}.mp3')


        chorus_audio, sr = librosa.load(f'{output_file_name}.mp3', sr=None)

        for function_name,function in functions.items():

            # Extract a soundtrack features
            audio_feature = function(chorus_audio, sr)
            audio_feature_statistics = extract_soundtrack_feature_statistics(audio_feature)

            #fill new_features_dict
            for i in range(len(audio_feature_statistics)):
                column_name = function_name + '_'+str(i+1)
                if column_name in new_features_dict:
                    new_features_dict[column_name].append(audio_feature_statistics[i])
                else:
                    new_features_dict[column_name] = [audio_feature_statistics[i]]


        return pd.DataFrame(new_features_dict)

def classify_song_file_in_same_dir():
        X_sample = extract_sample_from_song_file_in_same_dir()
        return 'Popular to be' if trained_pipeline.predict(X_sample)[0] == 1 else 'Unpopular to be'
