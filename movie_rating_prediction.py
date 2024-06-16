import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

# Load your trained model (ensure you have a trained model saved as 'model.pkl')
# Load the model from the file
model =load("movie_rating_prediction.joblib")

# Title of the web app
st.title('Movie Success Predictor')

# Input features
year = st.number_input('Year', min_value=1900, max_value=2100, step=1)
actor_1 = st.text_input('Actor 1')
actor_2 = st.text_input('Actor 2')
duration = st.number_input('Duration (minutes)', min_value=1, step=1)
genre = st.text_input('Genre')
votes = st.number_input('Votes', min_value=0, step=1)
director = st.text_input('Director')

# Make predictions
if st.button('Predict'):
    # Create feature array
    features = pd.DataFrame({
    'Year': [year],
    'Actor 1': [actor_1],
    'Actor 2': [actor_2],
    'Duration': [duration],
    'Genre': [genre],
    'Votes': [votes],
    'Director': [director]
})
    prediction = model.predict(features)
    
    st.write(f'Predicted Success: {prediction[0]}')
