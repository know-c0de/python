#!/usr/bin/env python
#coding = utf-8


import urllib2
import urlparse

n = []
f = open('wangzhan.txt', "a+")

while True:
    url = f.readline()
    if not url:
        break
    xurl = urlparse.urlparse(url)
    xxurl = urlparse.urlunparse(xurl)
    n.append(xxurl)
f.close()

for i in n:
    try:
        page = urllib2.urlopen(i, timeout=10).read()
    except Exception as e:
        continue
