from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model_path = "/home/datamaking/work/code/workarea/weekly_online_meeting/1-linear-regression/model/linear_regression_model.pkl"
model = joblib.load(model_path)

# Define non-location features to extract locations from model input features
non_location_features = ['total_sqft', 'bath', 'balcony', 'bhk']
locations = [
    feature.replace("location_", "")
    for feature in model.feature_names_in_
    if feature not in non_location_features
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input
        data = request.get_json()
        print("Printing the value of data: ")
        print(data)

        # Extract required fields
        total_sqft = data.get("total_sqft")
        bath = data.get("bath")
        balcony = data.get("balcony")
        bhk = data.get("bhk")
        location = data.get("location")

        # Validate input
        if not all([total_sqft, bath, balcony, bhk, location]):
            return jsonify({"error": "Missing required fields"}), 400

        # Build feature dict
        input_data = {
            'total_sqft': [total_sqft],
            'bath': [bath],
            'balcony': [balcony],
            'bhk': [bhk],
        }

        # One-hot encode location
        location_data = {f"location_{loc}": [1 if loc == location else 0] for loc in locations}

        # Create input DataFrame
        input_df = pd.DataFrame(input_data)
        input_df = pd.concat([input_df, pd.DataFrame(location_data)], axis=1)

        print("Printing value of input_df: ")
        print(input_df.head())

        # Predict
        prediction = model.predict(input_df)
        predicted_price = float(prediction[0])

        return jsonify({"predicted_price": round(predicted_price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
