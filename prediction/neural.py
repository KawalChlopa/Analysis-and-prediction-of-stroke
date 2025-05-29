from sklearn.model_selection import train_test_split
import keras
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
db_location = os.path.join(parent_dir, 'persistence', 'stroke-dataset.db')
persistence_path = os.path.join(parent_dir, 'persistence')
os.makedirs(persistence_path, exist_ok=True)


conn = duckdb.connect(db_location)
df = conn.execute("SELECT * FROM Indicators").fetchdf()
data = df.drop("state_id", axis='columns')


headers_to_label = [
    'sex', 'had_heart_attack', 'had_angina', 'had_stroke', 'had_asthma',
    'had_skin_cancer', 'had_copd', 'had_depressive_disorder', 'had_kidney_disease',
    'had_arthritis', 'deaf_or_hard_of_hearing', 'blind_or_vision_difficulty',
    'difficulty_concentrating', 'difficulty_walking', 'difficulty_dressing_bathing',
    'difficulty_errands', 'chest_scan', 'alcohol_drinkers', 'hiv_testing',
    'flu_vax_last_12', 'pneumo_vax_ever', 'high_risk_last_year'
]

label_encoders = {}
for column in headers_to_label:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le


X = data.drop(columns=['had_heart_attack'])
y = data['had_heart_attack']


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


xtrain, xtest, ytrain, ytest = train_test_split(X_scaled, y, train_size=0.8, random_state=42)


model = keras.models.Sequential([
    keras.layers.Input(shape=(xtrain.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model.fit(xtrain, ytrain, validation_data=(xtest, ytest), epochs=100, batch_size=32, callbacks=[early_stop])


y_pred_prob = model.predict(xtest)
y_pred = (y_pred_prob >= 0.3).astype(int).flatten()


print("\n Classification Report:")
print(classification_report(ytest, y_pred))


cm = confusion_matrix(ytest, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title(" Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()


model.save(os.path.join(persistence_path, 'neural_network_model.keras'))
joblib.dump(label_encoders, os.path.join(persistence_path, 'label_encoders.joblib'))
joblib.dump(X.columns.tolist(), os.path.join(persistence_path, 'model_features.joblib'))
joblib.dump(scaler, os.path.join(persistence_path, 'scaler.joblib'))

