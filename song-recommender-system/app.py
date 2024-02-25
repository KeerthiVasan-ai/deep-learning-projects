import streamlit as st
import recommendor
import warnings
import pickle
warnings.filterwarnings("ignore",category=Warning)

with open("./model/song_recommender.pkl", 'rb') as f:
    model = pickle.load(f)

st.title("Ambi-fy")
user_id = st.text_input("Enter the User Id", placeholder="Enter the user between 0 - 499")

if st.button("Show Recommendations"):
    if(int(user_id) < 500):
        choice = recommendor.get_recommendor(150,model,int(user_id))
        print(choice)
        st.subheader("Songs Recommended For the user are:")
        recommendations = recommendor.get_songs(choice)
        for song in recommendations:
            st.write(song)
    else:
        st.subheader("An Unexcepted error occured")
        st.write(f"Invalid User {user_id}")