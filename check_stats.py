import psutil
import os
import json

total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

print("vaba RAM:", round(free_memory/1000, 2), "gb")
print("kokku RAM:", round(total_memory/1000, 2), "gb")

hdd = psutil.disk_usage('/')

print("vaba salvestusruumi:", round(hdd.free / (10**9), 2), "gb")
print("kokku salvestusruumi:", round(hdd.total / (10**9), 2), "gb")

warning = 20

if round((used_memory/total_memory) * 100, 2) > warning:
    print("ram usage is more than", warning, "%")
else:
    print("ram usage is fine")

if round((hdd.used/hdd.free) * 100, 2) > warning:
    print("disk usage is more than", warning, "%")
else:
    print("disk usage is fine")

pc_ram = {"ram":{
    "free ram in gb": round(free_memory/1000, 2),
    "total ram in gb": round(total_memory/1000, 2),
    "used ram in %": round((used_memory/total_memory) * 100, 2)
    }
}

pc_disk = {"disk":{
    "free disk space in gb": round(hdd.free / (10**9), 2),
    "total disk space in gb": round(hdd.total / (10**9), 2),
    "used disk space in %": round((hdd.used/hdd.free) * 100, 2)
    }
}

with open ("pc_ram_log.json", "a") as q:
    json.dump(pc_ram, q, indent=4)

with open("pc_disk_log.json", "a") as q2:
    json.dump(pc_disk, q2, indent=4)

