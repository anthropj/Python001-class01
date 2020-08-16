# 扁平序列：str
# 容易序列: list, tuple, dictionary, collections.deque
# 可变序列: list, dictionary, collecitons.deque
# 不可变序列: str, tuple


def imitate_map(func_obj, iterable):
    for item in iterable:
        yield func_obj(item)


import time

def timer(func):
    def calculate_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        return time.time()-start
    return calculate_time

@timer    
def func(a):
    for _ in range(a):
        time.sleep(0.1)

print(func(10))