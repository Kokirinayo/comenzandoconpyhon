#STRINGS 

mi_first_string = "mi string con comillas dobles "

mi_second_string = 'mi string con comillas simples'

#print(mi_first_string, mi_second_string)
#print('esto es un texto de una variable ' + mi_first_string + ' '+ mi_second_string) 

#LA FORMA CORRECTA SERIA LA SIGUIENTE PUES LA ANTEIOR ES PESADA Y AUTOINTITIVA:

print(f'esto es un texto de una variable {mi_second_string} patata con patatas')


other_string = 'hola'

a,b,c,d = other_string

print(d)
print(b)
print(c)

print(f'{a}{b}{c}{d}') #todo junto

print(mi_first_string.upper())   #TE LO IMPRIME EN MAYUSCULAS TOT0

print(mi_first_string.capitalize())  #LA PRIMERA LETRA EN MAYUSCULAS EL RESTO EN MINUSCULAS
print(mi_first_string.lower())    #PONE TO EN MINUSCULAS
print(len(mi_first_string))       #CUENTA LA CANTIDAD DE CARACTERES QUE HAY
print(mi_first_string.find('r'))   #LO UTILIZAMOS PARA SABER EN QUE POSICION ESTA LA LETRA QUE QUEREMOS
print(mi_first_string.count('r'))  #CUENTA LA CANTIDAD DE CARACTERES QUE HAY EN UNA VARIABLE
print(mi_first_string.upper().isupper())  #PREGUNTA SI TODO ESTA HECHO EN MAYUSCULAS
print(mi_first_string.lower().isupper())
 