from flask import Blueprint, render_template, request
from model import model, predict_kelulusan

# Blueprint untuk routing
main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        nilai_matematika = float(request.form['nilai_matematika'])
        nilai_bahasa = float(request.form['nilai_bahasa'])
        nilai_sains = float(request.form['nilai_sains'])

        # Prediksi kelulusan
        prediction = predict_kelulusan(nilai_matematika, nilai_bahasa, nilai_sains, )
        return render_template('index.html', prediction=prediction)
