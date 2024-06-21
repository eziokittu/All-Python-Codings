import time

print("----------------01. time.time()-----------------")
# time.time() - It returns us the seconds of time that have elapsed since the Unix epoch.
# In simple words, it tells us the time in seconds that have passed since 1 January 1970.
print("Seconds elapsed since 1 Jan 1970 -", time.time())

print("\n---------------02. time.asktime()----------------")
# time.asktime() - It returns us the current time in one string in the format
# DAY MONTH DATE HOUR:MINS:SECS YEAR by default, and giving parameters in the form of a tuple
# (exactly 9) say time.asctime((year, month, dayinmonth, hour, min, sec, xx, dayinyear, xx))
# returns the date in the format DAY MONTH DATE HOUR:MINS:SECS YEAR
print(time.asctime((2019, 12, 29, 13, 55, 43, 4, 354, 0)))
print(time.asctime())

print("\n----------------03. time.sleep()-----------------")
# time.sleep() - it delays the execution of further commands for given specific seconds.
# In simple terms, it sends the program to sleep for some defined number of seconds.
print("Printed Before")
time.sleep(1.000)
print("Printed After 1.0 seconds")

print("\n--------------04. time.localtime()---------------")
# time.localtime() - takes the number of seconds passed since epoch
# as an argument and returns struct_time in local time.
print(time.localtime())
print(time.asctime(time.localtime()))

print("\n--------------05. time.strftime()---------------")
# time.strftime() - This function takes struct_time (or tuple corresponding to it)
# as an argument and returns a string representing it based on the format code used.
# %Y - year [0001,..., 2018, 2019,..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23
# %M - minutes [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 61]
# To learn more, visit: https://docs.python.org/3/library/time.html#time.strftime
print( time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()) )
example_tuple = (2019, 12, 29, 13, 55, 43, 4, 354, 0)
print( time.strftime("He arrived at %H:%M on %m/%d/%Y with a heavy suitcase to stay", example_tuple) )

print("\n--------------06. time.strptime()---------------")
# time.strptime() - The strptime() function parses a string representing time
# and returns struct_time.
time_string = "2018 21st june"
time_structTime = time.strptime(time_string, "%Y %dst %B")
print(time_structTime) # time.struct_time
print(time.asctime(time_structTime))

print("\n--------------07. time.mktime()---------------")
# time.mktime() - takes struct_time (or a tuple containing 9 elements corresponding to struct_time)
# as an argument and returns the seconds passed since epoch in local time.
# Basically, it's the inverse function of localtime()
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
local_time = time.mktime(t)
print("Local time:", local_time)

print("\n--------------08. time.gmtime()---------------")
# time.gmtime() - The gmtime() function takes the number of seconds
# passed since epoch as an argument and returns struct_time in UTC.
result = time.gmtime(1545925769)
print("result:", result)
print("year:", result.tm_year)
print("tm_hour:", result.tm_hour)
# [NOTE] - If no argument or None is passed to gmtime(), the value returned by time() is used.