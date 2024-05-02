#my dict 

my_dict = dict()
my_other_dict =  {}

print(my_dict)
print(type(my_dict))
print(type(my_other_dict))



my_dict = {
    'Nombre':'Noemi',
    'Apellido':'Lopez',
    'Edad':32,
    'Apodo':'Nayo',
    'Lenguaje':{'Python','Java','Swit'},
    1:1.35
}

print(my_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Nayo'
print(my_dict)

my_dict['Nombre'] = 'Pepo'

print(my_dict[1])

my_dict['Calle'] = 'Rambla chonga'

print(my_dict)

del(my_dict)['Calle']
print(my_dict)

print('Noemi'in my_dict)
print('Pepo'in my_dict)
print('Nayo' in my_dict)
print('Noemi'in my_other_dict)
print('Pepo'in my_other_dict)
print('Nayo' in my_other_dict)

print('Apellido'in my_dict)

#print(my_dict.clear) limpiar
#print(my_dict.copy) copiar

#print(my_dict.items

my_new_dict = my_other_dict.fromkeys(('Nombre', 1, 'Piso'))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,['Noemi','Lopez'])
print((my_new_dict))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
print(my_new_dict.values())
print((my_new_dict.values()))