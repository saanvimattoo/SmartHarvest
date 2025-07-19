# SmartHarvest 🌾

**SmartHarvest** is a machine learning–powered platform designed to assist farmers and agricultural stakeholders in making data-driven decisions. It integrates three key modules:

- ✅ Crop Recommendation  
- 📈 Crop Yield Prediction  
- 🌦️ Live Weather & Forecast  

Built using Python, Flask, and real-time weather APIs, SmartHarvest supports precision agriculture and sustainable farming practices.

---

## 🌐 Live Demo

🔗 [https://smartharvest-6a3f.onrender.com/](https://smartharvest-6a3f.onrender.com/)

Try it out live — no installation needed!

---

## 📚 Features

- Crop recommendation based on soil nutrients, temperature, humidity, and more
- Yield prediction using regression models trained on historical data
- Real-time weather updates and air quality info via OpenWeatherMap API
- Responsive web UI using HTML, CSS, JavaScript, and jQuery
- Flask-powered backend for unified integration of ML models and live data

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Backend**: Flask  
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, jQuery  
- **Machine Learning**: scikit-learn, XGBoost, LightGBM  
- **Deployment**: Render  
- **APIs**: OpenWeatherMap for weather and air quality  

---

## 🚀 How to Run Locally

1. **Clone the repository**

    ```
    git clone https://github.com/saanvimattoo/SmartHarvest.git
    cd SmartHarvest
    ```

2. **Create and activate a virtual environment** (optional but recommended)

    ```
    python -m venv venv
    source venv/bin/activate      # For Linux/Mac
    venv\Scripts\activate         # For Windows
    ```

3. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Run the app**

    ```
    python app.py
    ```

5. **Visit in your browser**

    ```
    http://localhost:5000
    ```

---

## 🧠 ML Modules Overview

### 🌱 Crop Recommendation

- Input: N, P, K, pH, humidity, rainfall, temperature
- Models Tested: Logistic Regression, Naive Bayes, SVM, Random Forest, XGBoost
- Best Model: Random Forest (highest accuracy)
- Output: Suggested crop

### 🌾 Crop Yield Prediction

- Input: State, Crop, N, P, K, pH, temperature, rainfall
- Models: Linear Regression, Gradient Boosting, XGBoost, LightGBM
- Output: Predicted yield (tons per hectare)

---

## 🌦️ Live Weather Module

- Built with HTML, CSS, JavaScript + OpenWeatherMap API
- Provides:
  - Current weather (with background & icon updates)
  - Air Quality Index (AQI, PM2.5, PM10, etc.)
  - 5-day forecast + hourly forecast
- Dynamic UI adjusts based on weather/time

---

## 🌱 Future Scope

- 📱 Mobile app version for farmers
- 🤖 Chatbot for crop/weather queries
- 🗣️ Voice-based interaction
- 🌿 Plant disease detection via image upload

---

## 👩‍💻 Built By

**Saanvi Mattoo** – ML Engineer & Fullstack Developer  
*(Collaborated with peers as part of an industrial-oriented mini project)*

---

## 📬 Contact

[GitHub – @saanvimattoo](https://github.com/saanvimattoo)

---

## 📄 References

- OpenWeatherMap API – [https://openweathermap.org/api](https://openweathermap.org/api)  
- scikit-learn – [https://scikit-learn.org](https://scikit-learn.org)  
- XGBoost – [https://xgboost.readthedocs.io](https://xgboost.readthedocs.io)  
- Flask – [https://flask.palletsprojects.com](https://flask.palletsprojects.com)  

