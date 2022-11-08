"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from operator import le


users_dict = {"Sergery": (123, False), "Misha": (321, True), "Kolya": (222, True), "Vova": (111, False)}
users_list = [("Sergery", 123, False), ("Misha", 321, True), ("Kolya", 222, True), ("Vova", 111, False)]


def check_1(info):                                                           # O(1)
    user = users_dict[info[0]]                                               # O(1)
    if not (user[0] == info[1]):                                             # O(1) + O(1) + O(1) = O(1)
        print("Password is wrong")                                       # O(1)
        return      
    if not (user[1] == True):                                                # O(1)
        print("Please, activate your profile")                               # O(1)
        return
    print("Success")


person_1 = ("Misha", 321)
person_2 = ("Misha", 999)
person_3 = ("Vova", 111)
check_1(person_1)
check_1(person_2)
check_1(person_3)

print()

def check_2(info):  #O(n)
    for i in range(len(users_list)):        #O(n)
        if info[0] == users_list[i][0]:     #O(1)
            if info[1] != users_list[i][1]: #O(1)
                print("Password is wrong!")
                break
            if users_list[i][2] != True: #O(1)
                print("Please, activate your profile")
                break
            print("Success")
            break

person1_ = ("Misha", 321)
person2_ = ("Misha", 999)
person3_ = ("Vova", 111)             

check_2(person1_)
check_2(person2_)
check_2(person3_)

#Считаю, что решение check_1 более эффективно. Т.к. требует меньше вычислений без необходимости 
# перебора всего массива данных, лишь обратиться по ключу. Так же код более компактный.