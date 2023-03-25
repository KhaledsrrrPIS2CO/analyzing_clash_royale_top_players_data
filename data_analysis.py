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
    mean = np.mean(df['net_win_rate'])
    median = np.median(df['net_win_rate'])
    mode = stats.mode(df['net_win_rate'])[0][0]

    # Close MySQL connection
    cnx.close()

    return mean, median, mode


measures_central_tendency = get_measures_central_tendency()
print(measures_central_tendency)
