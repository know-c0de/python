#! /usr/bin/env python2.7.5
#coding=utf-8

import urllib2
import re

n = []
files = open('wangzhan.txt', "a+")

url_legal_pattern = re.compile('http://.*')

while True:
    f = files.readline()
    if not f:
        break
    n.append(f)
files.close()

match = url_legal_pattern.search(n)
if not match:
    print 'The url is wrong'
    return -1

for i in n:
    try:
        response = urllib2.urlopen(i).read()
        print response
    except:
        continue
