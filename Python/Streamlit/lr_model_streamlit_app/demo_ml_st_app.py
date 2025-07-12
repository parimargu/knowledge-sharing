import streamlit as st
import pandas as pd
import joblib


# Load your trained model
lr_model_path = "/home/datamaking/work/code/workarea/weekly_online_meeting/1-linear-regression/model/linear_regression_model.pkl"
loaded_model = joblib.load(lr_model_path)

# prediction function (model prediction)
def predict_price(input_df):
    print("Inside of predict_price function")
    return loaded_model.predict(input_df)

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

# Create one-hot encoding for location
location_data = {f"location_{loc}": [True if loc == location else False] for loc in locations}

# Combine into one DataFrame
input_data = {
    'total_sqft': [total_sqft],
    'bath': [bath],
    'balcony': [balcony],
    'bhk': [bhk],
}
input_df = pd.DataFrame(input_data)
input_df = pd.concat([input_df, pd.DataFrame(location_data)], axis=1)

# Predict button
if st.button("Predict Price"):
    result = predict_price(input_df)
    st.success(f"🏡 Estimated House Price: ₹ {int(result[0]):,}")
