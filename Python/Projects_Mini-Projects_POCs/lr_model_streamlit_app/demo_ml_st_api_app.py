import streamlit as st
import pandas as pd
import requests

import joblib


# Load your trained model
lr_model_path = "/home/datamaking/work/code/workarea/weekly_online_meeting/1-linear-regression/model/linear_regression_model.pkl"
loaded_model = joblib.load(lr_model_path)

# prediction function (model prediction)
def predict_price(input_df):
    print("Inside of predict_price function")
    print("Using prediction api endpoint")
    url = "http://127.0.0.1:5000/predict"  # Your Flask API endpoint
    payload = input_df.to_dict(orient='records')[0]
    print("Printing value of payload: ")
    print(payload)
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return [response.json()["predicted_price"]]
    else:
        st.error("Prediction failed: " + response.json().get("error", "Unknown error"))
        return [0]

# List of locations
non_location_features = ['total_sqft', 'bath', 'balcony', 'bhk']

# Extract only location columns from the model's feature list
locations = [
    feature.replace("location_", "")  # Clean the prefix for display
    for feature in loaded_model.feature_names_in_
    if feature not in non_location_features
]

# Streamlit UI
st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Prediction")

st.markdown("Fill in the details below to estimate the house price.")

# Input fields
total_sqft = st.number_input("Total Square Feet", min_value=300.0, max_value=10000.0, value=1000.0)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
balcony = st.number_input("Number of Balconies", min_value=0, max_value=5, value=1)
bhk = st.number_input("BHK (Bedrooms)", min_value=1, max_value=10, value=2)
location = st.selectbox("Select Location", locations)

# Combine into one DataFrame
input_data = {
    'total_sqft': [total_sqft],
    'bath': [bath],
    'balcony': [balcony],
    'bhk': [bhk],
    'location': [location]
}
input_df = pd.DataFrame(input_data)

# Predict button
if st.button("Predict Price"):
    result = predict_price(input_df)
    st.success(f"🏡 Estimated House Price: ₹ {int(result[0]):,}")
