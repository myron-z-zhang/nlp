import numpy as np
import matplotlib.pyplot as plt

func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
func1 = func.deriv(m=1) 
x = np.linspace(-10, 10, 30)
print 'x', x
y = func(x)
print 'y', y
y1 = func1(x)
print 'y1', y1

plt.plot(x, y, 'ro', x, y1, 'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
