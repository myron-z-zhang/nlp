import numpy as np

c, v = np.loadtxt('BHP.csv', delimiter=',', usecols=(6, 7), unpack=True)

change = np.diff(c)
print 'Change', change

signs = np.sign(change)
print 'Signs', signs

print 'v', v[1:]
print 'On balance volume', v[1:] * signs
