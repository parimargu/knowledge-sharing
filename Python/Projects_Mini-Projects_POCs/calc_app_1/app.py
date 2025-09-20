# Vibe Coding

from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler

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


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = request.form.get("num1")
            num2 = request.form.get("num2")
            operation = request.form.get("operation")

            # Validate inputs
            if not num1 or not num2 or not operation:
                error = "All fields are required."
                app.logger.warning("Missing input fields")
                return render_template("index.html", result=result, error=error)

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                error = "Inputs must be numeric."
                app.logger.warning("Non-numeric input received: num1=%s, num2=%s", num1, num2)
                return render_template("index.html", result=result, error=error)

            # Perform operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    error = "Division by zero is not allowed."
                    app.logger.error("Division by zero attempted")
                    return render_template("index.html", result=result, error=error)
                result = num1 / num2
            else:
                error = "Unsupported operation."
                app.logger.warning("Unsupported operation: %s", operation)
                return render_template("index.html", result=result, error=error)

            app.logger.info("Calculation: %s %s %s = %s", num1, operation, num2, result)

        except Exception as e:
            error = f"Unexpected error: {str(e)}"
            app.logger.exception("Unexpected error occurred")

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
