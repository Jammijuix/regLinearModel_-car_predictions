V# 🚗 Vehicle Price Prediction App

A Streamlit web application that predicts vehicle prices using a pre-trained linear regression model, with an interactive feature importance chart powered by Plotly.

---

## Features

- **Sidebar Input Panel** — Select vehicle attributes (make, body style, drivetrain, transmission, engine aspiration, body size, horsepower, torque) to configure a vehicle for prediction.
- **Feature Importance Chart** — Interactive horizontal bar chart showing which features most influence the model's predictions.
- **Price Prediction** — Instantly predicts vehicle price in USD based on selected features.

---

## Project Structure

```
├── Regr_model_cars.py        # Main Streamlit application
├── linear_model.pkl          # Pre-trained linear regression model (pickle)
├── feature_importance.xlsx   # Feature importance scores for the chart
├── Pic 1.png                 # Sidebar image/logo
├── Pic 2.png                 # Top banner image
└── README.md
```

---

## Requirements

Install dependencies with:

```bash
pip install streamlit numpy pandas plotly openpyxl pillow scikit-learn
```

> **Note:** `scikit-learn` must be the same version used when training and pickling `linear_model.pkl`, otherwise the model may fail to load.

---

## How to Run

```bash
streamlit run Regr_model_cars.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Model Details

- **Algorithm:** Linear Regression
- **Input Features:** 36 features (2 numeric + 34 one-hot encoded categorical)
- **Numeric Features:** Horsepower, Torque
- **Categorical Features:**
  - **Make:** Aston Martin, Audi, BMW, Bentley, Ford, Mercedes-Benz, Nissan
  - **Body Size:** Large, Compact, Midsize
  - **Body Style:** SUV, Sedan, Wagon, Hatchback, Coupe, Convertible, Convertible SUV, Cargo Van, Pickup Truck, Passenger Van, Cargo Minivan, Passenger Minivan
  - **Engine Aspiration:** Twin-Turbo, Turbocharged, Electric Motor, Twincharged, Naturally Aspirated, Supercharged
  - **Drivetrain:** 4WD, AWD, FWD, RWD
  - **Transmission:** Automatic, Manual
- **Output:** Predicted vehicle price in USD

---

## Usage

1. Use the **left sidebar** to select vehicle features.
2. View the **Feature Importance** chart on the left to understand what drives the prediction.
3. Click the **"Predict"** button on the right panel to generate a price estimate.

---

## Known Limitations

- The model supports only the 7 car makes listed in the sidebar. Vehicles from other manufacturers are not supported.
- Predictions are based on a linear regression model and may not capture non-linear price relationships.
- The `linear_model.pkl` file must be present in the same directory as the app to run# 🚗 Vehicle Price Prediction App

A Streamlit web application that predicts vehicle prices using a pre-trained linear regression model, with an interactive feature importance chart powered by Plotly.

---

## Features

- **Sidebar Input Panel** — Select vehicle attributes (make, body style, drivetrain, transmission, engine aspiration, body size, horsepower, torque) to configure a vehicle for prediction.
- **Feature Importance Chart** — Interactive horizontal bar chart showing which features most influence the model's predictions.
- **Price Prediction** — Instantly predicts vehicle price in USD based on selected features.

---

## Project Structure

```
├── Regr_model_cars.py        # Main Streamlit application
├── linear_model.pkl          # Pre-trained linear regression model (pickle)
├── feature_importance.xlsx   # Feature importance scores for the chart
├── Pic 1.png                 # Sidebar image/logo
├── Pic 2.png                 # Top banner image
└── README.md
```

---

## Requirements

Install dependencies with:

```bash
pip install streamlit numpy pandas plotly openpyxl pillow scikit-learn
```

> **Note:** `scikit-learn` must be the same version used when training and pickling `linear_model.pkl`, otherwise the model may fail to load.

---

## How to Run

```bash
streamlit run Regr_model_cars.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Model Details

- **Algorithm:** Linear Regression
- **Input Features:** 36 features (2 numeric + 34 one-hot encoded categorical)
- **Numeric Features:** Horsepower, Torque
- **Categorical Features:**
  - **Make:** Aston Martin, Audi, BMW, Bentley, Ford, Mercedes-Benz, Nissan
  - **Body Size:** Large, Compact, Midsize
  - **Body Style:** SUV, Sedan, Wagon, Hatchback, Coupe, Convertible, Convertible SUV, Cargo Van, Pickup Truck, Passenger Van, Cargo Minivan, Passenger Minivan
  - **Engine Aspiration:** Twin-Turbo, Turbocharged, Electric Motor, Twincharged, Naturally Aspirated, Supercharged
  - **Drivetrain:** 4WD, AWD, FWD, RWD
  - **Transmission:** Automatic, Manual
- **Output:** Predicted vehicle price in USD

---

## Usage

1. Use the **left sidebar** to select vehicle features.
2. View the **Feature Importance** chart on the left to understand what drives the prediction.
3. Click the **"Predict"** button on the right panel to generate a price estimate.

---

## Known Limitations

- The model supports only the 7 car makes listed in the sidebar. Vehicles from other manufacturers are not supported.
- Predictions are based on a linear regression model and may not capture non-linear price relationships.
- The `linear_model.pkl` file must be present in the same directory as the app to run.