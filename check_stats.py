import psutil
import os

print('RAM used:', psutil.virtual_memory()[2], '%')

# total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

# print("vaba RAM:", round(free_memory/1000, 2), "gb")
# print("kokku RAM:", round(total_memory/1000, 2), "gb")

hdd = psutil.disk_usage('/')

print("vaba salvestusruumi:", hdd.free / (230))
print(hdd.total // (230))
