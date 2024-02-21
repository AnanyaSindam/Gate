import numpy as np
import matplotlib.pyplot as plt

# Define the function for |H(jw)|
def magnitude_response(w):
    return 3 / np.sqrt(1 + w**2)

# Frequency range
w = np.linspace(0, 10, 1000)

# Calculate magnitude response
magnitude = magnitude_response(w)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(w, magnitude, label='|H(jω)| = 3/√(1+ω^2)')
plt.xlabel('ω')
plt.ylabel('|H(jω)|')
plt.grid(True)
plt.legend()

plt.savefig('freq.png')
plt.show()
