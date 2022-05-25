import psutil
import os

print('RAM used:', psutil.virtual_memory()[2], '%')

total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

print("vaba RAM:", round(free_memory/1000, 2), "gb")
print("kokku RAM:", round(total_memory/1000, 2), "gb")

hdd = psutil.disk_usage('/')

print("vaba salvestusruumi:", round(hdd.free / (10**9), 2), "gb")
print("kokku salvestusruumi:", round(hdd.total / (10**9), 2), "gb")

warning = 50

if round((used_memory/total_memory) * 100, 2) > warning:
    print("ram usage is more than", warning, "%")
else:
    print("ram usage is fine")

if round((hdd.used/hdd.free) * 100, 2) > warning:
    print("disk usage is more than", warning, "%")
else:
    print("disk usage is fine")

