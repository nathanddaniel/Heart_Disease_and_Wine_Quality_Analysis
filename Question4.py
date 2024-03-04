import matplotlib.pyplot as plt
import pandas as pd

# Question 4

# Read the dataset
dataset = pd.read_csv('heart_disease_data.csv')

# Split the dataset into features and labels
data = dataset.iloc[:, :-1]  # Assuming the last column is the label
labels = dataset.iloc[:, -1]

# Create a figure with a 4x4 grid of subplots
fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(20, 10))

# Create the density plots for each feature
# Assuming there are 13 features, we use the first 13 axes for plotting
data.plot(ax=ax.flatten()[:13], kind='density', subplots=True, sharex=False)

# Adjust the layout and display the plot
fig.tight_layout()
plt.show()


