import pandas as pd
import requests

#import
def import_data(directory):
    data_songs=pd.read_csv(directory).set_index('id', drop=True)
    return data_songs

#Function to obtain the features of a song.
def song_features(track,BASE_URL,access_token):
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    track_id = track
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    response_features=r.json()
    return pd.DataFrame([response_features])

#Function to get the id's songs from playlist. 
def get_id_songs(playlist,BASE_URL,access_token):    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    r = requests.get(BASE_URL + 'playlists/'+playlist+'/', headers=headers)
    response_tracks=r.json()
    lst=[]
    lst = [i['track']['id'] for i in response_tracks['tracks']['items']]
    return(lst)