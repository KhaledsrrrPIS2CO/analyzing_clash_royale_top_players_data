import mysql.connector
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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
    max_val = np.max(df['net_win_rate'])
    min_val = np.min(df['net_win_rate'])

    return mean, median, mode, max_val, min_val


# Call the get_measures_central_tendency function and print the results
mean, median, mode, max_val, min_val = get_measures_central_tendency()
print("Measures of central tendency:")
print(f"\nMean: {mean} \nMedian: {median} \nMode: {mode}\nMax: {max_val}\nMin: {min_val}")


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


# Call the get_measures_variability function and print the results
range_val, variance_val, std_dev = get_measures_variability()
print("\nMeasures of variability:")
print(f"Range: {range_val} \nVariance: {variance_val} \nStandard Deviation: {std_dev}\n")


def get_68_95_99_rule():
    """
    This function calculates the 68-95-99 rule for the 'net_win_rate' column using NumPy and returns the result as a
    formatted string.
    """

    # Fetch data into a DataFrame
    df = connect_to_database()

    # Calculate mean and standard deviation
    mean = np.mean(df['net_win_rate'])
    std_dev = np.std(df['net_win_rate'])

    # Calculate the 68-95-99 rule
    rule_68 = (mean - std_dev, mean + std_dev)
    rule_95 = (mean - 2 * std_dev, mean + 2 * std_dev)
    rule_99 = (mean - 3 * std_dev, mean + 3 * std_dev)

    # Format the result as a string
    result = f"The 68-95-99 rule for the net_win_rate is:\n68% of the data lies between {rule_68[0]:.2f} and" \
             f" {rule_68[1]:.2f}\n95% of the data lies between {rule_95[0]:.2f} and" \
             f" {rule_95[1]:.2f}\n99% of the data lies between {rule_99[0]:.2f} and {rule_99[1]:.2f}"

    return result


# Call the  get_68_95_99_rule function and print the results
six_nine_nine_rule = get_68_95_99_rule()
print(six_nine_nine_rule)


def plot_net_win_rate_distribution():
    # Fetch data into a DataFrame
    df = connect_to_database()

    # Calculate the mean and standard deviation of the net_win_rate
    mu, sigma = np.mean(df['net_win_rate']), np.std(df['net_win_rate'])

    # Create an array of values that represent the range of net_win_rate values
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

    # Calculate the corresponding probability density function (PDF) for each value in the range
    pdf = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))

    # Plot the PDF using matplotlib
    plt.plot(x, pdf)
    plt.title("Normal Distribution of Net Win Rate")
    plt.xlabel("Net Win Rate")
    plt.ylabel("Probability Density")
    plt.show()


plot_net_win_rate_distribution()
