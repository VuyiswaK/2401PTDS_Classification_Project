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
import joblib, os

# Data dependencies
import pandas as pd
import re

path = os.getcwd()

# Vectorizer
vectorizer_path = path + "\\tfidfvect.pkl"
if os.path.exists(vectorizer_path):
    test_cv = joblib.load(vectorizer_path)
else:
    st.error("Vectorizer file not found. Please check the file path.")

# Load your raw data
raw = pd.read_csv(path + "\\train.csv")

# Text cleaning function
def clean(text):
    # Make lower case
    text = text.lower()

    # Remove punctuation and numbers
    import string
    text = re.sub(r'[^\w]', ' ', text)  # Remove punctuation
    text = ''.join([l for l in text if l not in '0123456789'])  # Remove numbers
    return text

# The main function where we will build the actual app
def main():
    """News Classifier App with Streamlit"""

    # Creates a main title and subheader on your page - these are static across all pages
    st.title("News Classifier")
    st.subheader("Analysing news articles")

    # Creating sidebar with selection box - you can create multiple pages this way
    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    # Building out the "Information" page
    if selection == "Information":
        st.info("The classifier is built to analyze news headlines, content and descriptions and classify them in the following categories:")
        
        # Displaying bullet points using Markdown
        st.markdown("""
            - Education
            - Technology
            - Business
            - Entertainment 
            - Sports
        """)
		
    # Building out the "Prediction" page
    if selection == "Prediction":
        st.info("Prediction with ML Models")
        st.image(path + "\\science-in-the-news.png", use_column_width=True)
        
        # Creating a text box for user input
        news_text = st.text_area("Enter news headline, content or description here", "Type Here")

        if st.button("Classify"):
            # Clean input text
            cleaned_text = clean(news_text)
            
            # Transforming user input with vectorizer
            vect_text = test_cv.transform([cleaned_text]).toarray()

            # Load your .pkl file with the model of your choice + make predictions
            predictor = joblib.load(path + "\\classification_model.pkl")
            prediction = predictor.predict(vect_text)

            # When model has successfully run, will print prediction
            st.success("Text Category: {}".format(prediction))

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
    main()