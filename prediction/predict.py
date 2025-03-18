import numpy as np
import keras



def predict_heart_disease_probability(sample, data):
    model = keras.models.load_model(data)
    sample = np.array(sample).reshape(1, -1)
    return model.predict(sample)[0, 0]

sample_data = [0.14137389834600994,1,0,1,0.0,0.0,0,1,0.5,1.0,0.0,0,0.0,0.21739130434782608,0,1,1]

probability = predict_heart_disease_probability(sample_data,"heart_disease_model.keras")
print(f"Probabilty of heart attack: {probability:.2f}")