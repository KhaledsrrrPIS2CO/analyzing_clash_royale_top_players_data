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
mean = np.mean(df['net_win_rate'])
std_dev = np.std(df['net_win_rate'])
# Calculate the 90th percentile of net_win_rate
top_10_percentile = df['net_win_rate'].quantile(0.9)
# Get the top 10% of players based on net_win_rate
top_players = df[df['net_win_rate'] >= top_10_percentile]


print(mean)
print(std_dev)
print(top_players)

# Close MySQL connection
cnx.close()


exit()


