import os
import zipfile
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import log_loss, f1_score
import matplotlib.pyplot as plt
import joblib
# import numpy as np

# Extract training data csv file from zip file
current_directory = os.path.join(os.getcwd(), 'mlmodel')
zip_file_path = os.path.join(current_directory, 'training-dataset.zip')

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(current_directory)

# Load csv file to pandas dataframe
file_path = os.path.join(current_directory, 'Crop_Recommendation.csv')
df = pd.read_csv(file_path)

print(df.head())


# Data Preprocessing

# Encode the target variable (Crop) into numerical format
label_encoder = LabelEncoder()
df['Crop'] = label_encoder.fit_transform(df['Crop'])

# Separate features and target variable
X = df.drop(columns=['Crop'])  # Independent variables
y = df['Crop']  # Dependent variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize feature values to improve model performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save the scaler and label encoder for later use in predictions
joblib.dump(scaler, "mlmodel/scaler.pkl")
joblib.dump(label_encoder, "mlmodel/label_encoder.pkl")


# Model Training

# Convert data into XGBoost DMatrix format for optimized training
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

## Model hyperparameters (balanced for classification)
params = {
    'objective': 'multi:softprob',  # Multi-class classification with probability output
    'num_class': 22,  # Number of crop categories
    'eval_metric': 'mlogloss',  # Log loss as evaluation metric
    'max_depth': 6,  # Limits tree depth to prevent overfitting
    'learning_rate': 0.1,  # Balances convergence speed and generalization
    'n_estimators': 100,  # Number of boosting rounds
    'subsample': 0.8,  # Prevents overfitting by using 80% of data per tree
    'colsample_bytree': 0.8,  # Uses 80% of features per tree to enhance diversity
    'random_state': 42  # Ensures reproducibility
}

## Train XGBoost model
model = xgb.train(params, dtrain, num_boost_round=100)


# Model Evaluation

## Predict probabilities on test set
y_pred_prob = model.predict(dtest)  # Output is a (num_samples, 22) array

# Save the trained model for later use
model.save_model("mlmodel/xgboost_model.json")

## Evaluate using log loss
loss = log_loss(y_test, y_pred_prob)
print(f'Log Loss: {loss:.4f}')

# # Evaluate model performance using F1 score
# y_pred = np.argmax(y_pred_prob, axis=1)
# f1 = f1_score(y_test, y_pred, average='macro') # if dataset has unbalanced classes, use average='weighted'
# print(f"F1 Score: {f1}")