#!/usr/bin/env python
# coding=utf-8

print("Hello world")

#变量
message = "my name is zy"
print(message)

#字符窜
##对于字符串单引号和双引号都可以
name = 'zy'
print(name)

##title()来修改字符串的每个单词的首字母的大小写
name = 'add lovelace'
print(name.title())
##upper()全部大些
print("upper()  : " + name.upper())
##lower()全部小写
print("lower() :" + name.lower())
##字符串的拼接用'+'
##删除末尾空白用rstrip(), 字符串开头空格用lstrip(), 剔除两端的空白用strip()
favorite_language = ' python i like '
print(favorite_language + 'end')
word =  favorite_language.rstrip()
print(word + 'end')
print(favorite_language + 'end')
print(favorite_language.lstrip())
print("i like world, my name is 'zy'")


#数字
print(2 + 3)
print(10 - 3)
print(2 * 3)
print(3 / 2)#python3: 1.5,   pyton2: 1
##pyton2
print(3/2)#1
print(3.0 / 2)#1.5
print(3/2.0)#1.5
print(3.0/ 2.0)#1.5
## 3^2
print(3 ** 2)
##浮点数的相乘， 小数点位数不确定
print(0.1 * 0.1)
print(0.2 * 0.4)

##用str避免类型错误
#error : print("Happy" + 25 + "rd Birthday!")
print("Happy " + str(18) + " Birthday")


