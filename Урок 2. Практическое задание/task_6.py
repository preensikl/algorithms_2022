"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint

counter = 0
def question(numb):
    global counter
    if counter == 10:
        print("Game over")
        return
    counter += 1
    answer = int(input("Write your suppose: "))
    if answer == numb:
        print(numb)
        return
    if answer > numb:
        print("Less")
    else:
        print("More")
    return question(numb)

question(randint(0, 100))