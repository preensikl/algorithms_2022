"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit
from time import perf_counter

def timechecker(func):
    def decorate(arg):
        print("\n", func.__name__)
        print("timeit", timeit(lambda: func(arg), number=1000))
        start = perf_counter()
        a = func(arg)
        print(perf_counter()-start)
        return a
    return decorate


mass = [random.randint(1, 100) for i in range(50*2+1)]
@timechecker
def median_founder(mass_get):
    mass = mass_get[:]
    n, n_full = (len(mass)-1)//2, len(mass)
    for val in range(n):
        for i in range(n_full - val):
            if i+1 != len(mass) and mass[i] > mass[i+1]:
                mass[i], mass[i+1] = mass[i+1], mass[i]
    k = i-1
    return mass[k]
            
median_founder(mass)
