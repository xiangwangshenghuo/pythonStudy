# coding:utf-8

users = ['bobby1', 'bobby2', 'bobby3', 'bobby1', 'bobby2', 'bobby2' ]
user_dict = {}
for user in users:
    user_dict.setdefault(user, 0) # 代码简洁、且性能高
    user_dict[user] +=1
print(user_dict)
if 'bobby1' in user_dict:
    print('dsaas')

# 1. 取键：keys()方法

#spyder

bb={'人才/可怕':23,'伏地魔&波特':'army','哈哈哈,人才,回合':'hhh'}

for ii in bb.keys():

    print(ii)

#输出：

#人才/可怕

#伏地魔&波特

#哈哈哈,人才,回合

# 2. 取值：values()方法

for jj in bb.values():

    print(jj)

#输出

#23

#army

#hhh

# 3. 取键值对：items()方法

for kk,vv in bb.items():

    print(kk, vv)

#输出

#人才/可怕 23

#伏地魔&波特 army

#哈哈哈,人才,回合 hhh

# 4. 单独的keys

xx = bb.keys()

print(xx) #输出：dict_keys(['人才/可怕', '伏地魔&波特', '哈哈哈,人才,回合'])

if '人才/可怕' in bb.keys():

    print(bb['人才/可怕'])

#输出该键对应的值：23

# 5. 字典的get方法 —— 获取指定键的值，如果键不存在，则返回第二个参数（默认值），不修改原字典

c = bb.get('人才','没有找到该键')

print(c)

cc = bb.get('人才/可怕','没有找到该键')

print(cc)


# 6. 字典的pop方法 ——获取该键对应的值，并且删除字典中的这一键值对，如果该键不存在，则返回第二个参数（默认值）

d = bb.pop('人才','pop失败') # pop失败

print(d)

dd = bb.pop('人才/可怕','pop失败') #pop成功，且删除该键对应的键值对

print(dd)

print(bb) #原字典已变化


# 7. 字典的popitem方法 ——随机返回一个键值对，随机是因为字典时无序的；且删除原字典中的该键值对

key, value = bb.popitem()

print(key, ':', value) #取出的键值对

print(bb) #变化之后的字典
# 8 .清除所有元素
bb.clear()
print(bb)

