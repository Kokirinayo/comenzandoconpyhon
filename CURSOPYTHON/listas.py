#LISTAS  ES UN  TIPO DE VARIABLE

my_list = ['Python',55,False,'Hola mundo']  #no puedes poner cualquier cosa tipo oeoruoweruow porque ese valor no existe

print(type(my_list))

print(my_list)  #AQUI IMPRIJMIRA LA LISTA ENTERA
print(my_list[1])  #IMPRIME EL 55 POR QUE EN PROGRAMACION SE EMPIEZA A CONTAR DESDE 0 , ES DECIR Python seria u 0, 55 el 1 y false el 2
print(my_list[-1])  #EMPIEZA CONTANDO POR DETRAS



#AGREGAR COSAS A LA LISTA

my_list.append(55)  #AÑADIMOS EL 55 A LA LISTA
my_list.insert(3, 'suscribanse')     #CON ESTA OPCION ESCOGEMOS DONDE QUEREMOS QUE ESTÉ EN LA LISTA OSEA ELEGIR LA PISICION
print(my_list)
my_list.remove('Hola mundo')  #LO UTILIZAMOS PARA BORRAR DE LA LISTA ALGO
print(my_list)
my_list.pop(2)
print(my_list)
print(my_list.count(55))

my_list.reverse()  #PONE LA LISTA AL REVES
print(my_list)

#my_list.clear()  #DEJA LA LISTA VACIA

