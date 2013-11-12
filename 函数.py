#!/usr/bin/env python
#coding=utf-8

def get_even(n):
    sum = 0
    
    for x in range(n):
        if x % 2 is 0:
            sum += x
        return sum

print get_even(10)
print get_even(11)
print get_even(100)
print get_even(500)
