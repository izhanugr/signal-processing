#to plote discrete time sequence

import matplotlib.pyplot as plt

n = [0,1,2,3,4,5,6]
xn = [-1,4,-3,0,9,8,9]

plt.stem(n,xn)
plt.title('discrete time Seqeunce')
plt.xlabel('----->n')
plt.ylabel('Amplitude')
plt.show()