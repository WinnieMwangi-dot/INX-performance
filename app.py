import os
import pickle
import streamlit as st

# Print the current working directory
st.write("Current working directory:", os.getcwd())

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Model Prediction App')
st.write('Your model is loaded and ready to use!')
