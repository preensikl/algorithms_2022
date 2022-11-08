"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from collections import Counter
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1(array_f):
    m = 0
    num = 0
    for i in array_f:
        count = array_f.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array_f):
    new_array = []
    for el in array_f:
        count2 = array_f.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array_f[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3(array_f):
    return f"{list((Counter(array_f).items()))[0]}"

# "Очень интересная ситуация, если возвращать обьект каунтера, то время в 2 раза дольше.
# А если конвертировать в лист, то быстрее."


print(func_1(array))
print(func_2(array))
print(func_3(array))

print(timeit(stmt=lambda: func_1(array)))
print(timeit(stmt=lambda: func_2(array)))
print(timeit(stmt=lambda: func_3(array)))