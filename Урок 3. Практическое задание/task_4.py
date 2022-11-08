"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib, sqlite3
from uuid import uuid4



class Web_cash():
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
