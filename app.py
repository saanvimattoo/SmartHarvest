import numpy as np
from flask import Flask, request, render_template
import pickle
import joblib
import pandas as pd

app = Flask(__name__)

# Load models
crop_model = pickle.load(open('model.pkl', 'rb'))
crop_scaler = pickle.load(open('scaler.pkl', 'rb'))
yield_model = joblib.load('crop_yield_model.pkl')

# Crop dictionary
crop_dict = {
    1: {"name":"rice", "image": "rice.png"}, 
    2: {"name":"maize", "image": "maize.png"},
    3: {"name":"chickpea", "image": "chickpea.png"},
    4: {"name":"kidneybeans", "image": "kidneybeans.png"},
    5: {"name":"pigeonpeas", "image": "pigeonpeas.png"},
    6: {"name":"mothbeans", "image": "mothbeans.png"},
    7: {"name":"mungbean", "image": "mungbean.png"}, 
    8: {"name":"blackgram", "image": "blackgram.png"},
    9: {"name":"lentil", "image": "lentil.png"},
    10: {"name":"pomegranate", "image": "pomegranate.png"},
    11: {"name":"banana", "image": "banana.png"},
    12: {"name":"mango", "image": "mango.png"},    
    13: {"name":"grapes", "image": "grapes.png"}, 
    14: {"name":"watermelon", "image": "watermelon.png"},
    15: {"name":"muskmelon", "image": "muskmelon.png"},
    16: {"name":"apple", "image": "apple.png"},
    17: {"name":"orange", "image": "orange.png"},
    18: {"name":"papaya", "image": "papaya.png"},     
    19: {"name":"coconut", "image": "coconut.png"}, 
    20: {"name":"cotton", "image": "cotton.png"},
    21: {"name":"jute", "image": "jute.png"},
    22: {"name":"coffee", "image": "coffee.png"}
    
}

@app.route('/weather')
def detailed_weather():
    return render_template('weather.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    crop_result = None
    crop_image = None
    yield_result = None
    
    if request.method == 'POST':
        # Handle crop recommendation form
        if 'Nitrogen' in request.form:
            N = int(request.form['Nitrogen'])
            P = int(request.form['Phosphorus'])
            K = int(request.form['Potassium'])
            temperature = float(request.form['Temperature'])
            humidity = float(request.form['Humidity'])
            ph = float(request.form['pH'])
            rainfall = float(request.form['Rainfall'])

            feature_list = [N, P, K, temperature, humidity, ph, rainfall]
            single_pred = np.array(feature_list).reshape(1,-1)
            single_pred_scaled = crop_scaler.transform(single_pred)
            prediction = crop_model.predict(single_pred_scaled)

            if prediction[0] in crop_dict:
                crop = crop_dict[prediction[0]]
                crop_result = f"{crop['name']} is the best crop to be cultivated"
                crop_image = crop['image']
            else:
                crop_result = "No recommendation available"
                crop_image = "default.png"
        
        # Handle yield prediction form
        elif 'yield_N' in request.form:
            input_data = {
                'N': float(request.form['yield_N']),
                'P': float(request.form['yield_P']),
                'K': float(request.form['yield_K']),
                'pH': float(request.form['yield_pH']),
                'rainfall': float(request.form['yield_rainfall']),
                'temperature': float(request.form['yield_temperature']),
                'State_Name': request.form['State_Name'],
                'Crop': request.form['Crop']
            }

            df = pd.DataFrame([input_data])
            prediction = yield_model.predict(df)[0]
            yield_result = f'Predicted Yield: {prediction:.2f} tons/hectare'

    return render_template("index.html", 
                           crop_result=crop_result, 
                           crop_image=crop_image,
                           yield_result=yield_result)

if __name__ == "__main__":
    app.run(debug=True)