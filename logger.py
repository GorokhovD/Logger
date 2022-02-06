import os
import psutil

path = psutil.Popen([input("Insert Path: ")]).pid
#cpuu = psutil.cpu_percent(interval=3)

def cpu_load():
    process = psutil.Process(path)
    cpu_l = process.cpu_percent(interval=1)
    return cpu_l


def process_memory():
    process = psutil.Process(path)
    mem_info = process.memory_info()
    return mem_info.rss, mem_info.vms


def handles():
    process = psutil.Process(path)
    n_handles = process.num_handles()
    return n_handles

cpu = cpu_load()
mem = process_memory()
handl = handles()

print(path)
print(cpu)
print(mem)
print(handl)


# C:\Windows\System32\notepad.exe
# C:\Program Files\Autodesk\AutoCAD 2016\acad.exe
