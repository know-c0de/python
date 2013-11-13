#!/usr/bin/env python2.7.6
#coding=utf-8
#
#Copyright 2013 Google Inc
#Time:2013.11.13
#Author:spirit
#E-mail:code.sec01@gmail.com
#
#The code is work for addition from 1 to 500
#

def get_even(n):
    sum = 0                      
    
    for x in range(n):          
        if x % 2 is 0:            
            sum += x              
        return sum                
        
print get_even(10)                
print get_even(11)                
print get_even(100)
print get_even(500)
