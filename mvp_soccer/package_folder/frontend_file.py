# import streamlit as st
# import pandas as pd
# import numpy as np
# import requests
# from package_folder.data import get_data
# from package_folder.api_file import predict


# # Example list of 190 countries (for demonstration, using fewer)
# countries = get_data()
# home_team = countries['home_team'].unique()
# away_team = countries['away_team'].unique()


# # User selects the 1st and 2nd country
# first_country_option = st.selectbox('Select 1st country', home_team)
# second_country_option = st.selectbox('Select 2nd country', away_team)

# # User inputs for game type
# friendly_game = st.radio('Is it a friendly game?', ('Yes', 'No'))
# neutral_game = st.radio('Is it a neutral game?', ('Yes', 'No'))



# # User submits their selections
# if st.button('Submit'):
#     # Perform model prediction
#     friendly_game = 1 if friendly_game == 'Yes' else 0
#     neutral_game = 1 if neutral_game == 'Yes' else 0
#     result = predict(first_country_option, second_country_option, friendly_game, neutral_game)

#     # Display the outcome and accuracy
#     st.write(f"Model's Prediction based on inputs:")
#     st.write(result)  # result is now a dictionary, which should prevent the error
# else:
#     st.write('Please make your selections and click submit to see the prediction.')



# response = requests.get(f"https://soccer4-tefknaii7q-ew.a.run.app/predict?feature1={1}&feature2={1}&feature3={1}&feature={1}").json()
# st.write("The prediction is", str(response['prediction']))




# Newly generated code:
import streamlit as st
import pandas as pd
import numpy as np
import requests
from package_folder.data import get_data
from package_folder.api_file import predict

# Fetching the countries data
countries_data = get_data()
home_teams = countries_data['home_team'].unique()
away_teams = countries_data['away_team'].unique()

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

    # Perform model prediction
    prediction_result = predict(first_country_option, second_country_option, friendly_game_bool, neutral_game_bool)

#     # Display the outcome
#     st.write("Model's Prediction based on inputs:")
#     st.write(prediction_result)  # Assuming prediction_result is already in a display-friendly format
# else:
#     st.write('Please make your selections and click submit to see the prediction.')

      # # Display the outcome FANCIER WAY
    if prediction_result:
            st.success(f"Prediction: {prediction_result['prediction']}")
            # Additional formatting can go here, e.g., showing an icon, a picture, or custom styling
            # Example: st.image('path_to_some_relevant_image.jpg')
    else:
            st.error("Unable to generate prediction. Please try again.")
else:
        st.write('Please make your selections and click submit to see the prediction.')
