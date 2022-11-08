from memory_profiler import memory_usage, profile
import time

def func_analize(func):
    print(func.__name__)
    def decorate(*args):
        memory1 = memory_usage()
        time1= time.perf_counter()
        my_func = func(*args)
        time2=time.perf_counter()
        memory2 = memory_usage()
        print("Time:", time2-time1, "Memroy: ", memory2[0]-memory1[0])
        return my_func
    return decorate

def class_analiz(func):
    def decoration(**kwargs):
        print("\n")
        print(func.__name__ ,"before", memory_usage())
        a = func(**kwargs)
        print(func.__name__ ,"after", memory_usage(), "\n")
        return a
    return decoration