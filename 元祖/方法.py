d = (134, 214, 0, 255)
print(type(d[0:2]))
print(d[0:2]==(134,214))
print(max(d))
d = ('212','dsfds','23fcwf')
print(max(d))
d = 'qwewtew'
print(tuple(d))

a  = {1:1,2:2,3:3}
del a[1]
print(type(a[2]))
print(type(str(a)))

try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
        print(2/0)
    except Exception as e:
        print(e)
    finally:
        print("关闭文件")
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")