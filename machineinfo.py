import time
import psutil
from tabulate import tabulate

#informasi cpu
count = psutil.cpu_count()
freq = psutil.cpu_freq()
percent = psutil.cpu_percent()
stat = psutil.cpu_stats()
time = psutil.cpu_times()

print("CPU MACHINE INFORMATION")
print("------------------------")
print("CPU COUNT: ", count)
print("CPU FREQUENCY: ", freq)
print("CPU PERCENT: ", percent)
print("CPU STAT: ", stat)
print("CPU TIME: ", time)
print()

#informasi disk
counters = psutil.disk_io_counters()
partisi = psutil.disk_partitions()

print("DISK INFORMATION")
print("-----------------")
print("COUNTERS DISK: ", counters)
print("DISK PARTITIONS: ", partisi)
print()

#informasi memori
swap = psutil.swap_memory()
virtual = psutil.virtual_memory()

print("MEMORY INFORMATION")
print("-------------------")
print("SWAP MEMORY: ", swap)
print("VIRTUAL MEMORY: ", virtual)
print()

#informasi jaringan
connect = psutil.net_connections()
address = psutil.net_if_addrs()
netstat = psutil.net_if_stats()
netcount = psutil.net_io_counters()

print("NETWORKS DETAILS INFORMATION")
print("-----------------------------")
print("NETWORK CONNECTION: ", connect)
print("NETWORK ADDRESS: ", address)
print("NETWORK STATS: ", netstat)
print("NETWORK COUNTERS", netcount)
print()

#informasi proses
pids = psutil.pids()
iter = psutil.process_iter()

print("PROCESSES INFORMATION")
print("----------------------")
print("PIDS PROCESS: ", pids)
print("ITER PROCESS: ", iter)
print()

#informasi sistem
boot = psutil.boot_time()
user = psutil.users()

print("SYSTEM INFORMATION")
print("-------------------")
print("BOOT TIME: ", boot)
print("USERS: ", user)
