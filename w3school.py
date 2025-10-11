
import numpy as np
import matplotlib.pyplot as plot
# Specify the range of values of the sine wave
time = np.arange(0, 10, 0.1)
# Amplitude of the sine wave is calculated by the sine of values of the variable
amplitude = np.sin(time)
# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, amplitude)
# Give a title for the sine wave plot, the x-axis, and the y-axis
plot.title('Sine wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='b')
# Display the sine wave
plot.show()