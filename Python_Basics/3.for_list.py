#!/usr/bin/env python
# coding=utf-8
#3.1遍历整个列表
mags = ['alice', 'david','carolina']
for mag in mags:
    print(mag)

##3.1.1
for mag in mags:
    print(mag.title())
print("I can't wait t osee your next trick")


#3.1.2
#range(x, y, z = 1): x, x + z, ....,  x + w(x + w < y);
for value in range(1, 5):
    print(value)
nums = list(range(1, 6))
print(nums)

nums  =  list(range(1, 10, 2))
print(nums)

#3.1.3 列表的统计计算
didits = [1, 2,3, 4,5,  6 ]
print("min : "  + str(min(didits)) + " max : " + str(max(didits)) +  " sum  :" + str(sum(didits)))

#3.1.4
nums = [value * 2 for value in range(1, 11)]
print(nums)
#3.1.5切片
players = ['charles', 'martina', 'michael', 'florence',  'eli']
print(players)
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[:])
print(players[-3:])
print(players[: - 1])

myplayers = players[:]#两个列表
friendplayers = players#指向一个列表
print(myplayers)
print(friendplayers)
myplayers.append("appendNum")
print(players)
print(myplayers)
friendplayers.append("appendNum")
print(players)
print(friendplayers)
