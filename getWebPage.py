#!/usr/bin/env python
#coding=utf-8


import urllib2
import sys

url = []
data = []


def getWebPageContent(url):
    with urllib2.urlopen(url) as webpage:
        data = webpage.read()
    return data

if url == sys.argv[1]:
    content = data
    con = getWebPageContent()
    con.feed(content)
    print content
    if not url.startswith("http://"):
        url = "http://"+url
else:
    print 'Usage:%s url' % sys.argv[0]


if __name__ == '__main__':
    getWebPageContent(url)
