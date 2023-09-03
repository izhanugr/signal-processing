import numpy as np
import matplotlib.pyplot as plt

#to define independent & dependent var
n = np.arange(0,1,0.01)
xn = np.sin(2*np.pi*3*n)

#to plot the signal
plt.stem(n,xn)
plt.title('Sampled sin wave')
plt.xlabel('----->n')
plt.ylabel('Amplitude')
plt.show()

