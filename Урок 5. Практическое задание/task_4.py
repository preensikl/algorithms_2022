"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

just_dict = {}
special_dict = OrderedDict()
tests_number = 10000
func_list = []

def test_function(func):
    print(func.__name__, timeit(func, number=tests_number))

def test_append_dict():
    for i in range(1000):
        just_dict[i] = f"test: {i}"

def test_append_OrderDict():
    for i in range(1000):
        special_dict[i] = f"test: {i}"

def test_dict_copy():
    a = just_dict.copy()
    return a

def test_OrderDict_copy():
    a = special_dict.copy()
    return a

def test_dict_get():
    for i in range(1000):
        a = just_dict.get(i)

def test_OrderDoct_get():
    for i in range(1000):
        a = special_dict.get(i)

def test_dict_items():
    for key, value in just_dict.items():
        a, b = key, value

def test_OrderDict_items():
    for key, value in special_dict.items():
        a, b = key, value

def test_dict_keys():
    a = just_dict.keys()

def test_OrderDict_keys():
    a = special_dict.keys()

def test_dict_clear():
    for i in range(30):
        just_dict.clear()

def test_OrderDict_clear():
    for i in range(30):
        special_dict.clear()

func_list = [test_append_dict, test_append_OrderDict, 
            test_dict_copy, test_OrderDict_copy, 
            test_dict_get, test_OrderDoct_get,
            test_dict_items, test_OrderDict_items, 
            test_dict_keys, test_OrderDict_keys, 
            test_dict_clear, test_OrderDict_clear]

for i in range(len(func_list)):
    if i % 2!= 1:
        print()
    test_function(func_list[i])




