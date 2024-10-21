"""
Simple Streamlit webserver application for serving developed classification
models.

Author: ExploreAI Academy.

Note:
---------------------------------------------------------------------
Please follow the instructions provided within the README.md file
located within this directory for guidance on how to use this script
correctly.
---------------------------------------------------------------------

Description: This file is used to launch a minimal streamlit web
application. You are expected to extend the functionality of this script
as part of your predict project.

For further help with the Streamlit framework, see:

https://docs.streamlit.io/en/latest/
"""

# Streamlit dependencies
import streamlit as st
import joblib
import os
import pandas as pd
import re
import requests
from io import BytesIO  # Import BytesIO

# Function to fetch and load a pickle file from a URL
def load_pickle_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Use BytesIO to treat the bytes response as a file-like object
        return joblib.load(BytesIO(response.content))
    else:
        st.error(f"Error loading the file from URL: {url} (Status code: {response.status_code})")
        return None

# Vectorizer URL
vectorizer_url = "https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/tfidfvect.pkl"
test_cv = load_pickle_from_url(vectorizer_url)

# Load your raw data
raw = pd.read_csv('https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/train.csv')

# Text cleaning function
def clean(text):
    # Make lower case
    text = text.lower()
    # Remove punctuation and numbers
    text = re.sub(r'[^\w]', ' ', text)  # Remove punctuation
    text = ''.join([l for l in text if l not in '0123456789'])  # Remove numbers
    return text

# The main function where we will build the actual app
def main():
    """News Classifier App with Streamlit"""

    st.title("News Classifier")
    st.subheader("Analysing news articles")

    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    if selection == "Information":
        st.info("The classifier is built to analyze news headlines, content, and descriptions.")
        st.markdown("""
            - Education
            - Technology
            - Business
            - Entertainment 
            - Sports
        """)

    if selection == "Prediction":
        st.info("Prediction with ML Models")
        st.image("https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/science-in-the-news.png", use_column_width=True)
        
        # Creating a text box for user input
        news_text = st.text_area("Enter news headline, content or description here", "Type Here")

        if st.button("Classify"):
            # Clean input text
            cleaned_text = clean(news_text)
            
            # Transforming user input with vectorizer
            vect_text = test_cv.transform([cleaned_text]).toarray()

            # Load your model from the URL
            model_url = "https://raw.githubusercontent.com/VuyiswaK/2401PTDS_Classification_Project/main/Streamlit/classification_model.pkl"
            predictor = load_pickle_from_url(model_url)
            
            if predictor is not None:
                prediction = predictor.predict(vect_text)
                st.success("Text Category: {}".format(prediction))

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()


 