from flask import Flask, jsonify, request
from flask_cors import CORS
from api import get_weather

app = Flask(__name__)

CORS(app)


@app.route("/api/weather")
def weather_api():
    city = request.args.get("city", "Melbourne")
    try:
        return jsonify(get_weather(city))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000)
