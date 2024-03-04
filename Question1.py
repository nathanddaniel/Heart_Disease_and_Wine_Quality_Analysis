import matplotlib.pyplot as plt
import pandas as pd

# Question 1

dataset = pd.read_csv('heart_disease_data.csv')

# Split the data into features and labels
data = dataset.iloc[:, :-1]  # All columns except the last one
labels = dataset.iloc[:, -1]  # Only the last column

# The line below creates a plot with a 4 x 4 grid and set the figure size to 20 by 10
# fig,ax unpacks the tuple (ie the immutable array) returned into the figure object and array of axes objects

fig, ax = plt.subplots(ncols=4, nrows=4, figsize=(20, 10))

# We created 'ax' and 'figs' objects, so now we can create the histogram plots inside those objects
# We should apply the '.hist' method to the data

data.hist(ax=ax.flatten()[:13])

# The following code will make the layout of the plot tight and render the plot
fig.tight_layout()
plt.show()