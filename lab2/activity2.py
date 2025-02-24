# Importing necessary libraries
import pandas as pd  # For data manipulation and handling CSV files
import sqlite3       # For creating and interacting with SQLite databases

# ---------------------------------------------
# FUNCTION 1: READ CSV FILE
# ---------------------------------------------

def read_csv(csv_file):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    csv_file (str): Path to the CSV file.

    Returns:
    DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    # Using pandas' read_csv() to read the CSV file into a DataFrame
    return pd.read_csv(csv_file)

# ---------------------------------------------
# FUNCTION 2: CREATE SQLITE DATABASE AND STORE DATA
# ---------------------------------------------

def create_db(dataframe, file, name):
    """
    Creates an SQLite database and stores the DataFrame as a table.

    Parameters:
    dataframe (DataFrame): The pandas DataFrame to store in the database.
    file (str): The SQLite database file name.
    name (str): The table name where data will be stored.
    """
    # 1️⃣ Establishing a connection to the SQLite database.
    # If the file does not exist, SQLite creates a new one.
    connection = sqlite3.connect(file)

    # 2️⃣ Writing DataFrame into SQLite database as a table.
    # - 'name' → name of the table in the database.
    # - 'con' → database connection.
    # - 'if_exists="replace"' → replaces table if it already exists.
    # - 'index=False' → excludes DataFrame's index from being stored as a separate column.
    dataframe.to_sql(name, con=connection, if_exists='replace', index=False)

    # 3️⃣ Closing the connection after the operation.
    connection.close()

# ---------------------------------------------
# FUNCTION 3: READ DATA FROM SQLITE DATABASE
# ---------------------------------------------

def read_db(file, name):
    """
    Reads data from an SQLite database table into a pandas DataFrame.

    Parameters:
    file (str): The SQLite database file name.
    name (str): The table name to read data from.

    Returns:
    DataFrame: The queried data as a pandas DataFrame.
    """
    # 1️⃣ Connecting to the SQLite database
    connection = sqlite3.connect(file)

    # 2️⃣ Writing SQL query to fetch all data from the specified table
    query = f"SELECT * FROM {name}"

    # 3️⃣ Using pandas' read_sql_query() to execute the query and load data into a DataFrame
    df = pd.read_sql_query(query, connection)

    # 4️⃣ Closing the connection after fetching data
    # it would still work if you dont close the connection but it is good practise to close after you are done performing your task 
    connection.close()

    return df  # Returning the DataFrame containing queried data

# ---------------------------------------------
# MAIN BLOCK: EXECUTION STARTS HERE
# ---------------------------------------------

if __name__ == '__main__':
    # File paths and table name
    csv_file = 'data.csv'    # 📂 Path to the source CSV file
    file = 'database.db'     # 🗄️ Name of the SQLite database file
    table_name = "Students"  # 📊 Table name in the database

    # ----------------------------
    # STEP 1: READ CSV FILE
    # ----------------------------
    # Reads the CSV file into a pandas DataFrame
    dataframe = read_csv(csv_file)

    # ----------------------------
    # STEP 2: CREATE DATABASE AND STORE DATA
    # ----------------------------
    print("Creating Database")
    # Creates the SQLite database and stores the DataFrame as a table
    create_db(dataframe, file, table_name)

    # ----------------------------
    # STEP 3: QUERY DATABASE
    # ----------------------------
    print("Querying the database")
    # Reads data back from the SQLite database into a new DataFrame
    queried_df = read_db(file, table_name)

    # ----------------------------
    # STEP 4: CONFIGURE PANDAS DISPLAY SETTINGS
    # ----------------------------
    # Setting pandas options for better DataFrame display in the terminal
    pd.set_option('display.width', 1000)      # Set terminal width for DataFrame display
    pd.options.display.max_colwidth = 3       # Truncate long text in cells after 3 characters
    pd.set_option('display.max_columns', 7)   # Display a maximum of 7 columns

    # ----------------------------
    # STEP 5: DISPLAY DATAFRAME
    # ----------------------------
    # Prints the first 10 rows of the queried DataFrame
    print(queried_df.head(10))
