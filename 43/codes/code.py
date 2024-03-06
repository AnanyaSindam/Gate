import numpy as np
import matplotlib.pyplot as plt

# Read data from file, skipping the first row
data = np.loadtxt("data.dat", skiprows=1)

# Extracting t and y(t) values
t_values = data[:, 0]
y_values = data[:, 1]

# Plotting
plt.plot(t_values, y_values)
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.grid(True)

# Set y-axis limits
plt.ylim(-15, 1)

# Add horizontal line at y=0.33
plt.axhline(y=0.33, color='r', linestyle='--')

# Label y=0.33 on the y-axis
plt.text(plt.xlim()[0], 0.33, '0.33', va='center', ha='right', color='r')
plt.savefig('plot.png')
plt.show()

