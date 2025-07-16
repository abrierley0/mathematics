import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-3,3,0.25)

y = 6 + 10*math.e**(0.5*x)

plt.plot(x,y, '-kx', label=f'4 - math.e**x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Exponential Plotter')
plt.grid(True)
plt.savefig('exponential.png')
 