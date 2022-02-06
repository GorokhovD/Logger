import os
import psutil
from time import sleep

path = input("Insert Path: ")
interval = int(input("Set Interval: "))

def proc_Open():
    file = psutil.Popen([path]).pid
    return file


def cpu_load():
    process = psutil.Process(proc)
    cpu_l = process.cpu_percent(interval=1)
    return cpu_l


def process_memory():
    process = psutil.Process(proc)
    mem_info = process.memory_info()
    return mem_info.rss, mem_info.vms


def handles():
    process = psutil.Process(proc)
    n_handles = process.num_handles()
    return n_handles


def writer():
    f = open("logger.log", "a")
    f.write("============== \n")
    f.write("Process ID:    %i \n" % proc + "Process used CPU:     %i \n" % cpu + "Process used memory rss:     %i \n Process used memory vms:     %i \n" % mem + "Process Handle:     %i \n" % handl)
    f.close()
    print("Log Saved")

proc = proc_Open()
cpu = cpu_load()
mem = process_memory()
handl = handles()

while psutil.pid_exists(proc):
    writer()
    sleep(interval)



# C:\Windows\System32\notepad.exe
# C:\Program Files\Autodesk\AutoCAD 2016\acad.exe
