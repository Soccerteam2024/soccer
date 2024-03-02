import streamlit as st
import requests


param1 = st.slider('Select a number', 1, 10, 3)

param2 = st.slider('Select another number', 1, 10, 3)

url = 'https://containersoccer-7wfyzlyocq-oe.a.run.app/predict'

params = {
    'feature1': param1,  # 0 for Sunday, 1 for Monday, ...
    'feature2': param2,
    'first_country_option': param3,
    'second_country_option': param4,
    'first_country_option': param3,
    'second_country_option': param4
}
response = requests.get(url, params=params)

st.text(response.json())

# newly added code


# import streamlit as st
# import pandas as pd
# import numpy as np

# # Example list of 190 countries (for demonstration, using fewer)
# countries = ['Country {}'.format(i) for i in range(1, 191)]

# @st.cache
# def get_select_box_data():
#     # Simulating a DataFrame with outcomes and accuracies
#     return pd.DataFrame({
#           'Outcome': np.random.choice(['Win', 'Lose', 'Draw'], 190),
#           'Accuracy': np.random.uniform(50, 100, 190)
#         }, index=countries)

# df = get_select_box_data()

# # User selects the 1st and 2nd country
# first_country_option = st.selectbox('Select 1st country', countries)
# second_country_option = st.selectbox('Select 2nd country', countries)

# # User inputs for game type
# friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
# neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))

# def model_prediction(first_country, second_country, friendly, neutral):
#     # Simulate model prediction
#     # This function should be replaced with your actual model prediction logic
#     # For demonstration, it randomly selects a row from the DataFrame
#     # Adjust this to use the friendly and neutral parameters as needed
#     return df.loc[first_country].to_dict()

# # User submits their selections
# if st.button('Submit'):
#     # Perform model prediction
#     result = model_prediction(first_country_option, second_country_option, friendly_game, neutral_game)

#     # Display the outcome and accuracy
#     st.write(f"Model's Prediction based on inputs:")
#     st.write(result)  # result is now a dictionary, which should prevent the error
# else:
#     st.write('Please make your selections and click submit to see the prediction.')
