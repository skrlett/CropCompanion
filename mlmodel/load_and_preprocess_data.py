import zipfile
import os
import pandas as pd
extract_folder = 'mlmodel/'

with zipfile.ZipFile('training-dataset.zip', 'r') as zip_ref:
    zip_ref.extractall(extract_folder)


file_path = os.path.join(extract_folder, 'Crop_Recommendation.csv')
df = pd.read_csv(file_path)

print(df.head())