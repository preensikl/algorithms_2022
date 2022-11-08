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

Это файл для второго скрипта
"""
import json
from memory_profiler import memory_usage
from func_analize import class_analiz

# 1
@class_analiz
class Steck:
    def __init__(self, **kwargs ):
        self.size = kwargs["size"]
        self.lst = [[]]

    def app(self, arg):
            if len(self.lst[-1]) <= self.size:
                self.lst[-1].append(arg)
            else :
                self.lst.append([])
                self.lst[-1].append(arg)
                

    def get(self):
        if self.lst != [[]] and self.lst != []:
            self.getter = self.lst[-1][-1]    
            self.__delete()
            return self.getter

    def __delete(self):
        self.lst[-1].remove(self.getter)
        if self.lst[-1] == []:
            del self.lst[-1]

    
    def __str__(self):
        return f"{self.lst}"

first_example = Steck(size = 2)
for i in range(100):
    first_example.app(i*2)

# 2
@class_analiz
class Steck_optimization:
    __slots__=("size", "lst", "getter")
    def __init__(self, **kwargs):
        self.size = kwargs["size"]-1
        self.lst = str([[]])

    def app(self, arg):
            self.lst = json.loads(self.lst)
            if len(self.lst[-1]) <= self.size:
                self.lst[-1].append(arg)
            else :
                self.lst.append([])
                self.lst[-1].append(arg)
            self.lst=json.dumps(self.lst)

    def get(self):
        self.lst = json.loads(self.lst)
        if self.lst != [[]] and self.lst != []:
            self.getter = self.lst[-1][-1]   
            self.__delete()
            return self.getter

    def __delete(self):
        self.lst[-1].remove(self.getter)
        if self.lst[-1] == []:
            del self.lst[-1]
        self.lst=json.dumps(self.lst)

    def __str__(self):
        return self.lst

second_example = Steck_optimization(size = 2)
for i in range(10):
    second_example.app(i*2)