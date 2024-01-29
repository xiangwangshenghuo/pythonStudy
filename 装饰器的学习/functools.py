# coding:utf-8
def login_required(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper


def itcast():
    """itcasr python"""
    pass

print(itcast.__name__) # itcast
print(itcast.__doc__)  # itcasr python


@login_required
def itcast():
    """itcasr python"""
    pass
# itcast -> wrapper
print(itcast.__name__) # wrapper
print(itcast.__doc__)  # None

import functools
def login_required(func):
    @functools.wraps(func)  # @functools.wraps(func) 会把wrapper恢复为原来的函数的属性
    def wrapper(*args, **kwargs):
        pass
    return wrapper


@login_required
def itcast():
    """itcasr python"""
    pass
# itcast -> wrapper
print(itcast.__name__) # itcast
print(itcast.__doc__)  # # itcasr python