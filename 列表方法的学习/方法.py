# 列表切片: 切片后一位不包括该下标，可以大于列表长度
l1 = [1, 2, 3, 4]
print(l1[0:2])
# 列表元素反转,改变原有列表
print(l1.reverse())
print(l1)


l = [1, 2, 3, 4]
# 拼接两个列表：extend(param):Extend list by appending elements from the iterable.
m = [5, 6, 7, 8]
l.extend(m)
print(l)
l.extend(range(5, 9))
print(l)
# 列表不能除法
# print(l/2)
# 列表的乘法就是几个列表相加
print(l*2)
class_name = ['1班', '2班', '3班', '5班', '4班']
class_name.sort(key=lambda x:x[0], reverse=True)
print('yao' , class_name)
class_name = ['6', '7', '1', '2', '8', '4', '10', '5', '3']
# 使用sort方法会改变列表本身，没有返回值, reverse默认为False，进行升序排列
class_name.sort(key=lambda x:int(x))
print(class_name)
# 获取列表中元素下标: Return first index of value.
class_name = ['6', '7', '1', '2', '8', '4', '10', '5', '3', '3']
print('获取列表中元素下标', class_name.index('3'))
# 列表不能直接转换为字典
# print(dict(class_name))
# for i, v in dict(class_name):

# 排序
l = [3,5,256,72,23,6,432,6562,3,4]
l.sort(reverse=True) # 改变l本身
print(l)

for i in range(5,1,-1):
    print(i)

# 求列表元素在列表中的下标
l.index(5)
