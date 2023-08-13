# Hit-Songs-Using-Repeated-Chorus-web-app 😀
This Machine learning project aims to build a predictive web application model and find out the song's popularity(popular to be/ n't popular to be).<br>
<b>project owner<b>: Shah Yaseen <br>
contact: shahyaseen71@gmail.com <br>
<b>Mentor<b>: Nour Ibrahim <br>
contact: nouribrahim1290@gmail.com
# About
<b>Hit-Songs-Using-Repeated-Chorus-application</b> facilitates on users who are interested in listening/making songs to predict their popularity. 
# Main functionalities
1- song prediction for the Recently released 15 songs from Spotify API. <br>
2- song prediction through Spotify API link .<br>
3- song prediction through uploaded song file. <br> 
4- song prediction through the youtube link.
# Data collection
Our data was scrapped by us using:<br>
1- Billboard API to fetch the names of hot-100 songs for the last 5 years and the unpopular songs released in the same years for the same artists.<br>
2- Pytube library to download the songs that are fetched from the billboard.<br>
3- Pychorus library to find the best chorus found for each song downloaded previously.<br>
4- Librosa library to extract the audio features from the best chorus found for each song.<br>
# Data Exploratory Analysis
this phase was very challenging as we extract more than 500 features for each song to be ensured that we will inform enough features to the model.<br>
<br>
firstly: Made some general visualizations to discover what data looks like.<br><br>
secondly: Checking and handling the discovered outliers.<br><br>
<b>thirdly:</b> Applying PCA to reduce the raw features into the most important features, as we reduced the +500 features to only 201 features.<br><br>
fourthly: Go back into general visualizations to find the co-relations and contrasts between the reduced features.<br><br>
fifthly: Made some analysis on the reduced data like univariant analysis, Bivariant analysis, and Multivariant analysis.<br><br>
# Data Modeling
Our mentor asked us to work on 2 different models (Regularized logistic regression & Random forest).<br><br>
so we decided to use Randomized and Grid search for both models and then choose the highest-performance one.<br><br>
<b> Finally </b> we used the Random forest model as it had the highest performance. <b>(+80%)</b>.<br>
# Deployment
As mentioned above our app is web so we divided the team into front-end and Back-end tasks.<br><br>
### construct module
Made a specific module(library) for the app to make the code cleaner and more readable.
### construct pipeline
Made a model pipeline to ease the flow of the model after the construction of the app's module.
### Front-End 
the app includes only 2 web pages:<br>
Home page: which allows users to interact with the app whether by:<br>
1- input a song's link(Spotify/youtube).<br>
2- Click the recently released songs button.<br><br>
Result page: which shows song predictions.
### Back-End
The framework used is the Flask framework, as we implemented the 4 main functionalities with it.<br>














