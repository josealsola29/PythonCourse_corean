# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:10:21 2020

@author: JALSOLA
"""

def firstPart():
    for x in range(10):
        print("Cocinando, espere...")
        if x+1==8:
            print("Error...")
            break;
        print("El número de la comida es: ",x+1)    
firstPart()


def secondPart():
    sum=0
    for x in range(10):
        if x != 5:
            sum +=x
            print(x)
    print('La suma es: ',sum)
secondPart()


def thirdPart():
    animal_list=['dog','cow','pig','cat','rabbit']
    position = animal_list.index('cat')
    print('cat\'s position is',position+1)
thirdPart()   