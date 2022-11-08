"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
info_1 = {"microsoft": 30, "apple": 20, "google": 40, "IBM":50, "amazon":60, "ozon":10}
info_2 = [("microsoft", 30), ("apple", 60), ("google", 40), ("IBM", 50), ("amazon", 20), ("ozon", 10)]

def func_1(obj):                                # O(n)
    max_capitals = []                           # O(1)
    for i in range(3):                          # O(1)
        cap = {"none": 0}                       # O(1)
        max_capitals.append(cap)                # O(1)
        for [key, val] in obj.items():          # O(n)
            if val > list(cap.items())[0][1]:   # O(1)
                cap.clear()                     # O(1)
                cap[key] = val                  # O(1)
        max_capitals.append(cap.copy())         # O(n)
        one = list(cap.items())[0][0]           # O(1)
        obj.pop(one)                            # O(1)
        cap.clear()                             # O(1)
    return max_capitals                         # O(1)
print(func_1(info_1)) 

print()

def func_2(obj):                                        # O(n^2)
    for i in range(len(obj)):                           # O(n)
        for i in range(len(obj)):                       # O(n)
            if i == len(obj)-1:                         # O(1)
                break                                   # O(1)
            if obj[i][1] > obj[i+1][1]:                 # O(1)
                obj[i], obj[i+1] = obj[i+1], obj[i]     # O(1)
    return obj[-3:]                                     # O(1)



print(func_2(info_2))


# Считаю, что решение func_1 более эффективное, т.к. имеет более низкую степень сложности О(n) 