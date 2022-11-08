"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
# from collections
from abc import ABC, abstractmethod
from collections import deque


class Calculator(ABC):
    # @abstractmethod
    def __init__(self):
        self.sum16 = 0
        self.mult16 = 1

    # @abstractmethod
    def calculator(self, *args):
        for i in args:
            self.sum16 = self.sum16 + int(i, 16)
        return deque(hex(self.sum16))
    
    # @abstractmethod
    def multiplication(self, *args):
        for i in args:
            self.mult16 = self.mult16 * int(i, 16)
        return deque(hex(self.mult16))

calc = Calculator()
summ = calc.calculator("a2", "C4F")
print(summ)

mult = calc.multiplication("a2", "C4F")
print(mult)


print(deque(hex(int("a2", 16)+int("C4F", 16))))