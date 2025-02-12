import pandas as pd
import xgboost as xgb
import joblib

# Load saved preprocessing models and trained XGBoost model
scaler = joblib.load("mlmodel/scaler.pkl")
label_encoder = joblib.load("mlmodel/label_encoder.pkl")
model = xgb.Booster()
model.load_model("mlmodel/xgboost_model.json")

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
    all_survival_probabilities = [dict(zip(crop_names, prob_row)) for prob_row in probabilities][0]
    
    # Filter the dictionary to only include items with values above 0.5
    filtered_probabilities = {crop: prob for crop, prob in all_survival_probabilities.items() if prob > 0.5}
    if len(filtered_probabilities) == 0:
        crop = max(all_survival_probabilities)
        odds = all_survival_probabilities[crop]
        return (
            f"No crops in our compendium have a survival probability of 50% or higher "
            f"for your conditions. The best option for you is {crop} with a survival "
            f"probability of {odds:.4f}."
        )
    return f"Here are the crops with a probability of survival above 50% in your conditions: {filtered_probabilities}"