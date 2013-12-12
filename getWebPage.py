#!/usr/bin/env python
#coding=utf-8


import urllib2
import sys


def getWebPageContent(url):
    with urllib2.urlopen(url) as webpage:
        data = webpage.read()
    return data

    if sys.argv[1] == url:
        content = data
        con = getWebPageContent()
        con.feed(content)
        print content
        if not url.startswith("http://"):
            url = "http:/"+url
    else:
        print 'Usage:%s url' % sys.argv[0]
