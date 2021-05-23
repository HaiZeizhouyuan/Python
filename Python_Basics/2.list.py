#!/usr/bin/env python
# coding=utf-8

#list:[]

bicycles  = ['trek', 'cannodale', 'redline', 'speciakixrdd']
print(bicycles)
#下标正数： 0，1，2，... ,   n - 1; 到着数： -1,   -2,  ....,  n
print(bicycles[0].title())
print(bicycles[-1])

motorcycles = ['honda',  'yamaha', 'suzyki']
print(motorcycles)
## 修改
motorcycles[0] = 'ducati'
print(motorcycles)

##末尾添加append(str)
motorcycles = ['honda',   'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print("=============")
##在列表下标x处添加insert(n, str)
motorcycles = ['honda', 'yamaha', 'suzuhi']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)
print("====================")
## 删除del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
##删除pop(x = n - 1),将末尾元素弹出，返回弹出的值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
pop_motorcycles = motorcycles.pop()
print(motorcycles)
print(pop_motorcycles)
motorcycles.pop(0)
print(motorcycles)

##不知道要删除的元素的下标时， 用remove(str), 删除第一个str
day = ['mon', 'tue', 'wed', 'thu', 'fri']
print(day)
day.remove('wed')
print(day)

##sort()
day = ['mon', 'tue', 'wed', 'thu', 'fri']
print(day)
day.sort()
print(day)
day.sort(reverse=True)
print(day)

##sorted(str),  返回排序后的列表， 但本列表顺序不变
num  =  [1, 4, 7,  2,   0,  5]
print(num)
num2 = sorted(num)
print(num2)
print(num)
print("\n")
##reverse(), 反转列表
print(day)
day.reverse()
print(day)

#len， 确定列表长度
l = len(day)
print(l)

