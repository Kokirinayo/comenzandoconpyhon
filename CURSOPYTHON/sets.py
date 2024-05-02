#SETS

my_set = {}
print(type(my_set))    #LO DEFINE COMO UN DICIONARIO

my_set = {'Python', 'Javascript', 'C++'}
print(type(my_set))   #LO DEFINE COMO UN SET

print(my_set)  #VEMOS QUE IMPRIME CON ORDEN ALATORIO
print(my_set)  #EN LOS SETS NO HAY ORDEN POR ESO NO PODEMOS QUE PIDAN IMPRIMIR ALGO EN CONCRETO


#EN LOS SETS NO ACEPTAN COSAS REPETIDAS

my_set.add('C++')
print(my_set) #COMO PODEMOS OBSERVAR NO LO PONE REPETIDO

my_set.add('C#')
print(my_set)  #SI AÑADIMOS ALGO QUE NO ESTA EN LA LISTA SI LO AÑADE

#ESTO SON FUNCIONES LO DE ABAJO ESCRITO

my_set_0 = {'Python', 'Javascript', 'C++'}

my_set.difference_update(my_set_0) #Te dara la diferencia entre uno y otro que en este caso es C# PORQUE MY SET 0 O TIENE EÑL C#


print(my_set)  

