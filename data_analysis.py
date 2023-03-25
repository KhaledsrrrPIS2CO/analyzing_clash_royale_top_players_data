import mysql.connector
import pandas as pd
import numpy as np
from scipy import stats


def get_measures_central_tendency():
    # Connect to MySQL database
    cnx = mysql.connector.connect(user='root', password='2020$2020$ABC',
                                  host='127.0.0.1', database='clash_royale_database')

    # Execute SQL query and fetch data into a DataFrame
    query = "SELECT * FROM player_stats"
    df = pd.read_sql_query(query, cnx)

    # Perform data analysis operations on the DataFrame using Pandas and NumPy functions
    mean = round(np.mean(df['net_win_rate']),2)
    median = np.median(df['net_win_rate'])
    mode = stats.mode(df['net_win_rate'])[0][0]

    # Close MySQL connection
    cnx.close()

    return mean, median, mode


mean, median, mode = get_measures_central_tendency()
print(f"\nMean: {mean} \nMedian: {median} \nMode: {mode}")


def get_measures_variability():
    # Connect to MySQL database
    cnx = mysql.connector.connect(user='root', password='2020$2020$ABC',
                                  host='127.0.0.1', database='clash_royale_database')

    # Execute SQL query and fetch data into a DataFrame
    query = "SELECT net_win_rate FROM player_stats"
    df = pd.read_sql_query(query, cnx)

    # Calculate the range, variance, and standard deviation of net_win_rate
    range_val = np.max(df['net_win_rate']) - np.min(df['net_win_rate'])
    variance_val = round(np.var(df['net_win_rate']), 2)
    std_dev = round(np.std(df['net_win_rate']), 2)

    # Close MySQL connection
    cnx.close()

    # Return the results as a dictionary
    return {range_val, variance_val, std_dev}


range_val, variance_val, std_dev = get_measures_variability()
print(f"Range: {range_val} \nVariance: {variance_val} \nStd: {std_dev}")



