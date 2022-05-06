
<div align="center">
    <img src="images/cover.png"  width=500 height=500/>
</div>

&nbsp;
# Spotify Recommender :headphones:

<img src="https://1000logos.net/wp-content/uploads/2017/08/Spotify-Logo.png" align="right"
     alt="Size Limit logo by Anton Lovchikov" width="150" height="110">


Welcome to this song recommender designed to work with Spotify created as the final project of the Ironhack 2020 Data Analytics course.

Based on a song provided by you or a mood, it will recommend fifty songs. These recommendations will be returned to you in the form of a playlist in your Spotify profile.  
&nbsp;

----

## The Project

The main objective of the project is to cover almost all the topics and technologies we have studied throughout the course.

&nbsp;
> **Project purpose.**



This recommender seeks to generate a playlist based on the mood of the moment, or on the sensations that a song awakens. For example, when a person arrives tired from work and feels like having a drink while listening to music, it can choose the mood 'Relax', or 'Own' and propose the song that the user wants at that very moment. 

&nbsp;
> **1. Database**

* The recommender works with a base of **6600 songs(330 hours)**. These are the main songs of each musical genre and decade.

```
It is important to keep the dataset updated with new songs. That's why in next versions I will add to the repository a notebook to update it and add as many as you want. I will call it 'get_new_songs'.
```
&nbsp;
> **2. Recommendation**

The recommendation is made using **features provided by Spotify**:
    
- **Acousticness**: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

- **Danceability**: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
    
- **Energy**: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
    
- **Instrumentalness**: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
        
- **Key**: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
        
- **Liveness**: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
        
- **Loudness**: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
        
- **Mode**: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
            
- **Speechiness**:Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
            
- **Tempo**: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
            
- **Time_signature**: An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4".

- **Valence**: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).


In this way, to make the recommendation, each song is treated as a vector, so that the recommendations are translated into the closeness that exists between the vectors. 

 To make the comparison, it is important to keep in mind that each feature has a scale, so they are scaled and of course, normalized.

 The similarity between the songs is calculated by cosine similarity, with 1 being the most similar, and -1 being the least.

 <div align="center">
    <img src="https://images4.programmerclick.com/862/31/31d7e6b3830fc1a71ecb735675197e7e.png"  width=300 height=300/>
</div>

&nbsp;
> **2. Use the program**

First, You have to create a Spotify developer account [here](https://developer.spotify.com/dashboard/), and create an app. This video can help you: https://www.youtube.com/watch?v=1vR3m0HupGI  

When you are ready, fork this repository to your **GitHub** and clone it in your local hard drive.
```
$ git clone https://github.com/<your-account>/<lab-repo>.git
```
Then you will obtain a folder named as the repository you have cloned. Now, you can start working with this.

Now, you must create a new environment in the terminal and install python.
```
conda create -n “name”
conda install ipykernel
conda install python=3.7
```
To execute the code, you must install some libraries:

```
pip install pandas
conda install requests
import numpy as np
pip install -U scikit-learn
pip install spotipy
import matplotlib.pyplot as plt
pip install streamlit
```
It is very important that the credentials generated by Spotify are added to the variables enabled in the "main.py".

```
username=‘Username’
client_id = ‘Client_id’
client_secret = ‘Client_Secret’
user_id=‘User_id’
```

Every musical taste is different, if you want to adjust your moods for the recommendations, you can do it!

Just change the ID of the playlist to a playlist of your choice. 

```
playlist_happy='37i9dQZF1DXdPec7aLTmlC'
playlist_booster='37i9dQZF1DX3rxVfibe1L0'
playlist_sad='37i9dQZF1DWZqdNJSufucb'
playlist_relax='37i9dQZF1DWVIzZt2GAU4X'
playlist_motivation='37i9dQZF1DXdxcBWuJkbcy'
playlist_energy='37i9dQZF1DWYp5sAHdz27Y'
playlist_mix='37i9dQZEVXcOx8nqzmzXjg'
playlist_dancing='37i9dQZF1DWSX4baQVDQut'
````

To run the code, you must go to the terminal, go to the repository directory and write:
```
streamlit run main.py
```

---

### :file_folder: **Folder structure**
```
└── project
    ├── .git
    │ 
    ├── .gitignore
    │ 
    ├── README.md
    │ 
    ├──p_acquisition
    ├──p_wrangling
    ├──p_analysis
    ├──p_reporting
    ├──p_connect
    ├──p_plot
    │ 
    ├── main.py
    │ 
    ├── Clean_Songs.ipynb
    │ 
    ├── Get_Songs.ipynb
    │ 
    ├── datasets
    │    ├── data_songs_clean.csv
    │    └── data_songs.csv
    │
    └──images
         ├── cover
         ├── Purple and Red Orange Cover
         └── image
        

```
&nbsp;

---
