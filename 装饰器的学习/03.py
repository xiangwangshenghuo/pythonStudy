def dec(fn):
    print(fn)
    return 1

print('dec',dec)

@dec
def foo():
    print('foo')


print('foo',foo)


def foo1():
    print('fool')


foo1 = dec(foo1)
print('fool',foo1)
