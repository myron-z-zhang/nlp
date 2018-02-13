import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = int(sys.argv[1])

x = np.arange(5)
print "Exp", np.exp(x)
print "Linspace", np.linspace(-1, 0, 5)


weights = np.exp(np.linspace(-1., 0., N))
weights /= weights.sum()
print "weights", weights

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N-1:-N+1]
t = np.arange(N-1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, sma, lw=2.0)
show()

