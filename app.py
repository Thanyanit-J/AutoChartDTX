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

if inputData != None:
    songbyte = inputData.getvalue()
    song = songbyte.read()
    simfile = open('Letters Goodbye.zip', 'r')
    
    btn = st.download_button(
             label="Download Simfile",
             data=Simfile,
             file_name="Letters Goodbye.zip",
           )


    st.image(image)
    # loaded_model = tf.keras.models.load_model('/model/acc0.8685')

