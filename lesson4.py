import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,1,0.01)
xt1 = np.cos(2*np.pi*3*t)
xt2 = np.cos(2*np.pi*5*t)
xt3 = np.cos(2*np.pi*7*t)
xt4 = np.cos(2*np.pi*9*t)

plt.subplot(2,2,1)
plt.plot(t,xt1)
plt.subplot(2,2,2)
plt.plot(t,xt2)
plt.subplot(2,2,3)
plt.plot(t,xt3)
plt.subplot(2,2,4)
plt.plot(t,xt4)
plt.show()
