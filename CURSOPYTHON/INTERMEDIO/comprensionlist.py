#comprension #en el captulo llamdo bucles #segun el rango llegara hasta el punto indicado esta explicado

normal_list  =  [1,2,3,4,5,6,7,8,9,10]

print(normal_list)

comprehension_list = [i for i in range(9)]

def sum_number(number):
    number += "_"
    return number

comprehension_list = [sum_number (i) for i in range(9)]
comprehension_list = [i * i for i in range(9)]
print(comprehension_list)              #borrar para que funcione el _ de las letras suscribete

my_string = 'subscribete'
comprehension_list = [sum_number(i) for i in my_string]
print(comprehension_list)

