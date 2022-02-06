import os
import psutil


#path = psutil.Popen([input("Insert Path: ")]).pid
path = input("Insert Path: ")
interval = input("Set Interval: ")

def file_Open():
    file = psutil.Popen([path]).pid
    return file


def cpu_load():
    process = psutil.Process(file)
    cpu_l = process.cpu_percent(interval=1)
    return cpu_l


def process_memory():
    process = psutil.Process(file)
    mem_info = process.memory_info()
    return mem_info.rss, mem_info.vms


def handles():
    process = psutil.Process(file)
    n_handles = process.num_handles()
    return n_handles

file = file_Open()
cpu = cpu_load()
mem = process_memory()
handl = handles()

for pid in psutil.pids():
    while pid == file:
       print(file)
       print(cpu)
       print(mem)
       print(handl)


# C:\Windows\System32\notepad.exe
# C:\Program Files\Autodesk\AutoCAD 2016\acad.exe
