# coding:utf-8
# 删除方法remove
class_name = ['6', '7', '1', '3','2', '8', '4', '10', '5', '3', '3']
for i in class_name:
    print(i)
    if i == '3':
        # 在遍历列表时，使用remove删除元素，那么该删除的元素右边的元素会向左移动一位，
        # 这样就会出现，删除元素右边的第一元素遍历不到，因为列表遍历是按照下标进行的
        class_name.remove(i)
    print(class_name)

# 如何解决这个问题呢：倒序删除的方法！
def test(data):
    for i in data[::]:
        if i ==7:
            data.remove(i)
    return data


data = [1, 2, 3,5,6,7,7,8,7,6,5,4,4,3]
print(data[1:-1])
print(data[1:-1:-1])
print(data[::])
print(data[::-1])
# print(test(data))
for i in data[:]:
    if i == 7:
        data.remove(i)
print(data)
