''' ----- Logger V 1.0 ----- '''

# Импортируем необхоимые библиотеки
import os
import psutil
from time import sleep

# Приветствие и краткая инструкция по работе с программой
print('''Hey! To perform my work, \n
you need to enter the path and \n
the time Interval in seconds after which the file will be written! \n
Example: \nInsert Path: C:\Windows\System32\calc.exe \nSet Interval: 7''')

# Задаем параметры для работы программы
path = input("Insert Path: ")
interval = int(input("Set Interval: "))

# Определяем набор функций для извлечения информации о каждом необходимом нам процессе.
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

# Создаем функцию для создания и записи данных в файл
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

# Условия выполнения программы
while psutil.pid_exists(proc):
    writer()
    sleep(interval)



# готовый путь для запуска теста программы C:\Windows\System32\notepad.exe
