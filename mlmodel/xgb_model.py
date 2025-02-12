import pandas as pd
import xgboost as xgb
import joblib

import os
from joblib import load

file_path_scalar = os.path.join(os.path.dirname(__file__), "scaler.pkl")
file_path_label_encoder = os.path.join(os.path.dirname(__file__), "label_encoder.pkl")
file_path_xgboost_model = os.path.join(os.path.dirname(__file__), "xgboost_model.json")
scaler = load(file_path_scalar)

# Load saved preprocessing models and trained XGBoost model
label_encoder = joblib.load(file_path_label_encoder)
model = xgb.Booster()
model.load_model(file_path_xgboost_model)

# ['Nitrogen', 'Phosphorus', 'Potassium', 'temp_category', 'Humidity', 'ph_category', 'rainfall']
def create_dataframe(nitrogen, phosphorus, potassium, temp_category, humidity, ph_category, rainfall):
    """
    Create a Pandas DataFrame from the given inputs.
    
    Parameters:
        nitrogen (list): List of nitrogen values
        phosphorus (list): List of phosphorus values
        potassium (list): List of potassium values
        temp_category (list): List of temperature categories
        humidity (list): List of humidity values
        ph_category (list): List of pH categories
        rainfall (list): List of rainfall values
    
    Returns:
        pd.DataFrame: DataFrame containing the provided data
    """
    data = {
        'Nitrogen': nitrogen,
        'Phosphorus': phosphorus,
        'Potassium': potassium,
        'Temperature': temp_category,
        'Humidity': humidity,
        'pH_Value': ph_category,
        'Rainfall': rainfall
    }
    
    return pd.DataFrame(data, index=[0])

def predict_crop_probabilities(nitrogen, phosphorus, potassium, temp_category, humidity, ph_category, rainfall):
    df = create_dataframe(nitrogen, phosphorus, potassium, temp_category, humidity, ph_category, rainfall)
    return predict_crop_probabilities_util(df)


def predict_crop_probabilities_util(inputs_df):
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

    top_crops = []
    for result in results:
        # Sort crops by probability in descending order and get the top 5
        top_five = sorted(result.items(), key=lambda item: item[1], reverse=True)[:5]
        top_crops.append(dict(top_five))
    
    return {"predictions": str(top_crops)}