# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:25:33 2020

@author: JALSOLA
"""
def hola_amigos(nombre, anos, hombre=True):
    s = ('Hola. My name is %s and My name age is %d' %(nombre, anos))

    if hombre:
        a = " \n\nHe is a man"
    else:
        a = " \n\nShe is a women"
    return s+a

f = open(r'C:\Users\jalsola\Desktop\CursoPython_Tareas\Dia1_Tarea2_File.txt', 'w')
f.write(hola_amigos("Jose", 23)) 
f.close()