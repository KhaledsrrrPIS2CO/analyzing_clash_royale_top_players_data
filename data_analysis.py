import mysql.connector
import pandas as pd
import numpy as np
from scipy import stats


def connect_to_database():
    """
    This function connects to a MySQL database, executes a query to retrieve data from the 'player_stats' table,
    and returns the data as a DataFrame.
    """

    # Connect to MySQL database
    cnx = mysql.connector.connect(user='root', password='2020$2020$ABC', host='127.0.0.1',
                                   database='clash_royale_database')

    # Execute SQL query and fetch data into a DataFrame
    query = "SELECT * FROM player_stats"
    df = pd.read_sql_query(query, cnx)

    # Close MySQL connection
    cnx.close()

    return df


def get_measures_central_tendency():
    """
    This function performs some central tendency measures (mean, median, mode) on the 'net_win_rate' column using NumPy
    and Pandas functions, and returns the results as a tuple.
    """

    # Fetch data into a DataFrame
    df = connect_to_database()

    # Perform data analysis operations on the DataFrame using Pandas and NumPy functions
    mean = round(np.mean(df['net_win_rate']), 2)
    median = np.median(df['net_win_rate'])
    mode = stats.mode(df['net_win_rate'])[0][0]

    return mean, median, mode


# Call the function and print the results
mean, median, mode = get_measures_central_tendency()
print(f"\nMean: {mean} \nMedian: {median} \nMode: {mode}")


def get_measures_variability():
    """
    This function performs some variability measures (range, variance, standard deviation) on the 'net_win_rate'
    column using NumPy and Pandas functions, and returns the results as a dictionary.
    """

    # Fetch data into a DataFrame
    df = connect_to_database()

    # Calculate the range, variance, and standard deviation of net_win_rate
    range_val = np.max(df['net_win_rate']) - np.min(df['net_win_rate'])
    variance_val = round(np.var(df['net_win_rate']), 2)
    std_dev = round(np.std(df['net_win_rate']), 2)

    # Return the results as a dictionary
    return {range_val, variance_val, std_dev}


# Call the function and print the results
range_val, variance_val, std_dev = get_measures_variability()
print(f"\nRange: {range_val} \nVariance: {variance_val} \nStandard Deviation: {std_dev}")
