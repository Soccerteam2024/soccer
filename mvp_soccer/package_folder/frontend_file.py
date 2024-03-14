# response = requests.get(f"https://soccer4-tefknaii7q-ew.a.run.app/predict?feature1={1}&feature2={1}&feature3={1}&feature={1}").json()
# st.write("The prediction is", str(response['prediction']))

# Newly generated code:
import streamlit as st
import pandas as pd
import numpy as np
import requests
# from data import get_data
path = "package_folder/data_folder/results.csv"


# Fetching the countries data
countries_data = get_data()
home_teams = countries_data['home_team'].unique()
away_teams = countries_data['away_team'].unique()
# home_teams = "Germany"
# away_teams = "Brazil"

# Streamlit interface
# Title
st.title("Match Predictor")

# User selects the 1st and 2nd country
first_country_option = st.selectbox('Select 1st country', options=home_teams)
second_country_option = st.selectbox('Select 2nd country', options=away_teams)

# User inputs for game type
friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))

# Submit button for user selections
if st.button('Submit'):
    # Convert user input to format expected by the predict function
    friendly_game_bool = 1 if friendly_game == 'Yes' else 0
    neutral_game_bool = 1 if neutral_game == 'Yes' else 0


    api_url = 'https://soccer4-tefknaii7q-ew.a.run.app/predict'

    params = {
        'feature1': first_country_option,
        'feature2': second_country_option,
        'feature3': friendly_game_bool,
        'feature4': neutral_game_bool

    }

    response = requests.get(api_url, params=params)


    if response.status_code == 200:
        prediction_result = response.json()  # Convert response to JSON
        st.success(f"Prediction: {prediction_result['prediction']}")
    else:
        st.error("Unable to generate prediction. Please try again.")
else:
    st.write('Please make your selections and click submit to see the prediction.')
