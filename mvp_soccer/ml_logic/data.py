import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


def get_data():
    #Loading the dataset from a csv-file by using the relative path
    path = "data/results.csv"
    data = pd.read_csv(path)
    return data

def data_preprocessing(data: pd.DataFrame):
    # Creating a new column "result" by transforming the results into "Win", "Lose" or "Draw"
    data.loc[data['home_score'] == data['away_score'], 'result'] = 'Draw'
    data.loc[data['home_score'] > data['away_score'], 'result'] = 'Win'
    data.loc[data['home_score'] < data['away_score'], 'result'] = 'Lose'

    #Creating a new column "friendly" to show if its a friendly game (true - 1) or not (false - 0)
    data.loc[data['tournament'] != 'Friendly', 'friendly'] = 0
    data.loc[data['tournament'] == 'Friendly', 'friendly'] = 1

    #Transofrmimg the values in column "friendly" into int because they are from datatype float
    data = data.astype({'friendly':'int'})

    #Creating a new column "neutral_encoded" by transoforming True into 1 and False into 0
    data['neutral_encoded'] = data['neutral'].apply(lambda x: 0 if x==False else 1)

    return data

def ohe_encoding():
    data = get_data()
    data_preprocessed = data_preprocessing(data)

    # Instantiating Features X (home_team, away_team, friendly, neutral_encoded) and dropping the other columns
    X = data.drop(columns = ['result','neutral', 'city', 'country', 'tournament', 'date', 'home_score', 'away_score'])

    #Selecting the categorical Features before encoding them
    X_categorical = X.select_dtypes(include = ['object'])

    # Instantiating the OHE without a min_frequency
    ohe = OneHotEncoder(sparse_output = False)

    # Fitting it to the categorical features
    ohe.fit(X_categorical)

    return ohe

def feature_encoding(X: pd.DataFrame):
    #Selecting the categorical Features before encoding them
    X_categorical = X.select_dtypes(include = ['object'])

    #Saving the numerical Features in a another variable to let our X untouched
    X_numerical = X.select_dtypes(include = ['int64'])

    ohe = ohe_encoding()

    # Storing the encoded features
    encoded_features = pd.DataFrame(ohe.transform(X_categorical),
                               columns = ohe.get_feature_names_out())
    # Concatenating the numerical and the encoded categorical features
    X_encoded = pd.concat([X_numerical, encoded_features], axis = 1)
    return X_encoded

def target_encoding(y: pd.DataFrame):
   # Instantiating the LabelEncoder
    target_encoder = LabelEncoder()

    # Fitting it to the target and tranforming it to a new variable y_encoded
    y_encoded = target_encoder.fit_transform(y)

    return y_encoded
