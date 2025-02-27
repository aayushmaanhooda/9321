"""
===============================
📦 FLASK SETUP & RUN INSTRUCTIONS
===============================

1️⃣ Install the required libraries:
-----------------------------------
pip install flask requests pandas

2️⃣ Run the Flask application:
------------------------------
python3 app.py or python3 <yourfilename>.py

3️⃣ Access the Endpoints:
-------------------------
- Fetch Raw JSON        → http://127.0.0.1:5000/fetch-json
- Get DataFrame as JSON → http://127.0.0.1:5000/get-df
"""

from flask import Flask, jsonify
import requests
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# 📡 Function to fetch JSON and convert to DataFrame
def fetch_json_to_df(url):
    response = requests.get(url)
    json_data = response.json()
    df = pd.DataFrame(json_data)
    return json_data, df


# 🌟 Root route returning "Welcome message"
@app.route('/', methods=['GET'])
def read_root():
     return {
         "message": "Welcome to Flask Application"
        }

# ✅ Route to fetch raw JSON
@app.route('/fetch-json', methods=['GET'])
def fetch_json():
    url = "https://raw.githubusercontent.com/joseluisq/json-datasets/master/json/operating-systems/macosx_releases.json"
    json_data, _ = fetch_json_to_df(url)
    return jsonify(json_data)

# 📊 Route to fetch DataFrame as JSON
@app.route('/get-df', methods=['GET'])
def get_df():
    url = "https://raw.githubusercontent.com/joseluisq/json-datasets/master/json/operating-systems/macosx_releases.json"
    _, df = fetch_json_to_df(url)
    return jsonify(df.to_dict(orient='records'))

# 🚀 Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
