import os
import joblib
import pandas as pd

def predict_heart_attack(sample: dict):
    # Ścieżki
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    model_path = os.path.join(parent_dir, 'persistence', 'random_forest_model.joblib')
    encoders_path = os.path.join(parent_dir, 'persistence', 'label_encoders.joblib')
    features_path = os.path.join(parent_dir, 'persistence', 'model_features.joblib')

    # Wczytaj model, encodery i listę cech
    model = joblib.load(model_path)
    label_encoders = joblib.load(encoders_path)
    model_features = joblib.load(features_path)

    # Zamień słownik na DataFrame
    df = pd.DataFrame([sample])

    # Zakoduj dane
    for column, encoder in label_encoders.items():
        if column in df.columns:
            df[column] = encoder.transform(df[column])

    # Uzupełnij brakujące kolumny zerami (lub innymi wartościami domyślnymi)
    for col in model_features:
        if col not in df.columns:
            df[col] = 0  # lub np. df[col] = 'Unknown' jeśli to tekst

    # Upewnij się, że kolumny są w tej samej kolejności
    df = df[model_features]

    # Predykcja
    prediction = model.predict(df)[0]
    return prediction

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
    'had_stroke': 'No',
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
    'weight_in_kilograms': 68,
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

result = predict_heart_attack(sample_input2)
print("Prawdopodobieństwo zawału (1 = TAK, 0 = NIE):", result)
