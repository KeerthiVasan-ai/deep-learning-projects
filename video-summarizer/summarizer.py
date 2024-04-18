import re
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

def configure():
        load_dotenv()


class Summarizer:
    def __init__(self, temp):
        configure()
        genai.configure(api_key=os.getenv("gemini_api"))
        generation_config = genai.GenerationConfig(
                temperature=temp
        )

        self.model = genai.GenerativeModel(
            'gemini-1.0-pro-latest',
            generation_config=generation_config)

    def summ(self, transcript):
        prompt = f"""The following text is a auto generated caption\
                of a video. It may have misspelt words. Read them very\
                carefully and summarize it into crisp points

                {transcript}
                """
        res = self.model.generate_content(prompt)
        print(res)
        return res.text