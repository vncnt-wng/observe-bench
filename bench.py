import psutil
from os import getpid
from time import sleep
import time
import sys
import subprocess

# psutil.cpu_percent(interval=1)
# per_cpu = psutil.cpu_percent(percpu=True)
# # For individual core usage with blocking, psutil.cpu_percent(interval=1, percpu=True)
# for idx, usage in enumerate(per_cpu):
#     print(f"CORE_{idx+1}: {usage}%")

# mem_usage = psutil.virtual_memory()

import psutil

print(sys.argv[1])
TEST_TIME = 15
clock = 0
interval = 0.5

stdout_lines = (
    subprocess.run(["lsof", "-i", f":{sys.argv[1]}"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .split("\n")
)

filtered = list(filter(lambda x: x != "", stdout_lines[1].split(" ")))

pid = filtered[1]

p = psutil.Process(int(pid))

f = open(f"results/{sys.argv[2]}", "w")

start_time = time.time()

while time.time() < start_time + TEST_TIME:
    f.write(f"{p.cpu_percent(interval=0.1)},{p.memory_percent()}\n")
    # clock += interval
    # sleep(interval)

f.close()

# for process in [psutil.Process(pid) for pid in psutil.pids()]:
#     if process.name() != "kernel_task":
#         print("Name:", process.name())
#         print("CPU%:", process.cpu_percent(interval=0.5))
#         print("MEM%:", process.memory_percent())
