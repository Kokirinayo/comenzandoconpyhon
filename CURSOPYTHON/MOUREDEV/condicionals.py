#condicionales

#si se cumple una condicion yo ejecuto lo que tu me digas si esta dentro de esa condicio


#primero comprueba if, luego elif, luego else
#variable  
my_condition = False

if my_condition:
    print('Se ejecuta la condicion del if')
    
my_condition = 5 * 3

if my_condition == 10:
    print('Se ejecuta la condicion del segundo if')
    
if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')   
elif my_condition == 1: 
    print('Es igual a 1')
else:
    print('Es menor o igual que 10 o mayor o igual que 20')

print('La ejecución continúa')

my_string = ''

if not my_string:
    print('Mi cadena de texto es vacía')
    
if my_string == 'Mi cadena de textoooo':
    print('Estas cadenas de texto coinciden')

