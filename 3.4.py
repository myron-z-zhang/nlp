import numpy as np

c,v = np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
vwap = np.average(c, weights=v)
print "VWAP =", vwap
print "mean =", np.mean(c)
t = np.arange(len(c))
print "t =", t
print "TWAP =", np.average(c, weights=t)

h,l = np.loadtxt('data.csv', delimiter=',', usecols=(4,5), unpack=True)
print "highest =", max(h)
print "average in high =", np.average(h)
print "Spread high price", np.ptp(h)
print "lowest =", min(l)
print "average in low =", np.average(l)
print "Spread low price", np.ptp(l)
