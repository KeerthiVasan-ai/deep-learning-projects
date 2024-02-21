'''TODO : CREATE A TEXT INPUT FIELD
GET THE VAULE AND PASS IT TO MODEL
SEE THE RESULT '''

import streamlit as st
import recommendor
import pickle

model = pickle.load("song-recommender-system/model/song_recommender.pkl")

choice = recommendor.get_recommendot(500,model,10)

song_list = recommendor.get_songs(choice)

print(song_list)
