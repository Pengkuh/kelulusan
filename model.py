from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

# Membaca data dari file Excel
df = pd.read_excel('data_kelulusan.xlsx')

# Pisahkan fitur dan target
X = df.drop('Status_Lulus', axis=1)  # Fitur
y = df['Status_Lulus']  # Target

# Model training
model = RandomForestClassifier()
model.fit(X, y)

# Fungsi untuk prediksi kelulusan
def predict_kelulusan(nilai_matematika, nilai_bahasa, nilai_sains):
    input_data = np.array([[nilai_matematika, nilai_bahasa, nilai_sains]])
    prediction = model.predict(input_data)
    return prediction[0]
