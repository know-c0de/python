#!/usr/bin/env python
#coding=utf-8

def sum(a=1,b=100):
    result = 0
    i = a 
    while i <= b:
        result += i
        i += 1
    return result
    
print sum()
