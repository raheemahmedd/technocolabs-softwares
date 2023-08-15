# Hit-Songs-Using-Repeated-Chorus-web-app 😀
This Machine learning project aims to build a predictive web application model and find out the song's popularity(popular to be/ n't popular to be).<br>
<b>project owner<b>: Technocolabs softwares company <br>
contact: https://github.com/Technocolabs100 <br>
<b>Mentor<b>: Nour Ibrahim <br>
contact: https://github.com/Nour-Ibrahim-1290
# About
<b>Hit-Songs-Using-Repeated-Chorus-application</b> facilitates on users who are interested in listening/making songs to predict their popularity. 
# Main functionalities
1- song prediction for the Recently released 15 songs from Spotify API. <br>
2- song prediction through Spotify API link .<br>
3- song prediction through uploaded song file. <br> 
4- song prediction through the youtube link.

##### Check it now 🔥: https.com 
# Data collection
Our data was scrapped by us using:<br><br>
1- Billboard API to fetch the names of hot-100 songs for the last 5 years and the unpopular songs released in the same years for the same artists, so we got 507 popular and 1260 unpopular songs with a total of 1767 songs.<br>
the final data extracted from Billboard API looks like 1767 rows x 3 columns(artist name, song name, song label).<br><br>
2- Pytube library to download the songs that are fetched from the billboard.<br>
the pytube library had many functions which are used to download youtube videos.<br>
- some pytube functions take a youtube link as input and then will download the video directly.<br>
- some pytube functions take the song name as input and then will download the video directly. <br><br>
*Note the pytube functions used take 2 arguments(inputs) a youtube link and the output path that will be the downloaded video saved in<br><br>
<div>
3- Pychorus library to find the best chorus found for each song downloaded previously.<br><br>

the pychorus library had many functions which are used to extract the chorus part included in the whole song.<br>
- we used a function called 'find_and_output_chorus' which takes 2 arguments(inputs) a song file and  the output path that will be the best chorus found saved in.

  *Note We determined the chorus duration to be equal to 15 seconds as mentioned in papers offered with the task.
</div>
<div>
4- Librosa library to extract the audio features from the best chorus found for each song.<br><br>
the librosa library had many functions which are used to extract numerical features from an audio file(chorus audio).<br> 

 we used only 11 major features : 
 - choroma_stft
 - chroma_cqt
 - chroma_cens 
 - spectral_centroid
 - mfcc
 - rms
 - tonnetz
 - crossing_rate 
 - spectral_bandwidth
 - spectral_contrast
 - spectral_rolloff<br><br>
we used Functions to extract feature statistics from the chorus like (min,mean,median,max,std,skew,kurtosis), so after using these functions we increased the total number of features from only 11 'major features' to 518 features. <br><br>
*Note Dataset now includes 518 features from librosa + the 3 features extracted from billboard API as mentioned above, so the final shape reached 1767 rows x 521 columns. 
 
</div>

# Data Exploratory Analysis
this phase was very challenging as we extracted more than 500 features(521) for each song to be ensured that we will inform enough features to the model.<br>
<br>
firstly: Made some general visualizations to discover what data looks like.<br><br>
- scatterplot to shew the distribution of data
- countplot to shew the counting of popular and unpopular songs in the dataset
- boxplot to check the outliers
- correlation to discover the relations between features
<div>
secondly: Checking and handling the discovered outliers.<br><br>
 </div>
 thirdly: checking the missing values and there weren't <br><br>


# Data preprocessing 
this phase is so important as it has a huge effect on the modeling phase.<br>
we apply many preprocessing techniques :
- transformer
- scaler
- PCA
  <br><br>
<b>*Note</b> Applying PCA to reduce the raw features into the most important features, as we reduced the +500 features to only 200 features.<br><br>

*Note after this phase we Go back into general visualizations to find dependencies and contrasts between the reduced features, and we made some analysis on the reduced data like univariant analysis, Bivariant analysis, and Multivariant analysis.<br><br>



# Data Modeling
#### *First task as a team
###### Each member tried to construct a random forest and logistic model alone then we chose the higher performance between us.
Our mentor asked us to work on 2 different models (Regularized logistic regression & Random forest),
so we decided to use Randomized and Grid search for both models and then choose the highest-performance one.<br><br>
*Note it was obvious that the random forest model had higher performance than the logistic one, as the random forest's maximum accuracy equals 84% while the logistic's maximum accuracy equals 71%.<br><br>
*Note we cared about the f1-score metric cause our data was imbalanced data.<br><br>

<b> Finally </b> we used the Random forest model as it had the highest performance. <b>(+84% accuracy & 60% f1-score)</b>.<br><br>
<img src="https://github.com/raheemahmedd/technocolabs-softwares/assets/72644330/f3f90a87-43fa-4db7-9ddb-fb44cc7b80ee">
# Deployment
#### *Second task as a team
###### As mentioned above our app is web so we divided the team into front-end and Back-end developers.<br><br>
<img src='https://github.com/raheemahmedd/technocolabs-softwares/assets/72644330/68cc0558-0e61-4c5e-ae43-5c9cbafd7403'>


### Front-End 
the app includes a few web pages:<br>
- Home page  <br>  <br>
<img src='https://github.com/raheemahmedd/technocolabs-softwares/assets/72644330/c4a4b94c-ff07-41e7-b579-ed7ebc08f3f3'><br>
- Inputs page <br>   
<img src='https://github.com/raheemahmedd/technocolabs-softwares/assets/72644330/fee9fcff-1f2a-4eff-bd82-36c61926cab4'><br>
<div>
which allows users to interact with the app through:<br>

1- input a song's link(Spotify/youtube).<br>
2- Click the recently released songs button.<br>
3- upload a personal song file.<br><br>
Result page:<br><br>
<img src='https://github.com/raheemahmedd/technocolabs-softwares/assets/72644330/78f65bcb-226a-44c4-a3e9-0100570b46c9'><br>
<img src='https://github.com/raheemahmedd/technocolabs-softwares/assets/72644330/d732ca6d-0607-4046-9692-6127b72d7e77'><br>
which shows song predictions.<br>
 - Developers: George saied - Rawan alaa- Nourhan Elashmawy.
</div>

### Back-End
The framework used is the Flask framework, as we implemented the 4 main functionalities with it.<br>
- predict_youtube(): this function aims to predict the popularity of a song by taking a youtube link from the user and it returns the model's prediction about the entered song link.<br><br>
 Developer: Sara Maged.
- predict_spotify(): this function aims to predict the popularity of a song by taking a Spotify API link from the user and it returns the model's prediction about the entered song link.<br><br>
 Developer: Nour Mansy.  
- check_spotify(): this function aims to fetch and predict the popularity of the recent 15 songs released from Spotify API.<br><br>
 Developer: Omar Ahmed. <br>
 <diV>
 *Note this function will take a few seconds to inform the user of his prediction(as the model will work on 15 songs ) so we make some constraints that if the last user's fetching action was three days ago and Spotify API didn't release new songs so the app will return him the last prediction's result fetched previously.<br><br>
 *Note adding some constraints, in this case, aims to increase the app performance and facilitate the user experience. <br><br>

- upload_song(): this function aims to predict  the popularity of a personally uploaded song file from a user.<br><br>
  Developer: Mazin Aziz.
  </diV>
### construct module
Made a specific module(library) for the app to make the code cleaner and more readable, so we apply it to our backend functions.<br>
###### constructed by Galal Owis
### construct pipeline
Made a model pipeline to ease the workflow of the model after the construction of the app's module to make all the preprocessing applied on the trained data previously, applied again but to the sample data that comes from the user.
###### constructed by Galal Owis

# Linkage between Frontend and Backend  
 ###### Omar Hegy
 ###### Raheem Ahmed













