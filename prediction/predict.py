import os
import keras
import joblib
import pandas as pd

def predict_heart_attack_neural(sample: dict):

    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    model_path = os.path.join('persistence', 'neural_network_model.keras')
    encoders_path = os.path.join('persistence', 'label_encoders.joblib')
    features_path = os.path.join('persistence', 'model_features.joblib')
    scaler_path = os.path.join('persistence', 'scaler.joblib')

    model = keras.models.load_model(model_path)
    label_encoders = joblib.load(encoders_path)
    model_features = joblib.load(features_path)
    scaler = joblib.load(scaler_path)

    df = pd.DataFrame([sample])
    for column, encoder in label_encoders.items():
        if column in df.columns:
            df[column] = encoder.transform(df[column])

    for col in model_features:
        if col not in df.columns:
            df[col] = 0

    df = df[model_features]
    x_scaled = scaler.transform(df)

    proba = float(model.predict(x_scaled)[0][0])
    prediction = int(proba >= 0.5)

    return prediction, proba


sample_input = {
    'sex': 'Male',
    'had_angina': 'Yes',
    'had_stroke': 'No',
    'had_asthma': 'No',
    'had_skin_cancer': 'No',
    'had_copd': 'No',
    'had_depressive_disorder': 'No',
    'had_kidney_disease': 'No',
    'had_arthritis': 'Yes',
    'deaf_or_hard_of_hearing': 'No',
    'blind_or_vision_difficulty': 'No',
    'difficulty_concentrating': 'No',
    'difficulty_walking': 'No',
    'difficulty_dressing_bathing': 'No',
    'difficulty_errands': 'No',
    'chest_scan': 'No',
    'weight_in_kilograms': 75,
    'alcohol_drinkers': 'Yes',
    'hiv_testing': 'No',
    'flu_vax_last_12': 'Yes',
    'pneumo_vax_ever': 'No',
    'high_risk_last_year': 'No',
    'age_category_id': 3,
    'bmi': 27.5,
    'covid_pos_id': 0,
    'ecigarette_usage_id': 0,
    'general_health_id': 1,
    'had_cancer': 0,
    'had_diabetes': 0,
    'income_id': 2,
    'insurance_id': 1,
    'physical_health_id': 2,
    'race_id': 1,
    'smoker_status_id': 0
}

sample_input2 = {
    'sex': 'Female',
    'had_angina': 'No',
    'had_stroke': 'Yes',
    'had_asthma': 'Yes',
    'had_skin_cancer': 'No',
    'had_copd': 'No',
    'had_depressive_disorder': 'Yes',
    'had_kidney_disease': 'No',
    'had_arthritis': 'Yes',
    'deaf_or_hard_of_hearing': 'No',
    'blind_or_vision_difficulty': 'Yes',
    'difficulty_concentrating': 'Yes',
    'difficulty_walking': 'Yes',
    'difficulty_dressing_bathing': 'No',
    'difficulty_errands': 'Yes',
    'chest_scan': 'Yes',
    'weight_in_kilograms': 88,
    'alcohol_drinkers': 'No',
    'hiv_testing': 'No',
    'flu_vax_last_12': 'Yes',
    'pneumo_vax_ever': 'Yes',
    'high_risk_last_year': 'Yes',
    'age_category_id': 5,
    'bmi': 24.3,
    'covid_pos_id': 0,
    'ecigarette_usage_id': 0,
    'general_health_id': 2,
    'had_cancer': 0,
    'had_diabetes': 1,
    'income_id': 3,
    'insurance_id': 1,
    'physical_health_id': 4,
    'race_id': 2,
    'smoker_status_id': 1
}


high_risk_sample = {
    'sex': 'Male',
    'had_angina': 'Yes',
    'had_stroke': 'Yes',
    'had_asthma': 'No',
    'had_skin_cancer': 'No',
    'had_copd': 'Yes',
    'had_depressive_disorder': 'Yes',
    'had_kidney_disease': 'Yes',
    'had_arthritis': 'Yes',
    'deaf_or_hard_of_hearing': 'No',
    'blind_or_vision_difficulty': 'No',
    'difficulty_concentrating': 'Yes',
    'difficulty_walking': 'Yes',
    'difficulty_dressing_bathing': 'Yes',
    'difficulty_errands': 'Yes',
    'chest_scan': 'Yes',
    'weight_in_kilograms': 80,  # bardzo wysoka masa
    'alcohol_drinkers': 'Yes',
    'hiv_testing': 'No',
    'flu_vax_last_12': 'No',
    'pneumo_vax_ever': 'No',
    'high_risk_last_year': 'Yes',

    # dodatkowe cechy (trzeba było używać przy trenowaniu)
    'age_category_id': 7,       # np. "65-74"
    'bmi': 38.5,                # bardzo wysoki
    'covid_pos_id': 1,          # przeszedł COVID
    'ecigarette_usage_id': 1,   # używa e-papierosów
    'general_health_id': 4,     # bardzo zły stan zdrowia
    'had_cancer': 1,            # miał raka
    'had_diabetes': 1,          # cukrzyca
    'income_id': 0,             # bardzo niskie dochody
    'insurance_id': 0,          # brak ubezpieczenia
    'physical_health_id': 25,   # 25 dni złego zdrowia w miesiącu
    'race_id': 3,               # dowolna wartość, zależna od kodowania
    'smoker_status_id': 2       # obecny palacz
}

low_risk_sample = {
    'sex': 'Female',
    'age_category_id': 1,              # np. 18–24 lata
    'bmi': 21.5,
    'weight_in_kilograms': 58,
    'had_angina': 'No',
    'had_stroke': 'No',
    'had_asthma': 'No',
    'had_skin_cancer': 'No',
    'had_copd': 'No',
    'had_depressive_disorder': 'No',
    'had_kidney_disease': 'No',
    'had_arthritis': 'No',
    'deaf_or_hard_of_hearing': 'No',
    'blind_or_vision_difficulty': 'No',
    'difficulty_concentrating': 'No',
    'difficulty_walking': 'No',
    'difficulty_dressing_bathing': 'No',
    'difficulty_errands': 'No',
    'general_health_id': 0,            # Excellent
    'ecigarette_usage_id': 0,          # Never
    'covid_pos_id': 0,                 # No
    'chest_scan': 'No',
    'alcohol_drinkers': 'No',
    'hiv_testing': 'No',
    'flu_vax_last_12': 'Yes',
    'pneumo_vax_ever': 'Yes',
    'high_risk_last_year': 'No'
}

prediction, probability = predict_heart_attack_neural(low_risk_sample)
print(f"Prawdopodobieństwo zawału: {probability:.2%}")