def hola_amigos(nombre, anos, hombre=True):
    print ('Hola. My name is %s and My age is %d\n' %(nombre,anos))
    
    if hombre:
        print ("He is a man")
    else:
        print("She is a women")
    
    
hola_amigos("José", 23,True)
