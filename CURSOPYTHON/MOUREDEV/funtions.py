#funciones DEF
# PARA DEFINIR UNA FUNCION TODO LO QUE TENGAMOS  TABULADO HACIA LA DERECHA DENTRO O DESPUES DE CREAR LA FUNCION
# TABULADO

def my_function ():  
    print('Esto es una funcion')
    
my_function ()
my_function ()
my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)
    
sum_two_values(5, 7)  
sum_two_values(4345, 73343)
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname, city):
    print(f'{name} {surname} {city}')
print_name(surname ='Moure',name = 'Brais', city ='villena')

def print_name_with_default (name, surname, city, alias = 'Sin alias'):
    print(f'{name}{surname}{city}{alias}')
    
print_name_with_default('Brais ', 'Moure ', 'Villena ', 'MoureDev ')
print_name_with_default('Brais ', 'Moure ', 'MoureDev ')

def print_upper_texts(*texts):
  for text in texts:
    print(text.upper()) 
    
    
print_upper_texts('Hola', 'Python', 'Nayo')
print_upper_texts('Hola')  #TODO EN MAYUSUCLA CON UPPER

lore