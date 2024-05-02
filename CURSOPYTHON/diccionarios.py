#DICCIONARIOS

my_list = {'a', 'b'}  #ESTA NO ES LA ESTRUCTURA CORRECTA QUE U TILIZAMOS EN LOS DICCIONARIOS POR ESO NOS DICE QUE ES UN SET

print(type(my_list))  #nos dira que es un SET

my_dict = {'Nombre' : 'Nicolas', 'Apellido' : 'Gonzalez', 'Apodo' : 'Nikoras' }  #ESTA ES LA ESTRUCTURA CORRECTA DE UN DICCIONARIO

print(type(my_dict)) #nos dira que es un diccionario



print(my_dict['Apodo'])

print(my_dict['Nombre']) #EN LAS LISTAS TENIAMOS COSAS DEL 0 AL ...  PERO EN LOS DICCIONARIOS lo guardamos como strigs

print(my_dict['Apellido'])

#FUNCIONES DE LOS DICCIONARIOS

print(my_dict.keys())#IMPRIME TODAS LA LLAVES {}

print(my_dict.values())  #IMPRIME LO CONTRARIO OSEA "LA RESPUESTA"

#COMO HEMOS VISTO EN LAS TUPLAS LOS DICCIONARIOS TAMBIEN LOS PODEMOS MODICIAR


my_dict = list(my_dict)
print(my_dict)  #SOLO SALEN LAS LLAVES NO LAS RESPUESTAS A  LAS LLAVES

my_dict = tuple(my_dict)

print(my_dict)