from fastapi import FastAPI
import pickle
from package_folder.utils import from_number_to_flower

# app = FastAPI()

# @app.get("/")
# def root():
#     return {'greeting':"hello"}

# @app.get("/predict")
# def predict(first_country_option,
#             second_country_option,
#             friendly_game,
#             neutral_game):

#     with open('models/best_model.pkl', 'rb') as file:
#         model = pickle.load(file)

#     prediction = model.predict([[first_country_option,second_country_option,friendly_game,neutral_game]])

#     pretty_prediction = from_number_to_flower(float(prediction[0]))

#     return {"prediction": pretty_prediction}





#New One

import streamlit as st
import pandas as pd
import numpy as np

# Example list of 190 countries (for demonstration, using fewer)
countries = ['Country {}'.format(i) for i in range(1, 191)]

@st.cache
def get_select_box_data():
    # Simulating a DataFrame with outcomes and accuracies
    return pd.DataFrame({
          'Outcome': np.random.choice(['Win', 'Lose', 'Draw'], 190),
          'Accuracy': np.random.uniform(50, 100, 190)
        }, index=countries)

df = get_select_box_data()

# User selects the 1st and 2nd country
first_country_option = st.selectbox('Select 1st country', countries)
second_country_option = st.selectbox('Select 2nd country', countries)

# User inputs for game type
friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))

def model_prediction(first_country, second_country, friendly, neutral):
    # Simulate model prediction
    # This function should be replaced with your actual model prediction logic
    # For demonstration, it randomly selects a row from the DataFrame
    # Adjust this to use the friendly and neutral parameters as needed
    return df.loc[first_country].to_dict()

# User submits their selections
if st.button('Submit'):
    # Perform model prediction
    result = model_prediction(first_country_option, second_country_option, friendly_game, neutral_game)

    # Display the outcome and accuracy
    st.write(f"Model's Prediction based on inputs:")
    st.write(result)  # result is now a dictionary, which should prevent the error
else:
    st.write('Please make your selections and click submit to see the prediction.')
