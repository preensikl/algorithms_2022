"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random



mass = [random.randint(1, 30) for i in range(5*2+1)]
print(*mass)


def gnom_sort(ls):
    n = len(ls)
    i = 0
    while True:
        if i+1 == n:
            break
        if ls[i+1] >= ls[i]:
            i += 1
        else:
            ls[i], ls[i+1] = ls[i+1], ls[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return ls 

def median(obj):
    for i in range(len(obj)):
        if i+1 == len(obj):
            break
        if obj[i] > obj[i+1]:
            return "List is not sorted"
    return obj[(len(obj)-1)//2]

mass = gnom_sort(mass)
median_int = median(mass)
print(mass, median_int)