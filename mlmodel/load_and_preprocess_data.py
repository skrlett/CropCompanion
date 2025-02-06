import zipfile
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBClassifier, XGBRegressor
# import joblib
extract_folder = 'mlmodel/'

with zipfile.ZipFile('training-dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(extract_folder)


file_path = os.path.join(extract_folder, 'Crop_Recommendation.csv')
df = pd.read_csv(file_path)

print(df.head())

df.drop_duplicates(inplace=True)

# Might need to outlier values using IQR Method for Rain, Humidity, PH and Temperature
# Q1 = df['rainfall'].quantile(0.25)
# Q3 = df['rainfall'].quantile(0.75)
# IQR = Q3 - Q1
# data = df[(data['rainfall'] >= (Q1 - 1.5 * IQR)) & (df['rainfall'] <= (Q3 + 1.5 * IQR))]



# mm of rain / month categorizing rain
#bins_rainfall = [0, 50, 100]
#labels_rainfall = ['Low' , ' Moderate', 'Heavy']
# df['rainfall_category'] = pd.cut(df['rainfall'], bins=bins_rainfall, labels=labels_rainfall)

# Categorizing ph where 7 is neutral 
#bins_ph = [0, 7 , 14]
#labels_ph = ['Low' , ' Moderate', 'High']
# df['ph_category'] = pd.cut(df['ph_value'], bins=bins_ph, labels=labels_ph)

# Categorizing Humidity 
#bins_humidity = [0, 7 , 14]
#labels_humidity = ['Low' , ' Moderate', 'High']
# df['humidity_category'] = pd.cut(df['humidity'], bins=bins_humidity, labels=labels_humidity)

# Categorizing Temperature
#bins_temp = [0, 7 , 14]
#labels_temp = ['Low' , ' Moderate', 'High']
# df['temp_category'] = pd.cut(df['temperature'], bins=bins_temp, labels=labels_temp)


# One hot encoding
df = pd.get_dummies(df, columns=['Crop', 'ph_category', 'rainfall_category', 'temp_category', 'humidity_category'])

#If categorize some data for Feature Selection should those categories be used instead?
X = df[['Nitrogen', 'Phosphorus', 'Potassium', 'temp_category', 'Humidity', 'ph_category', 'rainfall']]
y = df['Crop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")

# Save model for future use 
# joblib.dump(model, 'xgboost_crop_companion_model.pkl')