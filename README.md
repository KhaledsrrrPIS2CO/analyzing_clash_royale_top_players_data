The code is not complete (still under development) 

First of all I am a clash royale player :)
My tag: #QCR929GGQ

Overview
This Python project is has three modules
first to collect data from clash royale API
Second to analysis the collected data
Third to simulate a game between two knwown players

More details one the second moduel: the code retrieves data from a MySQL database and performs statistical analysis on the 'net_win_rate' column of the 'player_stats' table. It calculates measures of central tendency (mean, median, mode), measures of variability (range, variance, standard deviation), and the 68-95-99 rule. It also generates a probability density function plot for the net_win_rate column

Functions
connect_to_database()
This function connects to the MySQL database and retrieves data from the 'player_stats' table. It returns the data as a Pandas DataFrame.

get_measures_central_tendency()
This function performs measures of central tendency (mean, median, mode) on the 'net_win_rate' column using NumPy and Pandas functions. It returns the results as a tuple.

get_measures_variability()
This function performs measures of variability (range, variance, standard deviation) on the 'net_win_rate' column using NumPy and Pandas functions. It returns the results as a dictionary.

get_68_95_99_rule()
This function calculates the 68-95-99 rule for the 'net_win_rate' column using NumPy. It returns the result as a formatted string.

plot_probability_density_function()
This function generates a probability density function plot for the 'net_win_rate' column using Matplotlib.

plot_net_win_rate_histogram()
generates a histogram of net win rate data fetched from a database using Matplotlib, providing insights into the data's distribution and identifying any patterns or trends





