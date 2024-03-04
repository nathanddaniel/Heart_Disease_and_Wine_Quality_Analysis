import matplotlib.pyplot as plt
import pandas as pd

# Question 6
dataset = pd.read_csv('heart_disease_data.csv')

# Split the data into features and labels
data = dataset.iloc[:, :-1]
labels = dataset.iloc[:, -1]

# Creating a 13x13 grid of subplots with a figure size of 30x30 inches
fig, ax = plt.subplots(ncols=13, nrows=13, figsize=(30, 30))

# Create a scatter matrix of the data features and place it on the 13x13 grid of subplots
pd.plotting.scatter_matrix(data, ax=ax,  figsize=(30, 30))

fig.tight_layout()
plt.show()
