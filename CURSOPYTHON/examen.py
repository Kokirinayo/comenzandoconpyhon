#En una 'lista' de números, retorna el segundo número más grande.
# Ejemplo: [5,7,2,7,9,4,8]
#Respuesta: 8

lista = [5,7,2,7,9,4,8]

lista.sort()
print(lista[-2])


#CONVERSOR DE TIEMPO #2
#Crea una función que reciba días, horas, minutos y segundos 
#(como 'list') y retorne su resultado en milisegundos.


def militime(day = 0 , hour = 0 , minute = 0, second = 0):

        final_time = 0 
        hour =+ day * 24
        minute =+ hour * 60
        second =+ minute * 60
        final_time = second * 1000
        
        print(final_time)
militime(2,33,3,12)


#FIZZBUZZ #3
#Escribe una función que muestre por consola los números 
#de 1 a 100 (ambos incluidos y con un salto de línea entre
#cada impresión), sustituyendo los siguientes:
#- Múltiplos de 3 por la palabra "fizz".
#Múltiplos de 5 por la palabra "buzz".
#- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"


#numero es menor que 10 si, por lo tanto pondra un 0 INFINITIVAMENTE


def bizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print('bizzbuzz')
        elif a % 3 == 0:
            print('fizz')
        elif a % 5 == 0:
            print('buzz')
            
            
        else:
          print(a)
          
bizzbuzz()