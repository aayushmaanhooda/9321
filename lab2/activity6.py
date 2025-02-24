"""
===========================================
📦 FASTAPI SETUP & RUN INSTRUCTIONS
===========================================

1️⃣ Install the required libraries:
-----------------------------------
pip install fastapi uvicorn requests pandas

2️⃣ Run the FastAPI application:
--------------------------------
# Option 1: From code (activity6 is your file name)
python3 activity6.py

# Option 2: From terminal (recommended)
uvicorn activity6:app --reload

3️⃣ Access the Endpoints:
-------------------------
- Fetch Raw JSON        → http://127.0.0.1:8000/fetch-json
- Get DataFrame as JSON → http://127.0.0.1:8000/get-df

4️⃣ API Documentation (Swagger UI):
-----------------------------------
- Swagger UI  → http://127.0.0.1:8000/docs ✅
- ReDoc       → http://127.0.0.1:8000/redoc ✅

💡 Cool feature in FastAPI is it automatically generates interactive API docs at **/docs** (Swagger UI) and **/redoc** (ReDoc) without additional setup.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# 📡 Function to fetch JSON and convert to DataFrame
def fetch_json_to_df(url):
    response = requests.get(url)
    json_data = response.json()
    df = pd.DataFrame(json_data)
    return json_data, df

# ✅ Route to fetch raw JSON
@app.get('/fetch-json')
def fetch_json():
    """
    Fetches raw JSON from the external URL.

    ➤ Access this endpoint at:
      http://127.0.0.1:8000/fetch-json
    """
    url = "https://raw.githubusercontent.com/joseluisq/json-datasets/master/json/operating-systems/macosx_releases.json"
    json_data, _ = fetch_json_to_df(url)
    return JSONResponse(content=json_data)

# 📊 Route to fetch DataFrame as JSON
@app.get('/get-df')
def get_df():
    """
    Fetches JSON and returns it as a structured DataFrame.

    ➤ Access this endpoint at:
      http://127.0.0.1:8000/get-df
    """
    url = "https://raw.githubusercontent.com/joseluisq/json-datasets/master/json/operating-systems/macosx_releases.json"
    _, df = fetch_json_to_df(url)
    return JSONResponse(content=df.to_dict(orient='records'))

# 🚀 Run the FastAPI app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("activity6:app", host="127.0.0.1", port=8000, reload=True)
