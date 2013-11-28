#!/usr/bin/env python
#coding = utf-8

import urllib2
import urlparse


class Url:
    global url

    def __enter__(url):
        with open('wangzhan.txt', 'r') as url:
            print ('the url is:', url)
        return

    def __exit__(url):
        xurl = urlparse.urlparse(url)
        xxurl = urlparse.urlunparse(xurl)
        url.append(xxurl)
        with Exception as e:
            if url != urllib2.urlopen(url, timeout=10).read():
                print e
            print
        return


def get_url(html):
    with get_url(html) as url:
        html = urllib2.urlopen(url).read()
    print html
