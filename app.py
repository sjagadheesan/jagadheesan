import streamlit as st
import joblib 

# Load the joblib model (ensure the correct path and file extension)
model_nb = joblib.load('spam-ham')

st.title('SPAM HAM CLASSIFIER')

# Input text from the user
ip = st.text_input('Enter your text:')

# Prediction and button action
if st.button('PREDICT'):
    op = model_nb.predict([ip])
    st.title(op[0])
