"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
import random
from collections import deque
from timeit import timeit



just_list = []
for i in range(10000):
    just_list.append(random.randint(1, 1000))
just_deque = deque(just_list)

salt = [644, 109, 817, 153, 566, 495, 591]
RANGE_COUNTER = 10
INDEXES = [13, 2, 11, 12, 10]

# 1
# 1.1
def append_left_deque(arg):
    for i in range(RANGE_COUNTER):
        arg.appendleft(i)

# 1.2
def pop_left_deque(arg):
    for i in range(RANGE_COUNTER):
        arg.popleft()

# 1.3
def extend_deque(arg, sol):
    arg.extend(sol)

# 2

def pop_left_deque(arg):
    for i in range(RANGE_COUNTER):
        arg.popleft()

def append_left_list(arg):
    for i in range(RANGE_COUNTER):
        arg.insert(0, i)

def extendleft_deque(arg, sol):
    arg.extendleft(sol)

def pop_left_list(arg):
    for i in range(RANGE_COUNTER):
        arg.pop(0)


# 3
def get_el_deque(arg):
    a = 0
    for i in INDEXES:
        a = arg[i]

def get_el_list(arg):
    a = 0
    for i in INDEXES:
        a = arg[i]


# append_left_deque(just_deque)
# pop_left_deque(just_deque)
# extend_deque(just_deque, salt)
# pop_left_deque(just_deque)
# append_left_list(just_list)
# extendleft_deque(just_deque, salt)
# pop_left_list(just_list)
# get_el_deque(just_deque)
# get_el_list(just_list)

print(f"{append_left_deque.__name__} vs {append_left_list.__name__}")
print(append_left_deque.__name__, timeit(lambda: append_left_deque(just_deque), number=1000))
print(append_left_list.__name__, timeit(lambda: append_left_list(just_list), number=1000))
print()
print(f"{pop_left_deque.__name__} vs {pop_left_list.__name__}")
print(pop_left_deque.__name__, timeit(lambda: pop_left_deque(just_deque), number=1000))
print(pop_left_list.__name__, timeit(lambda: pop_left_list(just_list), number=1000))
print()
print(f"{get_el_deque.__name__} vs {get_el_list.__name__}")
print(get_el_deque.__name__, timeit(lambda: get_el_deque(just_deque), number=1000))
print(get_el_list.__name__, timeit(lambda: get_el_list(just_list), number=10000000))
print()
print("Just count of time")
print(extend_deque.__name__, timeit(lambda:extendleft_deque(just_deque, salt), number=1000))
print(extendleft_deque.__name__, timeit(lambda: extendleft_deque(just_deque, salt), number=1000))