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

Это файл для третьего скрипта
"""

"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import sqlite3
import hashlib
from func_analize import class_analiz

# 1
@class_analiz
class vk():
    def __init__(self):
        self.__conn = sqlite3.connect("accounts.db")
        self.__cur = self.__conn.cursor()
        self.__sold = "46cfa22aed794a9998bb8b0baa39ffce"

    def __insert_db(self, login, password):
        self.__cur.execute(f"INSERT INTO autorization (name, password) VALUES ('{login}', '{password}')")
        self.__conn.commit()

    def _hash_func(self, password):
        hash_paswword = str(hashlib.sha256((password + self.__sold).encode("utf-8")).hexdigest())
        return hash_paswword

    def __select_db(self, login):
        login_ = self.__cur.execute(f"SELECT name, password FROM autorization WHERE name = '{login}'")
        self.__conn.commit()
        try:
            return login_.fetchall()[0][1]
        except:
            return None

    def login(self, login, password):
        account = self.__select_db(login)
        if account != None:
            visti_hash_pass = self._hash_func(password)
            if visti_hash_pass == account:
                print("Log In")
            else:
                print("Wrong password")
        else:
            print("Account not found")

    def create_account(self, login, password):
        check = self.__select_db(login)
        if check == None:
            hash_pass = self._hash_func(password)
            self.__insert_db(login, hash_pass)
            print("Account created!")
        else:
            print("Account already exist")
            

main = vk()
main.create_account("Misha", "pmpm")
main.login("Pasha", "secret")
main.login("Pasha", "wrong")
print(main._hash_func("Misha"))

# 2
@class_analiz
class vk_optimzae():
    __slots__ = ("__conn", "__cur", "__sold", "hash_paswword", "login_", "account", "visti_hash_pass")
    def __init__(self):
        self.__conn = sqlite3.connect("accounts.db")
        self.__cur = self.__conn.cursor()
        self.__sold = "46cfa22aed794a9998bb8b0baa39ffce"

    def __insert_db(self, login, password):
        self.__cur.execute(f"INSERT INTO autorization (name, password) VALUES ('{login}', '{password}')")
        self.__conn.commit()

    def _hash_func(self, password):
        hash_paswword = str(hashlib.sha256((password + self.__sold).encode("utf-8")).hexdigest())
        return hash_paswword

    def __select_db(self, login):
        login_ = self.__cur.execute(f"SELECT name, password FROM autorization WHERE name = '{login}'")
        self.__conn.commit()
        try:
            return login_.fetchall()[0][1]
        except:
            return None

    def login(self, login, password):
        account = self.__select_db(login)
        if account != None:
            visti_hash_pass = self._hash_func(password)
            if visti_hash_pass == account:
                print("Log In")
            else:
                print("Wrong password")
        else:
            print("Account not found")

    def create_account(self, login, password):
        check = self.__select_db(login)
        if check == None:
            hash_pass = self._hash_func(password)
            self.__insert_db(login, hash_pass)
            print("Account created!")
        else:
            print("Account already exist")
            

main = vk_optimzae()
main.create_account("Misha", "pmpm")
main.login("Pasha", "secret")
main.login("Pasha", "wrong")
print(main._hash_func("Misha"))

