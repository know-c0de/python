#!/usr/bin/env python2.7.6
#coding=utf-8
#
#Copyright 2013 the Melange authors.
#
#You may obtain a copy at
#
# https://github.com/know_c0de/python/
#
#Author:know_c0de
#Time:2013.11.14
#E-mail:xxxxxxxx@qq.com
#Unless required by applicable law or agreed to in writing, software
#distributed under the license is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
#See the license for the specific language governing permissions and
#limitations under the license.


import urllib2
response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
print html
