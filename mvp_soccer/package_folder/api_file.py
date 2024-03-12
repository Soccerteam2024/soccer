from fastapi import FastAPI
import pandas as pd
import os
from package_folder.data import feature_encoding
import pickle

api = FastAPI()

# Calculate the path to the model file relative to this script's location
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, '../models/soccer_model.pkl')  # Adjust the relative path as necessary

# define a root `/` endpoint
@api.get("/")
def index():
    return {"ok": "API connected"}

@api.get("/predict")
def predict(feature1, feature2, feature3, feature4):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Creating a new DataFrame for first Prediction
    new_result = pd.DataFrame(columns = ['home_team', 'away_team', 'friendly', 'neutral_encoded'])
    # Adding some content to the new DataFrame
    new_result.loc[0] = [feature1, feature2, int(feature3),int(feature4)]


    X_categorical = new_result.select_dtypes(include = ['object'])
    X_numerical = new_result.select_dtypes(include = ['int64'])

    X_new_encoded = feature_encoding(new_result)
    prediction = model.predict(X_new_encoded)

    return {'prediction': prediction[0]}
