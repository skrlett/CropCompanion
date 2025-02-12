import pandas as pd
from xgb_model import predict_crop_probabilities

# Sample input data
poor_fit_conditions_sample = {
    'Nitrogen': [20],
    'Phosphorus': [70],
    'Potassium': [10],
    'Temperature': [24.54865288],
    'Humidity': [50.43893213],
    'pH_Value': [6.435654327],
    'Rainfall': [70.9345287]
}

well_fit_conditions_sample = {
    'Nitrogen': [80],
    'Phosphorus': [50],
    'Potassium': [40],
    'Temperature': [21.54865288],
    'Humidity': [81.43893213],
    'pH_Value': [7.435654327],
    'Rainfall': [251.9345287]
}

# Convert sample data to DataFrame
poor_fit_df = pd.DataFrame(poor_fit_conditions_sample)
well_fit_df = pd.DataFrame(well_fit_conditions_sample)

# Predict crop probabilities
poor_fit_predictions = predict_crop_probabilities(poor_fit_df)
well_fit_predictions = predict_crop_probabilities(well_fit_df)

# Print the predictions
print("Predictions for poor fit conditions:", poor_fit_predictions)
print("Predictions for well fit conditions:", well_fit_predictions)