import streamlit as st
from process_audio import get_audio
from transcriber import transcribe_process
from summarizer import Summarizer

st.set_page_config(
    page_title = "YT Summarizer",
    layout = "wide",
)

st.header("Welcome to YT Summarizer")
video_url = st.text_input("Enter the Youtube Link", placeholder="Enter the Youtube Link")

if st.button("Generate Summary"):
    if(video_url != None):
        file_path = get_audio(video_url)
        st.write("Processing the video")
        print(file_path)
        transcript = transcribe_process(file_path)
        st.write(
            f"""
                **Caption:** \n 
                {transcript}
            """
        )
        print(transcript)
        sum = Summarizer(0.3)
        result = sum.summ(transcript)
        st.write(result)
