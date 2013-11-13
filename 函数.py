#!/usr/bin/env python
#coding=utf-8

def get_even(n):                  #定义函数，参数
    sum = 0                       #初始化sum赋值
    
    for x in range(n):            #循环，给定x的数值范围
        if x % 2 is 0:            
            sum += x              #判断x是否为偶数，执行sum = sum + x
        return sum                

print get_even(10)                #当参数为10，输出
print get_even(11)                #当参数为11，输出
print get_even(100)
print get_even(500)
