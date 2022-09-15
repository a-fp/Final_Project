import pandas as pd
from p_acquisition import m_acquisition as mac
from p_analysis import m_analisys as man
from p_reporting import m_reporting as mre
from p_wrangling import m_wrangling as mwr
from p_plot import m_plot as mpl
from p_connect import m_connect as mco
import streamlit as st

import warnings

#Conexion Spotify
username='Username'
client_id = 'Client_id'
client_secret = 'Client_Secret'
user_id='User_id'
AUTH_URL = 'https://accounts.spotify.com/api/token'
redirect_uri="http://localhost:8080"
scope="playlist-modify-public playlist-modify-private ugc-image-upload"
BASE_URL = 'https://api.spotify.com/v1/'
access_token = mco.connect_spotify(client_id, client_secret, AUTH_URL)
sp = mco.connect_spotipy(username,scope,client_id,client_secret,redirect_uri)


playlist_happy='37i9dQZF1DXdPec7aLTmlC'
playlist_booster='37i9dQZF1DX3rxVfibe1L0'
playlist_sad='37i9dQZF1DWZqdNJSufucb'
playlist_relax='37i9dQZF1DWVIzZt2GAU4X'
playlist_motivation='37i9dQZF1DXdxcBWuJkbcy'
playlist_energy='37i9dQZF1DWYp5sAHdz27Y'
playlist_mix='37i9dQZEVXcOx8nqzmzXjg'
playlist_dancing='37i9dQZF1DWSX4baQVDQut'
playlist_summer='1hZVPBZijn8V7ZbiHyb1dx'


select = ['Happy', 'Booster', 'Sad', 'Relax', 'Motivation', 'Energy','Dancing', 'Drive', 'Mix','Summer','Own']
plot=['danceability','energy','key','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time_signature','mode']
directory = './datasets/data_songs_clean.csv'
summary= 'This is a playlist based on metrics such as: danceability, energy, loudness, acousticness, instrumentalness.  Enjoy it!'

st.set_page_config(
     page_title="Spotify recommender",
     page_icon="🎵",
     layout="wide",
     initial_sidebar_state="expanded",
 )

col1, col2, col3 = st.columns([2,4,1])
col1.write("")
col2.image("./Images/image/Logo.png",width=530) 
col3.write("")

col1, col2, col3 = st.columns(3)
col1.write("")
col2.title('Spotify recommender')
col3.write("")

col1, col2, col3 = st.columns(3)
col1.write("")
col2.caption('This is a project that I recommend songs based on moods or after songs.')
col3.write("")

for i in range(5):
    st.write("")
feel_1 = st.container()
for i in range(1):
    st.write("") 
feel_2 = st.container()


with feel_1:
    col1, col2, col3, col4, col5 = st.columns([2,2,3,2,2])
    col1.write("")
    col3.subheader("How do you feel today? ") 
    col3.write("")


with feel_2:
    col1, col2, col3, col4, col5= st.columns([2,2,10,2,2])
    col1.image('./Images/image/12.jpg')
    col1.image('./Images/image/8.jpg')
    col1.image('./Images/image/4.jpg')
    col2.image('./Images/image/11.jpg')
    col2.image('./Images/image/7.jpg')
    col2.image('./Images/image/3.jpg')
    feeling = col3.selectbox(" ",('Happy', 'Booster', 'Sad', 'Relax', 'Motivation', 'Energy', 'Dancing', 'Mix','Summer','Own'))
    col4.image('./Images/image/10.jpg')
    col4.image('./Images/image/6.jpg')
    col4.image('./Images/image/2.jpg')
    col5.image('./Images/image/9.jpg')
    col5.image('./Images/image/5.jpg')
    col5.image('./Images/image/1.jpg')

    if feeling == 'Own':
        track=col3.text_input('Enter track', value="", key='text_value')
        artist=col3.text_input('Enter artist', value="", key='text_value')
    col3.write("")
    playlist_name=col3.text_input("Please choose the name of your new playlist:")
    
    agree = col3.checkbox('Want to see the analysis?')


    if col3.button('Ready!'):
        run = 'yes'
    else:
        run = 'no'


    if run == 'no':
        st.write('')

    else:
        if __name__ == '__main__':
        
            data_songs = mac.import_data(directory)
            if feeling == 'Own':
                track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
                ID = pd.DataFrame([track_id['tracks']['items'][0]['id']])
                ID=ID.iloc[0][0]
            elif feeling == 'Happy':
                songs = mac.get_id_songs(playlist_happy,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Booster':
                songs = mac.get_id_songs(playlist_booster,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Sad':
                songs = mac.get_id_songs(playlist_sad,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Relax':
                songs = mac.get_id_songs(playlist_relax,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Motivation':
                songs = mac.get_id_songs(playlist_motivation,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Energy':
                songs = mac.get_id_songs(playlist_energy,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Mix':
                songs = mac.get_id_songs(playlist_mix,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Dancing':
                songs = mac.get_id_songs(playlist_dancing,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)
            elif feeling == 'Summer':
                songs = mac.get_id_songs(playlist_summer,BASE_URL,access_token)
                ID = mwr.selectRandom(songs)


            df_features= mac.song_features(ID,BASE_URL,access_token)
            df_features_clean = mwr.clean_df_features(df_features)
            data_songs = mwr.drop_duplicates(df_features_clean,data_songs)
            df_mix = mwr.concatenate(data_songs, df_features)
            df_mix_no_null=mwr.delete_nulls(df_mix)
            df_mix_scaled = man.scaler(df_mix_no_null)
            normalized_data_songs=man.normalization(df_mix_scaled)
            cos_sim = man.cosine_similarity(normalized_data_songs)
            cos_sim_df = man.df(cos_sim)
            songs_ponderate = man.concat(df_mix,cos_sim_df)
            similar_song = man.prepare_dataframe(songs_ponderate)
            best_tracks=mre.select_songs(similar_song)
            tracks=mre.prepare_tracks(best_tracks)
            playlist_id=mre.create_playlist(sp,playlist_name,user_id,summary)
            mre.cover_playlist(sp,playlist_id)
            mre.add_tracks(sp,playlist_id, tracks)
            col3.write(f"Your new playlist called '{playlist_name}' is ready. Enjoy it!")
            col3.write(f"[Click here to go](https://open.spotify.com/playlist/{playlist_id})")

            if agree:

                for i in range(5):
                    st.write("")

                col1, col2, col3, col4, col5 = st.columns([2,1,1,1,2])
                col1.write("")
                col3.subheader("Analysis") 
                col3.write("")

                col1, col2, col3, col4, col5 = st.columns([2,1,5,2,2])
                
                for column in plot:
                    mpl.ploti(similar_song, column)

                col1, col2, col3= st.columns([2,1,2])
                col1.image('./Images/image/danceability.png')
                col1.image('./Images/image/energy.png')
                col1.image('./Images/image/key.png')
                col1.image('./Images/image/loudness.png')
                col1.image('./Images/image/speechiness.png')
                col1.image('./Images/image/acousticness.png')
                col3.image('./Images/image/instrumentalness.png')
                col3.image('./Images/image/liveness.png')
                col3.image('./Images/image/valence.png')
                col3.image('./Images/image/tempo.png')
                col3.image('./Images/image/time_signature.png')
                col3.image('./Images/image/mode.png')
