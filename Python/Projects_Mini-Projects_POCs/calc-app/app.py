from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask app
app = Flask(__name__)

# Configure logging
handler = RotatingFileHandler("calculator.log", maxBytes=2000000, backupCount=5)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Flask Calculator API!",
        "endpoints": {
            "/calculate": "POST - Provide JSON with num1, num2, and operation (+, -, *, /)"
        }
    })


@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()

        if not data:
            app.logger.warning("No input data provided")
            return jsonify({"error": "No input data provided"}), 400

        num1 = data.get("num1")
        num2 = data.get("num2")
        operation = data.get("operation")

        # Validate inputs
        if num1 is None or num2 is None or operation is None:
            app.logger.warning("Invalid input data: %s", data)
            return jsonify({"error": "num1, num2, and operation are required"}), 400

        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            app.logger.warning("Non-numeric input received: num1=%s, num2=%s", num1, num2)
            return jsonify({"error": "num1 and num2 must be numeric"}), 400

        # Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                app.logger.error("Division by zero attempted")
                return jsonify({"error": "Division by zero is not allowed"}), 400
            result = num1 / num2
        else:
            app.logger.warning("Unsupported operation requested: %s", operation)
            return jsonify({"error": "Unsupported operation. Use +, -, *, /"}), 400

        app.logger.info("Calculation performed: %s %s %s = %s", num1, operation, num2, result)
        return jsonify({"num1": num1, "num2": num2, "operation": operation, "result": result})

    except Exception as e:
        app.logger.exception("Unexpected error during calculation")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
