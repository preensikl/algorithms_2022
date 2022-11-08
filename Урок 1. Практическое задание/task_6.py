"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from task_5 import Steck

class Quests():
    def __init__(self, **kwargs):
        self.sizes = kwargs["sizes"]
        self.shared_line = Steck(size = self.sizes)
        self.modification_line = Steck(size = self.sizes)
        self.done_line = Steck(size = self.sizes)

    def add_shared(self, arg):
        return self.shared_line.app(arg)

    def shared_to_done(self):
        return self.done_line.app(self.shared_line.get())

    def shared_to_modification(self):
        return self.modification_line.app(self.shared_line.get())

    def done_to_modification(self):
        return self.modification_line.app(self.done_line.get())
    
    def modification_to_done(self):
        return self.done_line.app(self.modification_line.get())


    def __str__(self):
        return f"""Shared: {self.shared_line} \nModification: {self.modification_line} \nDone:{self.done_line}"""

    
PayPall = Quests(sizes=3)

PayPall.add_shared("Create architecture")
PayPall.add_shared("Create back end")
PayPall.add_shared("Create front end")
PayPall.add_shared("Create UX/UI")
PayPall.add_shared("Connect back and front")
PayPall.add_shared("Test project")
PayPall.add_shared("Relize")

PayPall.shared_to_modification()
PayPall.shared_to_done()
PayPall.modification_to_done


print(PayPall)

