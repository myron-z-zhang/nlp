import numpy as np
import sys

o, h, l, c = np.loadtxt('BHP.csv', delimiter=',', usecols=(3, 4, 5, 6), unpack=True)

def calc_profit(opens, high, low, close):
    buy = opens * float(sys.argv[1])

    if low < buy < high:
        return (close - buy)/buy

