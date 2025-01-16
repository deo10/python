# working with date and time in python

from datetime import date

print(type(date))
# <class 'type'>

my_date = date(2020, 1, 1)
print(my_date)
# 2020-01-01

from datetime import time

print(type(time))
# <class 'type'>

my_time = time(12, 30, 45)
print(my_time)
# 12:30:45

print(my_time.hour)
# 12



import datetime

# get the current date and time
now = datetime.datetime.now()

# print the current date and time
print(now)
# print the current year
print(now.year)
# print the current month
print(now.month)
# print the current day
print(now.day)
# print the current hour
print(now.hour)

# format the current date and time - strftime() method
print(now.strftime("%Y-%m-%d %H:%M:%S"))
# 2020-08-01 12:30:45
print(now.strftime("%Y-%b-%d %H:%M:%S"))
# 2020-Aug-01 12:30:45


# from str to datetime
date_str = '2020-08-01'
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)
# 2020-08-01 00:00:00


# work with timedelta - add or subtract time

from datetime import timedelta

print(now + timedelta(days=1))
# 2020-08-02 12:30:45 - add 1 day

print(now + timedelta(hours=1))
# 2020-08-01 13:30:45 - add 1 hour

print(now + timedelta(days=1, hours=1, minutes=30))
# 2020-08-02 13:00:45 - add 1 day, 1 hour, 30 minutes

print(now - timedelta(days=1, hours=1, minutes=30))
# 2020-07-31 11:00:45 - subtract 1 day, 1 hour, 30 minutes


# module time

import time

# get the current time in seconds
print(time.time())
# 1596271845.155

# get the current time in seconds - readable format
print(time.ctime())
# Sat Aug  1 12:30:45 2020
print(time.ctime(43534534))
# Thu May 20 02:55:34 1971

# sleep for 2 seconds - pause the program
time.sleep(2)

