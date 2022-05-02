import requests

#Spotipy
import spotipy
import spotipy.util as util 


#Conexions
def connect_spotify(client_id, client_secret, AUTH_URL):
    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    # convert the response to JSON
    auth_response_data = auth_response.json()
    # save the access token
    access_token = auth_response_data['access_token']
    return access_token

def connect_spotipy(username,scope,client_id,client_secret,redirect_uri):
    token=util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)
    sp = spotipy.Spotify(auth=token)
    return sp

