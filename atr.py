import numpy as np
import sys

h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4,5,6), unpack=True)
print "h", h
print "l", l
N = int(sys.argv[1])
h = h[-N:]
l = l[-N:]
print "h-", h
print "l-", l
print "close", c
previousclose = c[-N-1:-1]
print "priviousclose", previousclose

truerange = np.maximum(h - l, h - previousclose, previousclose-l)
print "true range", truerange

atr = np.zeros(N)
atr[0] = np.mean(truerange)

for i in range(1, N):
    atr[i] = (N - 1)*atr[i - 1] + truerange[i]
    atr[i] /= N

print "atr", atr
