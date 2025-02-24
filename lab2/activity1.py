# 📚 Importing the pandas library for data manipulation and analysis
import pandas as pd

# ---------------------------------------------
# FUNCTION 1: READ CSV FILE
# ---------------------------------------------

def read_csv(csv_file):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    csv_file (str): The path to the CSV file.

    Returns:
    DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    # ✅ Using pandas' read_csv() to read the CSV file into a DataFrame
    return pd.read_csv(csv_file)

# ---------------------------------------------
# FUNCTION 2: PRINT DATAFRAME COLUMNS
# ---------------------------------------------

def print_columns(df):
    """
    Joins and returns all column names from the DataFrame as a single string.

    Parameters:
    df (DataFrame): The pandas DataFrame.

    Returns:
    str: A comma-separated string of column names.
    """
    # 📊 Getting column names from DataFrame using df.columns
    # 🧵 Joining column names with commas to create a single string
    columns = ",".join(df.columns)
    
    # 🖨️ Printing the column names
    print(columns)

    # 🔄 Returning the column names (optional)
    return columns

# ---------------------------------------------
# FUNCTION 3: PRINT DATAFRAME ROWS
# ---------------------------------------------

def print_rows(df):
    """
    Prints each row of the DataFrame as a list.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    """
    # 🔄 Converting DataFrame rows to a list of lists using values.tolist()
    for row in df.values.tolist():
        # 🖨️ Printing each row as a list
        print(row)

# ---------------------------------------------
# FUNCTION 4: WRITE DATAFRAME TO A NEW CSV FILE
# ---------------------------------------------

def write_in_csv(df, file):
    """
    Writes the DataFrame to a CSV file.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    file (str): The path to the output CSV file.
    """
    # 💾 Writing DataFrame to a CSV file
    # 🏷️ index=False → Excludes DataFrame's index from being stored in CSV
    df.to_csv(file, index=False)

# ---------------------------------------------
# MAIN BLOCK: EXECUTION STARTS HERE
# ---------------------------------------------

if __name__ == '__main__':
    # -----------------------------------------------------------
    # STEP 1️⃣: Download or use an existing CSV file
    # -----------------------------------------------------------
    '''
    The path to the CSV file that will be read
    '''
    csv_file = 'data.csv'  # 📂 Path to the source CSV file
    
    # -----------------------------------------------------------
    # STEP 2️⃣: Read CSV file into a DataFrame
    # -----------------------------------------------------------
    '''
    Reading the CSV file into a DataFrame and storing it as the variable "df"
    '''
    df = read_csv(csv_file)

    # -----------------------------------------------------------
    # STEP 3️⃣: Print DataFrame Columns
    # -----------------------------------------------------------
    '''
    Printing all the column names from the DataFrame
    '''
    print("Printing columns")
    print_columns(df)

    # -----------------------------------------------------------
    # STEP 4️⃣: Print DataFrame Rows
    # -----------------------------------------------------------
    '''
    Printing all rows from the DataFrame as lists
    '''
    print("Printing rows")
    print_rows(df)

    # -----------------------------------------------------------
    # STEP 5️⃣: Use to_string() to Print Full DataFrame
    # -----------------------------------------------------------
    '''
    Normally, printing df may truncate the DataFrame (especially if large).
    Using df.to_string() gives a complete, untruncated view of the DataFrame.
    '''
    print("Printing full DataFrame with df.to_string()")
    # print(df.to_string())  # 🖨️ Full DataFrame with no truncation

    # -----------------------------------------------------------
    # STEP 6️⃣: Save DataFrame as a New CSV File
    # -----------------------------------------------------------
    '''
    Writing the DataFrame to a new CSV file named 'new_data.csv'
    '''
    print("Writing the DataFrame as a CSV file")
    write_in_csv(df, "new_data.csv")
