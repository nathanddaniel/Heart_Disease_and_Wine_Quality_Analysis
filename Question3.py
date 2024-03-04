import matplotlib.pyplot as plt
import pandas as pd

# Question 3

# This will read the dataset in the file into a Pandas DataFrame
dataset = pd.read_csv('heart_disease_data.csv')

# Split the data into features and labels for further analysis
# The features are all columns except for the last one, thus :-1
# The labels is just the last column, hence -1
data = dataset.iloc[:, :-1]
labels = dataset.iloc[:, -1]

# Creates a 4 x 4 grid of plots and set the figure size to 20 by 10
# 'fig' is a figure object which is the container for all the plots
# 'ax' is an array of Axes objects which are individual plots in the grid
# fig,ax unpacks the tuple (ie the immutable array) returned into the figure object and array of axes objects

fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20, 10))

# Matplotlib has a '.hist()' method which creates a histogram plot
# However, it only accepts 1 'ax' object at a time, thus to create 13 histogram plots, we need a for loop
# This for loop should iterate from 0 to 12

for i in range(13):
    ax.flatten()[i].hist(data.iloc[:, i])
    ax.flatten()[i].set_title(data.columns[i], fontsize=15)

# Adjust the layout so there is no overlap of subplots
fig.tight_layout()

# Display the figure with all the subplots
plt.show()
