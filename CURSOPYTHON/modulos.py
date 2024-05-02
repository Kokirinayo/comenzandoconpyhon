#Modulos la forma que tenemos de importar de otros ficheros funciones #si le pones Sum_three_numbers as three , 
# no es necesario poner la frase entera, luego pones three(8,23,22)

from funciones import Sum_numbers, Sum_three_numbers as patata              # si queremos que el nombre sea mas coro ponemos un ass despus de sum three numbrs

Sum_numbers(5,7,12)
#Sum_three_numbers(8, 23 ,22)
patata(1,2,4)


#para que te deje importar el fichero es iportante copiar el mismo nombre y que no tenga "RESULTADOS EN LA PAGINA DE FUNCIONES"

from listas import my_list

print(my_list)