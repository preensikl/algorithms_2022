"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
import random
from collections import deque
from time import perf_counter
from timeit import timeit

def timechecker(func):
    def decorate(arg):
        print("\n", func.__name__)
        print("timeit", timeit(lambda: func(arg), number=1000))
        start = perf_counter()
        a = func(arg)
        print(perf_counter()-start)
        return a
    return decorate



unsort =  [random.randint(1, 1000) for i in range(100)]

@timechecker
def buble_sort_reversed(obj):
    counter = 0
    for b in reversed(range(len(obj))):
        for i in reversed(range(0, len(obj)-counter)):
            if obj[i] < obj[i-1] and i != 0:
                obj[i], obj[i-1] = obj[i-1], obj[i]
    return obj
            
buble_sort_reversed(unsort[:])