#!/usr/bin/env python2.7.6
#coding=utf-8
#
# Copyright 2013 the Melange authors.
#
# You may obtain a copy at
#
#  https://github.com/know-c0de/python/blob/master/函数.py
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""It's work for addition from 1 to 500"""

__authors__ = [
  '"spirit" <code.sec01@gmail.com>'
]

def get_even(n):
    sum=0
    """定义函数 初始化变量sum"""

    for x in range(n):
        if x % 2 is 0:              
            sum += x
        return sum
    """执行循环"""

print get_even(10)
print get_even(11)
print get_even(100)
print get_even(500)
    """执行输出"""
