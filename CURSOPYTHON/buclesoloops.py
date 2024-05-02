#bucles o loops el bucle mas comun es WHILE ESTO SE REPETIRA HASTA QUE NO SE CUMPLA LA CONDICION

#numero = 0
#while numero < 10
#print(numero)

#numero es menor que 10 si, por lo tanto pondra un 0 INFINITIVAMENTE


numero = 0
while numero < 10:
    numero += 1
print(numero)
if numero == 5:
    print('es menor que 5')
    
print('Hola mundo')

lista = [1,2.5,35,2,5,6,7]
for number in lista:
    print(number)

lista = ['a','s','l','m']
for character in lista:
    print(character)


lista = ['a','s','l','m']
for character in range(48):   #IMPRIME LA CANTIDAD DE VECES QUE QUIERES HASTA EL NUEMERO QUE DIGAS
    print(character)
if character == 5:
    print('es un 5')
break