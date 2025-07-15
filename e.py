import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-5.,5.,0.25)

y = 2**x
yd = 0.693*(2**x)

y1 = 3**x
y1d = 1.099*(3**x)

plt.figure(figsize=(10, 4))

# Subplot #1
plt.subplot(1,2,1)
plt.plot(x,y,'-kx', label='y = 2**x')
plt.plot(x,yd,'-rx', label='dy/dx')
#plt.title('y = 2**x')
plt.legend()
plt.grid(True)

# Subplot #2
plt.subplot(1,2,2)
plt.plot(x,y1,'-kx', label='y = 3**x')
plt.plot(x,y1d,'-rx', label='y1d = 1.099*(3**x)')
plt.grid(True)
#plt.title('y = 3**x')
plt.legend()

plt.suptitle('Exponential Functions and e = 2.71828(...)')
plt.savefig('e.png')
