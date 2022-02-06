import os
import psutil
import threading


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

def log():
    return proc, cpu, mem, handl
    #print("Process ID: %i" % proc, "Process used CPU: %i" % cpu, "Process used memory => rss: %i vms: %i" % mem, "Process Handle: %i" % handl)

proc = proc_Open()
cpu = cpu_load()
mem = process_memory()
handl = handles()
log = str(log())

for pid in psutil.pids():
    while pid == proc:
        f = open("logger.log", "w")
        f.write("Process Log %s \n" % path)
        threading.Timer(interval, f.write(log))
        print(log)
        #print(cpu)
        #print(mem)
        #print(handl)


# C:\Windows\System32\notepad.exe
# C:\Program Files\Autodesk\AutoCAD 2016\acad.exe
