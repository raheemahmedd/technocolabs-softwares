from billpy import *


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
        return render_template('home.html',next_page = '/templates/input.html')

@app.route('/start', methods=['POST'])
def input_page():
    return render_template('input.html')

@app.route('/predict_youtube', methods=['POST'])
def predict_youtube():
        try:
            try:
                YT_link = request.form['input']
                download_audio_from_youtube(YT_link)
                variable = classify_song_file_in_same_dir()
            except ValueError as ve:
                print(str(ve))
                if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve) or 'Invalid YouTube link' == str(ve):
                    variable = str(ve)
                else:
                    variable = 'something went wrong'
        except:
            variable = 'something went wrong'

        return render_template('result.html',result=variable)

@app.route('/predict_spotify', methods=['POST'])
def predict_spotify():
        try:
            try:
                spotify_link = request.form['input']

                name = get_song_name_by_spotify_link(spotify_link.split('?')[0])
                link = get_video_youtube_link_by_name(name)
                download_audio_from_youtube(link)
                variable = classify_song_file_in_same_dir()

            except ValueError as ve:
                if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve) or 'Invalid Spotify link' ==str(ve):
                    variable = str(ve)
                else:
                    variable = 'something went wrong'
        except:
            variable = 'something went wrong'


        return render_template('result.html', result=variable)


@app.route('/check_spotify_new_releases', methods=['POST'])
def check_spotify():
    if (datetime.now() - pickle.load(open('last_update_time.pkl','rb'))).days > 30: 
        try:
            results={}
            new_releases = get_latest_releases(10)
            for song_name in new_releases:
                try:
                    try:
                        song=get_video_youtube_link_by_name(song_name)
                        download_audio_from_youtube(song)
                        classify = classify_song_file_in_same_dir()
                    except ValueError as ve:
                        if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve):
                            classify = str(ve)
                        else:
                            classify = 'something went wrong'
                except:
                    classify = 'something went wrong'
            
                results[song_name] = classify
        except:
            return render_template('recents_results.html')
    

        pickle.dump(results,open('recent_results_dict.pkl','wb'))
        pickle.dump(datetime.now(),open('last_update_time.pkl','wb'))
        return render_template('recent_results.html',result=results)
    else:
        results = pickle.load(open('recent_results_dict.pkl','rb'))
        return render_template('recent_results.html',result=results)



@app.route('/upload_song', methods=['POST'])
def upload_song():
         try:
            try:
                file = request.files["audio_file"]
                if file.filename == '':
                    return render_template('result.html', result='No file selected')

                if file.filename.split('.')[-1].lower() not in ['mp3', 'wav', 'ogg','opus']:
                    return render_template('result.html', result='Invalid file format')
                file.save('song.opus')
                variable = classify_song_file_in_same_dir()
            except ValueError as ve:
                if 'Audio duration exceeds 8 minutes' == str(ve) or 'No chorus detected' == str(ve):
                    variable = str(ve)
                else:
                    variable = 'something went wrong'
         except:
             variable = 'something went wrong'

         return render_template('result.html', result=variable)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
