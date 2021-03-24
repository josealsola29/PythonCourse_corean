# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:10:00 2020

@author: JALSOLA
"""
def inputVal(num1, operador, num2):
    return num1 + operador + num2 

print("Ingresa el valor del primer número: ")
a=input()
print("Ingresa el valor del operador: ")
c= input()
print("Ingresa el valor del segundo número: ")
b= input()
print (inputVal(a, c, b))