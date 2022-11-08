"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from func_analize import func_analize
from memory_profiler import profile

def recursive(n):
    if len(str(n)) == 1:
        return n % 10
    return f"{n % 10}{recursive(n // 10)}"

print(recursive(123456))



@profile
def func_helper(args):
    def recursive(arg):
        if len(str(arg)) == 1:
            return arg % 10
        return f"{arg % 10}{recursive(arg // 10)}"
    return recursive(args)

print(func_helper(123456))
