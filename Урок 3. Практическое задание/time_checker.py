import time



def time_checker(func):
    def timer_func(*args):
        chek_1 = time.perf_counter()
        func(args)
        check_2 = time.perf_counter()
        result = round(check_2 - chek_1, 7)
        print(result)
        return result
    return timer_func