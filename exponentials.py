import numpy as np
import matplotlib.pyplot as plt
import math

#x = np.linspace(-4,4)
x = np.arange(-5.,5.,0.25)

# Demonstration
y1 = 1.5**x
y2 = 2**x
y3 = 3**x
y4 = 1**x

plt.plot(x,y1,'-bx', label='y = 1.5**x')
plt.plot(x,y2,'-ko', label='y = 2**x')
plt.plot(x,y3,'-c*', label='y = 3**x')
plt.plot(x,y4,'-mx', label='y = 1**x')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-5.,5., 0.,80.])
plt.grid(True)
plt.title('Exponential Functions')
plt.legend()
plt.savefig('exp_demo.png')
