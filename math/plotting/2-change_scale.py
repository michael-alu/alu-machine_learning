#!/user/bin/evn
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,21000,1000)
r = np.log(0.5)
t = 5730
y = np.exp((r/t) * x)

plt.plot(x,y)

plt.xlim(0,28650)

plt.yscale('log')

plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

plt.show()