#!/usr/bin/env python
#coding=utf-8

import urllib2

n = [] 
urls = []

while True:
    with open('wangzhan.txt', "a+") as url:
        urls = url.readline()
        if not urls.startswith("http://"):
            break
        n.append(urls)
    for i in n:
        while True:
            response = urllib2.urlopen(i).read()
            print response
        else:
            print 'Error'
