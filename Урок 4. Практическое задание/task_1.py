"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import timeit
# from functools import cache

list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18]

def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

test_1 = timeit.timeit(stmt= lambda: func_1(list_test), number=1000)
print(test_1)

def func_2(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i]%2 == 0]
    return new_arr

test_2 = timeit.timeit(stmt=lambda: func_2(list_test), number=1000)
print(test_2)

new_list = []

def func_3(i, nums):
    if len(nums) == i:
        return new_list
    if nums[i] % 2 == 0:
        new_list.append(i)
    return func_3(i+1, nums)

test_3 = timeit.timeit(stmt=lambda: func_3(0, list_test), number=1000)
print(test_3)

new_list_1 = []
counter = 0

def func_4(nums):
    global counter
    if len(nums) == 0:
        return new_list_1
    if nums[0] % 2 == 0:
        new_list_1.append(counter)
    counter = counter + 1
    return func_4(nums[1:])

test_4 = timeit.timeit(stmt=lambda: func_4(list_test), number=1000)
print(test_4)


list_test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18}


def func_5(nums):
    new_arr = []
    counter = 0
    for i in range(len(nums)):
        counter = counter + 1
        a = nums.pop()
        if a % 2 == 0:
            new_arr.append(counter)
    return new_arr

test_5 = timeit.timeit(stmt= lambda: func_5(list_test_set), number=1000)
print(test_5)


list_test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18}
new_list_1 = []
counter = 0

def test_6(nums):
    global counter
    if len(nums) == 0:
        return new_list_1
    if  nums.pop() % 2 == 0:
        new_list_1.append(counter)
    counter = counter + 1
    return func_4(nums)

test_6 = timeit.timeit(stmt=lambda: test_6(list_test), number=1000)
print(test_6)