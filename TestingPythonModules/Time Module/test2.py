import time
t = list(map(int, time.strftime("%H:%M:%S", time.localtime()).split(":")))
print(type(t[2]))
print(t[2])