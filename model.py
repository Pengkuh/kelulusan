from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

# Dataset contoh
data = {
    'Nilai_Matematika': [80, 70, 60, 85, 55],
    'Nilai_Bahasa_Indonesia': [75, 65, 85, 80, 60],
    'Nilai_Sains': [80, 60, 75, 90, 50],
    'Status_Lulus': ['Lulus', 'Tidak Lulus', 'Lulus', 'Lulus', 'Tidak Lulus']
}

df = pd.DataFrame(data)
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
