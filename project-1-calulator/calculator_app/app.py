from flask import Flask, render_template, request, jsonify
from backend.calculator_logic import calculate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def perform_calculation():
    data = request.json
    try:
        a = float(data.get("a", 0))
        b = float(data.get("b", 0))
        op = data.get("op", "+")
        
        result = calculate(a, op, b)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
