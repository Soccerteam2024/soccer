from fastapi import FastAPI
import pickle
from package_folder.utils import from_number_to_flower

app = FastAPI()

@app.get("/")
def root():
    return {'greeting':"hello"}

@app.get("/predict")
def predict(first_country_option,
            second_country_option,
            friendly_game,
            neutral_game):

    with open('models/best_model.pkl', 'rb') as file:
        model = pickle.load(file)

    prediction = model.predict([[first_country_option,second_country_option,friendly_game,neutral_game]])

    pretty_prediction = from_number_to_flower(float(prediction[0]))

    return {"prediction": pretty_prediction}
