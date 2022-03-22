import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import librosa
import librosa.display

st.write("""
# Demo of our project!

Convert a song to Simfile.
""")

# st.file_uploader get input in Bytes, so we need to read() it before progressing.
uploadedSong = st.file_uploader('Upload a song', type=['wav', 'mp3']) 

# simfile = open('Letters Goodbye.zip', 'rb')

# Obsolete workaround to download stuf in streamlit older version
# def get_table_download_link():
#     href = f'<a href="https://drive.google.com/u/0/uc?id=17Ahl-368opQc8Xmi1nIiN4S8H0b5S0BP&export=download" download>Download Simfile</a>'
#     return href
    
if uploadedSong != None:
#     song = inputData.read()
    song, _ = librosa.load(uploadedSong, sr=44100)
    
    st.write(len(song))
    # st.download_button(
    #      label="Download Simfile",
    #      data=simfile,
    #      file_name="Letters Goodbye.zip",
    #    )

