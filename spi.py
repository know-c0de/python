#! /usr/bin/env python2.7.5
#coding=utf-8

import urllib2
import os

n = []
files = open('wangzhan.txt', "a+")

while True:
    f = files.readline()
    if not f:
        break
    n.append(f)
files.close()

for i in n:
    while True:
        response = urllib2.urlopen(i).read()
        print response
    else:
        print 'Error'
