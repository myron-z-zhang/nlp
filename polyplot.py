import numpy as np
import matplotlib.pyplot as plt

#func = np.poly1d(np.array([1, 5, 3]).astype(float))
func = np.poly1d([1., 2., 3.])
print 'func                       ', func
x = np.linspace(-10, 10, 30)
print 'x', x
y = func(x)
print 'y', y

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
