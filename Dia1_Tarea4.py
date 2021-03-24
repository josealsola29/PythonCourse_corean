# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:00:06 2020

@author: JALSOLA
"""

def Multip(*num):
    sum = 0
    for i in num:
        sum = sum + i
    return print(sum)

Multip(10,51,13,42,62,8)
