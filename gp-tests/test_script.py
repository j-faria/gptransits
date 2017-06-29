import matplotlib.pyplot as plt
import numpy as np

timeResults = np.genfromtxt('results.dat')
freqResults = np.genfromtxt('diamonds_results.dat')

fig = plt.figure("Amplitude 1 (S0)", figsize=(10, 7))
plt.scatter(timeResults[:,1], freqResults[:,1], s=30)
plt.title("Amplitude S0 (ppm) - 1")
plt.xlabel('Timeseries')
plt.ylabel('Diamonds')
plt.tight_layout()

fig2 = plt.figure("Characteristic Frequency w0 (muHz) - 1", figsize=(10, 7))
plt.scatter(timeResults[:,2], freqResults[:,2], s=30)
plt.title("Characteristic Frequency 1 (w0)")
plt.xlabel('Timeseries')
plt.ylabel('Diamonds')
plt.tight_layout()

fig3 = plt.figure("Amplitude S0 (ppm) - 2", figsize=(10, 7))
plt.scatter(timeResults[:,1], freqResults[:,3], s=30)
plt.title("Amplitude 2 (S0)")
plt.xlabel('Timeseries')
plt.ylabel('Diamonds')
plt.tight_layout()

fig4 = plt.figure("Characteristic Frequency w0 (muHz) - 2", figsize=(10, 7))
plt.scatter(timeResults[:,2], freqResults[:,4], s=30)
plt.title("Characteristic Frequency 2 (w0)")
plt.xlabel('Timeseries')
plt.ylabel('Diamonds')
plt.tight_layout()

plt.show()