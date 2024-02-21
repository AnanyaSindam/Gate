import numpy as np
import matplotlib.pyplot as plt

# Load data from the freq.dat file
data = np.loadtxt('freq.dat')

# Extract frequency, magnitude, and phase values
frequency = data[:, 0]
magnitude = data[:, 1]
phase = data[:, 2]

# Plot magnitude response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(frequency, magnitude)
plt.xlabel('ω')
plt.ylabel('|H(jω)|')
plt.grid(True)
plt.savefig('freq.png') 
plt.show() 

# Plot phase response
plt.figure(figsize=(10, 6))
plt.plot(frequency, phase)
plt.xlabel('ω')
plt.ylabel('Phase (degrees)')
plt.grid(True)
plt.savefig('phase.png') 
plt.show() 

