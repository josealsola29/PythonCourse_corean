# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:55:03 2020

@author: JALSOLA
"""

def calculation(num1,num2,operator):
    if operator =="+":
        return num1+num2
    if operator =="-":
        return num1-num2
    if operator =="*":
        return num1*num2
    if operator =="/":
        return num1/num2
    if operator =="%":
        return num1%num2

print (calculation(1,5,"/"))