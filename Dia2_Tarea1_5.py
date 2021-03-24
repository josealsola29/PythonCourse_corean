# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 08:50:53 2020

@author: JALSOLA
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def remainder(a,b):
    return a%b

def inputVal():
    print("Ingresa el valor del primer número: ")
    n1=int(input())
    print("Ingresa el valor del operador: ")
    n2= input()
    print("Ingresa el valor del segundo número: ")
    n3= int(input())
    return n1, n2,n3


def mult_cal(a,b):
    return add(a,b), sub(a,b), multiply(a,b), divide(a,b), remainder(a,b)


def calculation(num1,num2,operator):
    if operator =="+":
        return add(num1,num2)
    elif operator =="-":
        return sub(num1,num2)
    elif operator =="*":
        return multiply(num1,num2)
    elif operator =="/":
        return divide(num1,num2)
    elif operator =="%":
        return remainder(num1,num2)
    else: 
        print("Wrong input in operator")

def start():
    n1,n2,n3 =  inputVal()
    result =    calculation(n1,n3,n2)
    result2 =   mult_cal(n1,n3)
    print("requested result : %d\n" % result)

    print("all of the results : add : %d, subtract : %d, multiply : %d, divide : %d, remainder: %d\n"% result2)
    
start()

