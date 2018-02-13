import numpy as np
import sys

N = int(sys.argv[1])

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
b = c[-N:]
print 'first b', b
b = b[::-1]
print 'second b', b

A = np.zeros((N, N), float)
print 'Zeros N by N', A

for i in range(N):
    A[i, ] = c[-N-1-i: -1-i]
print 'A', A

(x, residuals, rank, s) = np.linalg.lstsq(A, b)

print x, residuals, rank, s
print np.dot(b, x)