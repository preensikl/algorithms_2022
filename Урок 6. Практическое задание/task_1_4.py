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

Это файл для четвертого скрипта
"""
import sqlite3
import hashlib

# 1
class Web_cash():
    __clots__ = ("salt", "conn", "curs", "result", "url_hash", "url")

    def __init__(self):
        self.salt = "f2fdd202e5c94d60984f77e4e2b624a1"

    def __db_helper(self, magic):
        self.conn = sqlite3.connect("urls_cash.db")
        self.curs = self.conn.cursor()
        self.result = self.curs.execute(magic).fetchall()
        self.conn.commit()
        self.conn.close()
        return self.result

    def __add_hash(self, url):
        url_hash = hashlib.sha512((url + self.salt).encode("utf-8")).hexdigest()
        self.__db_helper(f"INSERT INTO urls_cash(url, hash) VALUES('{url}','{url_hash}')")
        

    def __select(self, url):
        url_cash = self.__db_helper(f"SELECT hash FROM urls_cash WHERE url = '{url}'")
        return url_cash

    def start(self, url):
        self.url = self.__select(url)
        if  self.url == []:
            self.__add_hash(url)
        else:
            return self.url[0][0]



main = Web_cash()


print(main.start("https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html"))
print(main.start("https://www.google.com/"))


# 2
class Web_cash_optimzae():
    def __init__(self):
        self.salt = "f2fdd202e5c94d60984f77e4e2b624a1"

    def __db_helper(self, magic):
        self.conn = sqlite3.connect("urls_cash.db")
        self.curs = self.conn.cursor()
        self.result = self.curs.execute(magic).fetchall()
        self.conn.commit()
        self.conn.close()
        return self.result

    def __add_hash(self, url):
        url_hash = hashlib.sha512((url + self.salt).encode("utf-8")).hexdigest()
        self.__db_helper(f"INSERT INTO urls_cash(url, hash) VALUES('{url}','{url_hash}')")
        

    def __select(self, url):
        url_cash = self.__db_helper(f"SELECT hash FROM urls_cash WHERE url = '{url}'")
        return url_cash

    def start(self, url):
        self.url = self.__select(url)
        if  self.url == []:
            self.__add_hash(url)
        else:
            return self.url[0][0]



main = Web_cash_optimzae()


print(main.start("https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html"))
print(main.start("https://www.google.com/"))

