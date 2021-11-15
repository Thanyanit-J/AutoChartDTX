import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

st.write("""
# Demo of our project!

Convert a song to Simfile.
""")

# st.file_uploader get input in Bytes, so we need to read() it before progressing.
inputData = st.file_uploader('Upload a song', type=['wav', 'mp3']) 

simfile = open('Letters Goodbye.zip', 'r')

# Obsolete workaround to download stuf in streamlit older version
# def get_table_download_link():
#     href = f'<a href="https://drive.google.com/u/0/uc?id=17Ahl-368opQc8Xmi1nIiN4S8H0b5S0BP&export=download" download>Download Simfile</a>'
#     return href
    
if inputData != None:
#     song = inputData.read()
    
    
    st.download_button(
         label="Download Simfile",
         data=simfile,
         file_name="Letters Goodbye.zip",
       )
#     st.markdown(get_table_download_link(), unsafe_allow_html=True)

#     st.image(image)
    # loaded_model = tf.keras.models.load_model('/model/acc0.8685')

