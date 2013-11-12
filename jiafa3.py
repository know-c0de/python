#!/usr/bin/env python
#coding=utf-8

num=0
for i in range(501):
    num += i
    if i < 500:
        continue
    else:
        print(num)
