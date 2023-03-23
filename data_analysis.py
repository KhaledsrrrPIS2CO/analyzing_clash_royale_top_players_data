import sqlalchemy as db
import pandas as pd
import numpy as np

# Connect to MySQL database
engine = db.create_engine('mysql+mysqlconnector://root:2020$2020$ABC@127.0.0.1/clash_royale_database')
connection = engine.connect()

# Execute SQL query and fetch data into a DataFrame
query = "SELECT * FROM player_stats"
df = pd.read_sql_query(query, connection)

# Perform data analysis operations on the DataFrame using Pandas and NumPy functions
mean = np.mean(df['net_win_rate'])
std_dev = np.std(df['net_win_rate'])

print(mean)
print(std_dev)

# Close MySQL connection
connection.close()
engine.dispose()

exit()
