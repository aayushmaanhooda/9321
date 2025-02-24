# 📚 Importing necessary libraries
import requests  # For sending HTTP requests and fetching JSON data
import pandas as pd  # For creating and manipulating DataFrames

# ---------------------------------------------
# FUNCTION 1: FETCH JSON FROM A URL
# ---------------------------------------------

def get_json(url):
    """
    Sends a GET request to the provided URL and returns the JSON data.

    Parameters:
    url (str): The URL to fetch JSON data from.

    Returns:
    dict or list: The parsed JSON data.
    """
    # 1️⃣ Sending a GET request to the provided URL
    response = requests.get(url=url)

    # 2️⃣ Parsing the response as JSON
    # because if you print resposne you will just get the status code so we need to parse it to see actual data 
    data = response.json()

    return data  # Returning the JSON data

# ---------------------------------------------
# FUNCTION 2: CONVERT JSON TO PANDAS DATAFRAME
# ---------------------------------------------

def create_df(json_object):
    """
    Converts a JSON object into a pandas DataFrame.

    Parameters:
    json_obj (list or dict): The JSON data to convert.

    Returns:
    DataFrame: The pandas DataFrame created from the JSON data.
    """
    # Using from_records() to convert list of dictionaries into a DataFrame
    # pd.DataFrame.from_records() is ideal when you have record-like data (e.g., list of dicts)
    # it would also work if you just did pd.DataFrame(josn_object)
    # but from_records has more advantages refer to this docs to read more about it 
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html
    return pd.DataFrame.from_records(json_object)
    

# ---------------------------------------------
# MAIN BLOCK: EXECUTION STARTS HERE
# ---------------------------------------------

if __name__ == '__main__':
    # ✅ URL containing JSON data about macOS releases
    url = "https://raw.githubusercontent.com/joseluisq/json-datasets/master/json/operating-systems/macosx_releases.json"

    # STEP 1️⃣: Fetch JSON from the URL
    print("📡 Fetching the JSON data from the URL")
    json_object = get_json(url)

    # STEP 2️⃣: Convert JSON to pandas DataFrame
    print("📊 Creating DataFrame from JSON")
    df = create_df(json_object)

    # STEP 3️⃣: Display the DataFrame
    print(df)
