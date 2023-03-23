import mysql.connector
import pandas as pd
import numpy as np

# Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='2020$2020$ABC',
                              host='127.0.0.1', database='clash_royale_database')


# Execute SQL query and fetch data into a DataFrame
query = "SELECT * FROM player_stats"
df = pd.read_sql_query(query, cnx)

# Perform data analysis operations on the DataFrame using Pandas and NumPy functions
mean = np.mean(df['column_name'])
std_dev = np.std(df['column_name'])

# Close MySQL connection
cnx.close()

exit()
