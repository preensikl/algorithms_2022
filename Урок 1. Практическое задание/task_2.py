"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

def func_1(obj):                                        # O(n^2)
    count = 0                                           # O(1)
    for i1 in range(len(obj)):                          # O(n)
        for i2 in range(count, len(obj)):               # O(n)
            if obj[i2] > obj[i1]:                       # O(1)
                obj[i2], obj[i1] = obj[i1], obj[i2]     # O(1)
            count+1                                     # O(1)
    return obj[0]                                       # O(1)

obj_1 = [1, 3, 5, 200, 34, 54, 34]
print("func_1 - ", func_1(obj_1)) 

def func_2(obj):                        # O(n)
    numb = obj[0]                       # O(1)
    for i in range(2, len(obj)):        # O(n)
        if obj[i] < numb:               # O(1)
            numb = obj[i]               # O(1)
    return numb                         # O(1)

print("func_2 - ", func_2([30, 20, 3, 2, 4, 10, 2, 15]))
