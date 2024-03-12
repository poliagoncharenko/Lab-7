import scipy
import time as time
import numpy as np
from random import randint


numbers = [randint(1, 1000001) for i in range(1000000)]
numbers1 = [randint(1, 1000001) for z in range(1000000)]
res_list = []
t_list_start = time.perf_counter()
for i in range(0, len(numbers)):
    res_list.append(numbers[i] * numbers1[i])
t_list_stop = time.perf_counter()


num = np.array(numbers, int)
num1 = np.array(numbers1, int)
t_array_start = time.perf_counter()
res = np.multiply(num, num1)
t_array_stop = time.perf_counter()


print(f'Время выполнения поэлементного умножения для numpy меньше чем для стандартных списков на: {(t_list_stop-t_list_start) - (t_array_stop-t_array_start)}')