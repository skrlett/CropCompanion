import pandas as pd
import xgboost as xgb
import joblib

# Load saved preprocessing models and trained XGBoost model
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")
model = xgb.Booster()
model.load_model("xgboost_model.json")

def predict_crop_probabilities(inputs_df):
    """
    Accepts a list of soil and climate condition inputs, preprocesses them,
    and returns probability distributions over all crop categories.
    """
    
    # Standardize input data
    input_data_scaled = scaler.transform(inputs_df)
    dinput = xgb.DMatrix(input_data_scaled)
    
    # Predict probabilities
    probabilities = model.predict(dinput)
    
    # Convert probabilities to readable format
    crop_names = label_encoder.inverse_transform(range(len(probabilities[0])))
    results = [dict(zip(crop_names, prob_row)) for prob_row in probabilities]

    return {"predictions": results}