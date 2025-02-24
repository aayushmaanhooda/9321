# 📚 Importing the necessary libraries
import pandas as pd  # For data manipulation and handling CSV files
from pymongo import MongoClient  # For connecting to MongoDB

# ---------------------------------------------
# FUNCTION 1: READ CSV FILE
# ---------------------------------------------
# https://www.mongodb.com/docs/manual/installation/
def read_csv(csv_file):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    csv_file (str): The path to the CSV file.

    Returns:
    DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    # ✅ Using pandas' read_csv() to load the CSV file into a DataFrame
    return pd.read_csv(csv_file)

# ---------------------------------------------
# FUNCTION 2: CREATE MONGODB DATABASE & INSERT DATA
# ---------------------------------------------

def create_mongo(df):
    """
    Creates a MongoDB database and inserts the DataFrame data into a collection.

    Parameters:
    df (DataFrame): The pandas DataFrame to store in MongoDB.
    """
    # 1️⃣ Connecting to MongoDB server running locally on default port (27017)
    client = MongoClient("mongodb://localhost:27017/")

    # 2️⃣ Accessing/Creating the database named 'comp9321'
    db = client['comp9321']

    # 3️⃣ Accessing/Creating the collection named 'Demographic_Statistics'
    collection = db['Demographic_Statistics']

    # 4️⃣ Deleting existing data in the collection to avoid duplicates
    collection.delete_many({})

    # 5️⃣ Inserting DataFrame into MongoDB
    # - df.to_dict('records') converts DataFrame rows into a list of dictionaries
    collection.insert_many(df.to_dict('records'))

    print("✅ Database and collection created successfully!")

    # 6️⃣ Closing the MongoDB connection
    # it would still work if you dont close the connection but it is good practise to close after you are done performing your task 
    client.close()

# ---------------------------------------------
# FUNCTION 3: READ DATA FROM MONGODB TO PANDAS DATAFRAME
# ---------------------------------------------

def read_mongo():
    """
    Reads data from MongoDB and converts it into a pandas DataFrame.
    """
    # 1️⃣ Connecting to MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # 2️⃣ Accessing the database and collection
    db = client['comp9321']
    collection = db['Demographic_Statistics']

    # 3️⃣ Reading all documents from the collection
    print("✅ Reading data from MongoDB to pandas DataFrame")
    cursor = collection.find()

    # 4️⃣ Converting MongoDB cursor to a list, then into a pandas DataFrame
    new_df = pd.DataFrame(list(cursor))

    # 5️⃣ Displaying the DataFrame loaded from MongoDB
    print("📊 Data Loaded from MongoDB:")
    print(new_df)

    # 6️⃣ Closing the MongoDB connection
    client.close()

# ---------------------------------------------
# MAIN BLOCK: EXECUTION STARTS HERE
# ---------------------------------------------

if __name__ == '__main__':
    # -----------------------------------------------------------
    # STEP 1️⃣: Read CSV file into pandas DataFrame
    # -----------------------------------------------------------
    '''
    Loading the CSV file into a DataFrame
    '''
    csv_file = 'data.csv'  # 📂 Path to the CSV file
    df = read_csv(csv_file)

    # -----------------------------------------------------------
    # STEP 2️⃣: Insert Data into MongoDB
    # -----------------------------------------------------------
    '''
    Creating MongoDB database and collection, then inserting the CSV data
    '''
    create_mongo(df)

    # -----------------------------------------------------------
    # STEP 3️⃣: Read Data from MongoDB
    # -----------------------------------------------------------
    '''
    Fetching the inserted data from MongoDB and displaying it as a DataFrame
    '''
    read_mongo()
