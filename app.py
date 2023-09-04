from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def home():
    response_data = {"server": "running"}
    return jsonify(response_data)
