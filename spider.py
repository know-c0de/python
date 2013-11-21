#!/usr/bin/env python
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

for x in n:
    match = url_legal_pattern.search(x)
    if not match:
        print 'The url is wrong'
    else:
        break

for i in n:
    try:
        response = urllib2.urlopen(i).read()
        print response
    except:
        continue
