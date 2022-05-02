import pandas as pd
import warnings


#Random
import random
def selectRandom(names):
  return random.choice(names)


def clean_df_features(df_features):
    df_features.drop(['type','uri','track_href','analysis_url','duration_ms'], axis = 'columns', inplace=True)
    df_features.set_index('id', inplace = True)
    df_features_clean=df_features.astype('float64')
    return df_features_clean

def drop_duplicates(df_features_clean,data_songs):
    for song in df_features_clean.index:
        if song in data_songs.index:
            data_songs=data_songs.drop(index=song)
    return data_songs

def concatenate(data_songs, df_features):
    frames = [data_songs, df_features]
    df_mix = pd.concat(frames, sort=False)
    return df_mix

def delete_nulls(df_mix):
    df_mix.dropna(inplace=True)
    return df_mix