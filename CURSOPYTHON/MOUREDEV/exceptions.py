#excepcions

numberOne = 5
numberTwo = 1
#numberTwo = '1' #si quitamos el # si saldria un error por que no podemos poner '' con numeros


#try except else

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except: #except es neesaro ponerlo si hay un try
    print('Se ha produido un error')
else: #else es opcional
    print('La ejecución contunia correctamente')
finally:  #se ejecuta siempre pase lo que pase
    print('La ejecución continua')
    
#excepiones por tipo

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except Exception as exception:
    print('exception')
