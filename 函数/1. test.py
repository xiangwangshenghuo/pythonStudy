def fun():
    try:
        a = 1/0
        return a
    except:
        print(0)

print(fun())