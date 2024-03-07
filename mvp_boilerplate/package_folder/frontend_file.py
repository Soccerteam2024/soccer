# import streamlit as st
# import requests

# st.title("My iris classifier app")

# st.write("Select your features")

# # Creating four sliders
# value1 = st.slider('Select a value for Sepal length', min_value=0, max_value=4, value=1, step=1)
# value2 = st.slider('Select a value for Sepal width',  min_value=0, max_value=4, value=1, step=1)
# value3 = st.slider('Select a value for Petal length',  min_value=0, max_value=4, value=1, step=1)
# value4 = st.slider('Select a value for Petal width',  min_value=0, max_value=4, value=1, step=1)

# # TEST LINE
# response = requests.get(f"https://mvp-b3jhtp774a-ew.a.run.app/predict?sepal_length={value1}&sepal_width={value2}&petal_length={value3}&petal_width={value4}").json()
# st.write("The flower belongs to class", str(response['prediction']))


#NEW FRONTEND

import streamlit as st
import pandas as pd
import numpy as np
import requests

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

#      User submits their selections
if st.button('Submit'):
    # Perform model prediction
    result = model_prediction(first_country_option, second_country_option, friendly_game, neutral_game)

    # Display the outcome and accuracy
    st.write(f"Model's Prediction based on inputs:")
    st.write(result)  # result is now a dictionary, which should prevent the error
else:
    st.write('Please make your selections and click submit to see the prediction.')



response = requests.get(f"https://soccer3-tefknaii7q-ew.a.run.app/predict?first_country_option={1}&second_country_option={1}&friendly_game={1}&neutral_game={1}").json()
st.write("The prediction is", str(response['prediction']))
