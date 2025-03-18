import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from sklearn.metrics import accuracy_score, classification_report



def neural_network(data_file):
    df = pd.read_csv(data_file)

    df_0 = df[df["HeartDisease"] == 0].sample(frac=0.5, random_state=42)
    df_1 = df[df["HeartDisease"] == 1]
    df = pd.concat([df_0, df_1]).sample(frac=1, random_state=42).reset_index(drop=True)

    x = df.drop(columns=["HeartDisease"])
    y = df["HeartDisease"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = keras.Sequential([
        keras.layers.Input(shape=(x_train.shape[1],)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_test, y_test), verbose=1)


    model.save("heart_disease_model.keras")


neural_network('test3.csv')