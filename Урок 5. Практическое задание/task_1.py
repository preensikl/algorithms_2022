"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34 

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple
from pprint import pprint

Company = namedtuple('Company', 'name first second third fouth')

Horns = Company(name="Horns", first=235, second=345634, third=55, fouth=235)
Hooves = Company(name="Hooves", first=123, second=1111, third=99, fouth=500)
Street_food = Company(name="Street_food", first=10, second=11, third=20, fouth=5)


def company_counter(*args):
    down = []
    high = []
    middle = 0
    for i in args:
        middle = middle + sum([i[1], i[2], i[3], i[4]])
    middle = middle // len(args)
    for i in args:
        if sum([i[1], i[2], i[3], i[4]]) > middle:
            high.append(i[0])
        else:
            down.append(i[0])
    return (("down", down), ("high", high))


total_years_info = company_counter(Horns, Hooves, Street_food)
pprint(total_years_info)