"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class Steck():                          # O(n)
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
            self.getter = self.lst[-1][-1]      # O(n)
            self.__delete()
            return self.getter

    def __delete(self):
        self.lst[-1].remove(self.getter)
        if self.lst[-1] == []:
            del self.lst[-1]

    
    def __str__(self):
        return f"{self.lst}"



if __name__ == "__main__":
    test = Steck(size=2)
    for i in range(7):
        test.app(i)
    test.app("key")
    test.app({"Misha": 25})
    test.app(["mimimi"])
    for i in range(8, 15):
        test.app(i)

    print(test)
    print(test.get())
    print(test.get())
    print(test.get())
    a = test.get()
    print("a", a)
