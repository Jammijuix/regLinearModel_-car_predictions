import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px
from PIL import Image
import openpyxl
import os


#page configuration
st.set_page_config(layout="wide")

#load your pre-load model

with open("linear_model.pkl", "rb") as f:
    lm2 = pickle.load(f)

#load feature Importance from the excel file
def load_feature_importance(file_path):
    return pd.read_excel(file_path)

#load feature importance  into dataFrame

final_fi = load_feature_importance("feature_importance.xlsx")

#sidebar setup
Base_dir = os.path.dirname(__file__)

image_sidebar = Image.open(os.path.join(Base_dir, "pic1.png"))
st.sidebar.image(image_sidebar, width="stretch")
st.sidebar.header("Vehicle Features")

#feature selection for sidebar


def get_user_input():
    horsepower = st.sidebar.number_input("Horsepower (No)", min_value =0, max_value=1000,step=1, value=300)
    torque = st.sidebar.number_input("Torque (No)", min_value=0, max_value=1500, step=1, value=400)

    make = st.sidebar.selectbox("Make", ['Aston Martin', 'Audi', 'BMW', 'Bentley', 'Ford', 'Mercedes-Benz', 'Nissan'])
    body_size = st.sidebar.selectbox("Body Size",['Large', 'Compact', 'Midsize'])
    body_style = st.sidebar.selectbox("Body Style",[
        'SUV','Sedan','Wagon',
        'Hatchback', 'Coupe', 'Convertible', 
        'Convertible SUV', 'Cargo Van','Pickup Truck',
        'Passenger Van', 'Cargo Minivan', 'Passenger Minivan'
    ])
    engine_aspiration = st.sidebar.selectbox("Engine Aspiration",['Twin-Turbo', 'Turbocharged','Electric Motor',
         'Twincharged', 'Naturally Aspirated', 'Supercharged'])
    drivetrain = st.sidebar.selectbox("Drivetrain",["4WD", "AWD", "FWD", "RWD"])
    transmission = st.sidebar.selectbox("Transmission", ["automatic", "manual"])

    user_data = {
        "Horsepower_No" : horsepower,
        "Torque_No" : torque,
        f"Make_{make}": 1,
        f"Body Size_{body_size}": 1,
        f"Body Style_{body_style}" : 1,
        f"Engine Aspiration_{engine_aspiration}": 1,
        f"Drivetrain_{drivetrain}": 1,
        f"Transmission_{transmission}": 1
    }
    return user_data

#top banner
image_banner = Image.open(os.path.join(Base_dir, "pic2.png"))
st.image(image_banner, width="stretch")

#centre title
st.markdown("<h1 stlye='text-align: center;'>Vehicle Price Predictions App</h1>", unsafe_allow_html=True)

#split layout into two columns
left_col, right_col = st.columns(2)

#left column: Feature Importance Interactive chart

with left_col:
    st.header("Feature Importance")

    #sort features importance DataFrame by "feature importance Score"
fi_sorted = final_fi.sort_values(by="Feature Importance score",  ascending=True)

#creating interactive bar chart with plotly
fig = px.bar(
    fi_sorted,
    x="Feature Importance score",
    y="Variable",
    orientation = "h",
    title = "Feature Importance ",
    labels= {"Feature Importance score": "Importance", "Variable": "Feature"},
    text="Feature Importance score",
    color_discrete_sequence = ["#e6b207"] #custom bar color
)
fig.update_layout(
    xaxis_title="Feature Importance Score",
    yaxis_title ="Variable",
    template= "plotly_white",
    height = 500
)

st.plotly_chart(fig, width="stretch")

#right column: Prediction Interface

with right_col:
    st.header("Predict Vehicle Price")

    #user input from sidebar

    user_data = get_user_input()

    #Transform the input the require formats

def prepare_input(data, feature_list):
    input_data = {feature: data.get(feature, 0) for feature in feature_list}
    return np.array([list(input_data.values())])


#feature list(same order in model training)

features = [
    'Horsepower_No', 'Torque_No', 'Make_Aston Martin', 'Make_Audi',
    'Make_BMW', 'Make_Bentley', 'Make_Ford', 'Make_Mercedes-Benz',
    'Make_Nissan', 'Body Size_Compact', 'Body Size_Large',
    'Body Size_Midsize', 'Body Style_Cargo Minivan', 'Body Style_Cargo Van',
    'Body Style_Convertible', 'Body Style_Convertible SUV',
    'Body Style_Coupe', 'Body Style_Hatchback',
    'Body Style_Passenger Minivan', 'Body Style_Passenger Van',
    'Body Style_Pickup Truck', 'Body Style_SUV', 'Body Style_Sedan',
    'Body Style_Wagon', 'Engine Aspiration_Electric Motor',
    'Engine Aspiration_Naturally Aspirated',
    'Engine Aspiration_Supercharged', 'Engine Aspiration_Turbocharged',
    'Engine Aspiration_Twin-Turbo', 'Engine Aspiration_Twincharged',
    'Drivetrain_4WD', 'Drivetrain_AWD', 'Drivetrain_FWD', 'Drivetrain_RWD',
    'Transmission_automatic', 'Transmission_manual'
]


#predict button

if st.button("Predict"):
    input_array = prepare_input(user_data, features)
    prediction = lm2.predict(input_array)
    st.subheader("Predicted Price")
    st.write(f"${prediction[0]:,.2f}")


#streamlit run Regr_model_cars.py

    

    

    


    

    