import numpy as np
import pandas as pd


#sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import linear_kernel



def scaler(df_mix_no_null):
    df_mix_values= df_mix_no_null.iloc[:,1:].values
    scaler = StandardScaler()
    df_mix_scaled = scaler.fit_transform(df_mix_values)
    return df_mix_scaled

def normalization(df_mix_scaled):
    data_songs_mag = np.sqrt((df_mix_scaled*df_mix_scaled).sum(axis=1))
    ndata_song=df_mix_scaled.shape[0]
    normalized_data_songs=df_mix_scaled/data_songs_mag.reshape(ndata_song,1)
    return normalized_data_songs

def cosine_similarity(normalized_data_songs):
    cos_sim = linear_kernel(normalized_data_songs,normalized_data_songs[-1:])
    return cos_sim

def df(cos_sim):
    cos_sim_df = pd.DataFrame(cos_sim)
    return cos_sim_df

def concat(df_mix,cos_sim_df):
    songs_ponderate = pd.concat([df_mix.reset_index(), cos_sim_df], axis=1)
    return songs_ponderate

def prepare_dataframe(songs_ponderate):
    songs_ponderate.rename(columns={0: 'similarity'}, inplace=True)
    similar_song = songs_ponderate.sort_values(by=['similarity'],ascending=False)
    similar_song = similar_song.drop(similar_song[similar_song['similarity']=='1'].index)
    return similar_song