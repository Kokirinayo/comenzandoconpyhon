#TUPLAS

my_tupla = (53, 'Perro', 4.5, True)

print(type(my_tupla))  #TE DIRA QUE ES UNA TUPLA

print(my_tupla[1]) 
print(my_tupla.count(53))  #PARA CONTAR CUANTOS TENEMOS
print(my_tupla.index(True))
print(my_tupla.index(4.5))

#LAS TUPLAS NO SE PUEDEN MODIFICAR, LAS LISTAS SI SE PUEDEN MODIFICAR

#PERO HECHA LA LEY HECHA LA TRAMPA, SI HACEMO ESTO SI PODREMOS

my_tupla = list(my_tupla)
print(type(my_tupla))  #ASI CONVERTIMOOS UNA TUPLA EN UNA LISTA

my_tupla.pop()
print(my_tupla) #LO CONVERTIMOS EN UNA LISTA Y LE QUITAMOS LA ULTIMA PALABRA CON POP PUESTO ARRIBA