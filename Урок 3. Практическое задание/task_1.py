"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from time import time
from time_checker import time_checker

first_list = []
second_list = []


@time_checker
def task_1_1(*args):            #O(n)
   print("\ntask_1_1")
   for i in range(1000):   #O(n)
      first_list.append(i)  #O(1)
task_1_1()

@time_checker
def task_1_2(*args):                 
   print("\ntask_1_2")  
   for i in range(1000):         
      second_list.append(str(i))
task_1_2()



@time_checker
def task_2_1(obj):
   print("\ntask_2_1")
   for i in obj:
      b = i
task_2_1(first_list)

@time_checker
def task_2_2(obj):
   print("\ntask_2_2")
   for i in range(len(obj)):
      b = obj[i]
task_2_2(second_list)


@time_checker
def task_3_1(obj):
   print("\ntask_3_1")
   for i in obj[0]:
      obj[0].remove(i)
task_3_1(first_list)

def task_3_2(obj):
   print("\ntask_3_2")
   for i in obj[0]:
      obj[0].remove(i)
task_3_1(first_list)