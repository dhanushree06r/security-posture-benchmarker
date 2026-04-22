from flask import Flask, request, jsonify
from services.groq_client import call_groq

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        user_input = data.get("input")

        if not user_input:
            return jsonify({"error": "Input is required"}), 400

        result = call_groq(user_input)

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)