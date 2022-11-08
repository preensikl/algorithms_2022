"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""
from func_analize import func_analize

@func_analize
def calculator():
    operations = ["+", "-", "/", "*"]
    operation = input("Write operation: ")
    if operation == "0":
        return
    if operation not in operations:
        print("Dont do it!")    
    first_numb = input("First_number: ")
    second_numb = input("Second_number: ")
    if (operation == "/" and second_numb == "0") == False :
        print(f'Your answer: {eval(f"{first_numb}{operation}{second_numb}")}')
    else:
        print("You can not division for 0")
calculator()


class calculator_optimizate():
    __slots__=("symbvol", "first", "second", "box_of_operation", "info")
    def __init__(self):
        self.box_of_operation = ("+", "-", "//", "*")
        self.info = "Not correct operation"
    @func_analize
    def culculate(self):
        self.symbvol = input("operation: ")
        if self.symbvol in self.box_of_operation:
            self.first= input("first: ")
            self.second = input("second: ")
            if self.symbvol == "//" and self.second == "0":
                return "You can not divide second for zero"
            else:
                return eval(f"{self.first}{self.symbvol}{self.second}")
        else:
            return self.info

print(calculator_optimizate().culculate())

