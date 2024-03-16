
# # # Newly generated code:
# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import requests


# # # Fetching the countries data
# # path = "data/results.csv"
# # countries_data =  pd.read_csv(path)
# # home_teams = countries_data['home_team'].unique()
# # away_teams = countries_data['away_team'].unique()

# # # Streamlit interface
# # # Title
# # st.title("Match Predictor")

# # # User selects the 1st and 2nd country
# # first_country_option = st.selectbox('Select 1st country', options=home_teams)
# # second_country_option = st.selectbox('Select 2nd country', options=away_teams)

# # # User inputs for game type
# # friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
# # neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))

# # # Submit button for user selections
# # if st.button('Submit'):
# #     # Convert user input to format expected by the predict function
# #     friendly_game_bool = 1 if friendly_game == 'Yes' else 0
# #     neutral_game_bool = 1 if neutral_game == 'Yes' else 0


# #     api_url = 'https://soccer4-tefknaii7q-ew.a.run.app/predict'

# #     params = {
# #         'feature1': first_country_option,
# #         'feature2': second_country_option,
# #         'feature3': friendly_game_bool,
# #         'feature4': neutral_game_bool

# #     }

# #     response = requests.get(api_url, params=params)


# #     if response.status_code == 200:
# #         prediction_result = response.json()  # Convert response to JSON
# #         st.success(f"Prediction: {prediction_result['prediction']}")
# #     else:
# #         st.error("Unable to generate prediction. Please try again.")
# # else:
# #     st.write('Please make your selections and click submit to see the prediction.')



import streamlit as st
import pandas as pd
import requests

# Fetching the countries data
path = "data/results.csv"
countries_data = pd.read_csv(path)
home_teams = countries_data['home_team'].unique()
away_teams = countries_data['away_team'].unique()

# Streamlit sidebar for Intro and Team Soccer sections
st.sidebar.title("Navigation")

# Intro section in sidebar with interactive components
with st.sidebar.expander("Intro"):
    st.write("Welcome to the Match Predictor! This tool helps you predict the outcome of soccer matches based on historical data.")
    # Example of an interactive component in the Intro section
    user_feedback = st.text_input("Have any feedback for us?")
    if st.button("Submit Feedback"):
        st.write("Thanks for your feedback!")

# Team Soccer section in sidebar with interactive components
with st.sidebar.expander("Team Soccer"):
    st.write("Explore team statistics, historical performance, and more to understand how each team competes.")
    # Example of an interactive component in the Team Soccer section
    team_selection = st.selectbox("Choose a team to learn more about:", home_teams)
    if st.button("Show Team Info"):
        # Placeholder for functionality to show team info
        st.write(f"Information for {team_selection}: [Team Info Placeholder]")

# Main app interface for the Prediction section on the main page
# Title
st.title("Match Predictor")

# User selects the 1st and 2nd country
first_country_option = st.selectbox('Select 1st country', options=home_teams)
second_country_option = st.selectbox('Select 2nd country', options=away_teams)

# User inputs for game type
friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))

# Submit button for user selections
if st.button('Submit Prediction'):
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
