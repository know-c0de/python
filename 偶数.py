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
#Time:2013.11.13
#E-mail:xxxxxxxx@qq.com
#Unless required by applicable law or agreed to in writing, software
#distributed under the license is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
#See the license for the specific language governing permissions and
#limitations under the license.


def get_even(start=0, end=0):

    for x in range(start, end):
        if x % 2 is 0:
            print x

print get_even(100, 200)
