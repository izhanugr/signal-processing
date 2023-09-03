#to Plot sin and cos wave

import numpy as np
import matplotlib.pyplot as plt

#to define independent and dependent variable
t = np.arange(0,1,0.001)
xt = np.sin(2*np.pi*3*t)

#to plot the signal
plt.plot(t, xt)
plt.title('Sine Wave')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()