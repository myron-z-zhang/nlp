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

# get first Monday
first_monday = np.ravel(np.where(dates == 0))[0]
print "Before ravel", np.where(dates == 0)
print "After ravel", np.ravel(np.where(dates == 0))
print "The first Monday index is", first_monday

# get last Friday
last_friday = np.ravel(np.where(dates == 4))[-1]
print "The last Friday index is", last_friday

weeks_indices = np.arange(first_monday, last_friday+1)
print "Weeks indices initial", weeks_indices

weeks_indices = np.split(weeks_indices, 3)
print "Weeks indices after split", weeks_indices

def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]

    return("APPL", monday_open, week_high, week_low, friday_close)

weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, opens, high, low, closes)
print "Week summary", weeksummary

np.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")

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

