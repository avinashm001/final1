import streamlit as st
import pandas as pd
import base64
from PIL import Image

st.title("HELLO SEXY")
st.header("media files")


st.markdown('''
This the video source of porn collection :[meganz](https://mega.nz/fm/7lFmQRha)''')



def add_bg_from_url():
    st.markdown(



         f"""
         <style>
         .stApp {{
             background-image: url("https://www.shutterstock.com/image-illustration/abstract-modern-background-design-flyers-600w-1889075287.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

