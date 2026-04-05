from flask import Flask, request, jsonify

app = Flask(__name__)

# =========================
# HEALTH CHECK
# =========================
@app.route("/")
def home():
    return jsonify({
        "message": "🧮 Math API is running",
        "endpoints": [
            "/add",
            "/subtract",
            "/multiply",
            "/divide"
        ]
    })


# =========================
# HELP FUNCTION
# =========================
def get_numbers():
    data = request.get_json()

    if not data:
        return None, None, "❌ JSON body required"

    try:
        num1 = float(data.get("num1"))
        num2 = float(data.get("num2"))
        return num1, num2, None
    except:
        return None, None, "❌ Invalid input"


# =========================
# ADD
# =========================
@app.route("/add", methods=["POST"])
def add():
    num1, num2, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "operation": "addition",
        "num1": num1,
        "num2": num2,
        "result": num1 + num2
    })


# =========================
# SUBTRACT
# =========================
@app.route("/subtract", methods=["POST"])
def subtract():
    num1, num2, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "operation": "subtraction",
        "result": num1 - num2
    })


# =========================
# MULTIPLY
# =========================
@app.route("/multiply", methods=["POST"])
def multiply():
    num1, num2, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "operation": "multiplication",
        "result": num1 * num2
    })


# =========================
# DIVIDE
# =========================
@app.route("/divide", methods=["POST"])
def divide():
    num1, num2, error = get_numbers()
    if error:
        return jsonify({"error": error}), 400

    if num2 == 0:
        return jsonify({"error": "❌ Cannot divide by zero"}), 400

    return jsonify({
        "operation": "division",
        "result": num1 / num2
    })


# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)