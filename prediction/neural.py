import duckdb
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
db_location = os.path.join(parent_dir, 'persistence', 'stroke-dataset.db')
model_path = os.path.join(parent_dir, 'persistence', 'random_forest_model.joblib')
feature_list_path = os.path.join(parent_dir, 'persistence', 'model_features.joblib')


conn = duckdb.connect(db_location)
df = conn.execute("SELECT * FROM Indicators").fetchdf()
data = df.drop("state_id", axis='columns')

headers_to_label = ['sex', 'had_heart_attack', 'had_angina', 'had_stroke',
 'had_asthma', 'had_skin_cancer', 'had_copd', 'had_depressive_disorder',
 'had_kidney_disease', 'had_arthritis', 'deaf_or_hard_of_hearing',
 'blind_or_vision_difficulty', 'difficulty_concentrating', 'difficulty_walking',
 'difficulty_dressing_bathing', 'difficulty_errands', 'chest_scan',
 'weight_in_kilograms', 'alcohol_drinkers',
 'hiv_testing', 'flu_vax_last_12', 'pneumo_vax_ever', 'high_risk_last_year']

label_encoders = {}
for column in headers_to_label:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

x = data.drop(columns=['had_heart_attack'])
y = data['had_heart_attack']
xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.8, random_state=42)

model = RandomForestClassifier()
model.fit(xtrain, ytrain)

joblib.dump(model, model_path)
joblib.dump(list(x.columns), feature_list_path)
