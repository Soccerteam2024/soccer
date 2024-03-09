from fastapi import FastAPI
import pandas as pd
from mvp_soccer.ml_logic.data import feature_encoding
import pickle

api = FastAPI()

# define a root `/` endpoint
@api.get("/")
def index():
    return {"ok": "API connected"}


@api.get("/predict")
def predict(feature1, feature2, feature3, feature4):
    filename = 'mvp_soccer/ml_logic/best_model/soccer_model.pkl'
    model = pickle.load(open(filename, 'rb'))
    # Creating a new DataFrame for first Prediction
    new_result = pd.DataFrame(columns = ['home_team', 'away_team', 'friendly', 'neutral_encoded'])
    # Adding some content to the new DataFrame
    new_result.loc[0] = [feature1, feature2, int(feature3),int(feature4)]


    X_categorical = new_result.select_dtypes(include = ['object'])
    X_numerical = new_result.select_dtypes(include = ['int64'])

    X_new_encoded = feature_encoding(new_result)
    prediction = model.predict(X_new_encoded)

    # Here, I'm only returning the features, since I don't actually have a model.
    # In a real life setting, you would return the predictions.

    return {'prediction': prediction[0]}

#print(predict('Ghana', 'Germany', 0, 1))
