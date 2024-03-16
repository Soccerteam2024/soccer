
import streamlit as st
import pandas as pd
import requests
import pycountry

# Function to get country code using pycountry
def get_country_code(country_name):
    try:
        return pycountry.countries.get(name=country_name).alpha_2
    except AttributeError:
        # Log or handle countries not found in pycountry
        return None

# Function to fetch flag URL from a service using country codes
def get_flag_url(country_name):
    country_code = get_country_code(country_name)
    if country_code:
        # Construct URL for flag image
        return f"https://flagcdn.com/w320/{country_code.lower()}.png"
    else:
        # Return a placeholder or a default image if the flag or code is not found
        return "https://upload.wikimedia.org/wikipedia/commons/d/d4/World_Flag_%282004%29.svg"

# Fetching the countries data
path = "data/results.csv"
countries_data = pd.read_csv(path)
home_teams = countries_data['home_team'].unique()
away_teams = countries_data['away_team'].unique()

# Streamlit interface setup
st.title("Match Predictor")

# User selects the 1st and 2nd country
first_country_option = st.selectbox('Select 1st country', options=home_teams, key='first_country')
second_country_option = st.selectbox('Select 2nd country', options=away_teams, key='second_country')

# User inputs for game type
friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))

# Display flags next to each other with 'vs' symbol if both countries are selected
if first_country_option and second_country_option:
    first_country_flag_url = get_flag_url(first_country_option)
    second_country_flag_url = get_flag_url(second_country_option)

    # Adjusting column setup for better centering of the "vs" symbol
    col1, col_vs, col2 = st.columns([5, 14, 5])
    with col1:
        st.image(first_country_flag_url, width=100, caption=first_country_option)
    with col_vs:
        st.markdown("<h3 style='text-align: center; vertical-align: middle;'>vs</h3>", unsafe_allow_html=True)
    with col2:
        st.image(second_country_flag_url, width=100, caption=second_country_option)

# Submit button for user selections
if st.button('Submit Prediction'):
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
        prediction_result = response.json()
        if prediction_result['prediction'] == 'Win':
            st.success(f"Prediction: {first_country_option} will win")
        elif prediction_result['prediction'] == 'Lose':
            st.success(f"Prediction: {first_country_option} will lose")
        elif prediction_result['prediction'] == 'Draw':
            st.success(f"Prediction: draw")
        else:
            st.error("Unable to generate prediction. Please try again.")
else:
    st.write('Please make your selections and click submit to see the prediction.')
