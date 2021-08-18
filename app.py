import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

st.write("""
# Hello world!
This is the first streamlit app

Our Senior Project shall be a masterpiece!

But first, let's test our CIFAR-10 model, shall we?
""")

# st.file_uploader get input in Bytes, so we need to read() it before progressing.
inputData = st.file_uploader('Upload an image', type="jpg") 
image = inputData.read()

# Display the image
plt.figure()
plt.imshow(image)
plt.colorbar()
plt.grid(False)
plt.show()


st.image(image)
# loaded_model = tf.keras.models.load_model('/model/acc0.8685')

