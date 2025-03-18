import pandas as pd
import sklearn
import joblib

df = pd.read_csv('../data/heart_2020_cleaned.csv')


headers = ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'Diabetic', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer', 'AgeCategory', 'GenHealth', 'Race']
label_encoders = {}
for column in headers:
    le = sklearn.preprocessing.LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

df.to_csv('labeled_data.csv', index=False)

scaler = sklearn.preprocessing.MinMaxScaler()
df[["BMI", "SleepTime", "PhysicalHealth", "MentalHealth", "Diabetic", "AgeCategory", "GenHealth", "Race"]] = scaler.fit_transform(df[["BMI", "SleepTime", "PhysicalHealth", "MentalHealth", "Diabetic",  "AgeCategory", "GenHealth", "Race"]])


df_0 = df[df["HeartDisease"] == 0].sample(frac=0.2, random_state=42)
df_1 = df[df["HeartDisease"] == 1]
df = pd.concat([df_0, df_1]).sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv('prepared_data.csv', index=False)
joblib.dump(scaler, "scaler.pkl")

