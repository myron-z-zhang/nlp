# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import numpy as np
from datetime import datetime

# ////
# 星期二 1
# 星期三 2
# 星期四 3
# 星期五 4
# 星期六 5
# 星期日 6

def datestr2num(s):
    return datetime.strptime(s, '%d-%m-%Y').date().weekday()

dates, opens, high, low, closes = np.loadtxt('data.csv', delimiter=',', usecols=(1,3,4,5,6), converters={1:datestr2num}, unpack=True)
closes = closes[:16]
dates = dates[:16]
print "Dates =", dates
print "Closes =", closes

averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(closes, indices)
    avg = np.mean(prices)
    print 'Day', i, 'prices', prices, 'Average', avg
    averages[i] = avg

top = np.max(averages)
print 'Highest average', top
print 'Top day of week', np.argmax(averages)
bottom = np.min(averages)
print "Lowest average", bottom
print 'Low day of week', np.argmin(averages)

