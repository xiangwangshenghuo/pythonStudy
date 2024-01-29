# 通用装饰器
import time 

def deco(func):
    def wrapped(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return func(*args, **kwargs)
    return wrapped


@deco
def test(n):
    sum = 0
    for i in range(n):
        sum += i
    print('.....')
    return sum
    print('******')
print(test(100000))

















