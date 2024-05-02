# OPERADORES ARITMETICOS

print( 6 + 3)  #SUMAR
print( 6 - 3)  #RESTAR
print( 6 * 3)  #MULTIPLICAR
print( 11 / 3)  #DIVIDIR
print( 7 % 3)  #SE LE LLAMA RESTO - DIVIDE 3 ENTRE SIETE Y NO 7 ENTRE 3 
print(4 ** 3)  #EXPONENTE , SALDRIA 
print(4 * 4 * 4) #DE ESTA FORMA COMPRENDEMOS MEJOR EL 4**4
print(11 // 3)   #DIVISION DE FLOR REDONDAEA EL NUMERO Y EL DIVISION NORMAL LO DEJA 3.6666 HASTA EL INFINITO


#   LOS OPERADORES ARITMETICOS TAMBIEN FUNCIONAN CON LETRAS Y PALABRAS COMO PODEMOS OBSERVAR:

print('Hola '  +  'mundo')  #SI QUIERES QUE QUEDE SEPARADO HOLA MUNDO PON UN ESPACIO EN EL ULTIMO ' DE HOLA
print('Hola mundo ' * 6) #ASI PODEMOS MULTIPLICAR LAS PALABRAS Y FRASES QUE QUERAMOS

a = 6

print('Hola ' + str(6))   #se usaria str para usarlo como str y no como variable porque tambien podriamos usar ' 
                                    #PERO NO SERIA CORRECTO
                                    

#OPERADORES COMPARATIVOS   BOOLEANO ES AQUEL QUE PUEDE REPRESENTAR VALORES DE LOGICA BINARIA, ESTO SON 2 VALORES
#QUE NORMALMENTE REPRESENTAN FALSO  O VERDADERO .EL BOOLIANO PREGUNTA SI ALGO ES FALSA Y TE DICE SI ES VERDADERO O FALSO.a

print(4 < 8)
print(4 > 8)
print(4 == 4) #SI SOLO PUSIERAMOS UN = ESTARIAMOS  ASIGNANDO UN VALOR DICIENDO QUE 4 ES IGUAL A 8 SIN EMBARGO QUEREMOS PREGUNTAR 
              # SI 4 Y 8 SON IGIUALES O NO SON IGUALES EFECITVAMENTO NO ES IGUAL A 8 SERIA 4 ES  == 4
              
              
print(4 <= 8)  #AQUI PREGUNTAMOS SI 4 ES MENOR O IGUAL A 8
print(4 >= 8)  #AQUI PREGUNTAMOS SI 4 ES MAYOR O IGUAL A 8 
print(4 != 8)   #AQUI ESTA PREGUNTANDO SI ES DIFERENTE O IGUAL PORQUE USAMOS EL !

print('hola' > 'mundo')
print('hola' == 'cola')   #ESTA ORDENADO ALFABETICAMENTE, CUENTA DONDE ESTAS POSICIONADAS

print(len('mariposa'))

print('c' > 'b')
print('aaa' < 'aba')  #COMPARA LAS PRIERAS LETRAS Y SI SON IGUALES PASA A LA SIGUIENTE Y ASI SUCESIBAMENTE


#OPERADORES LOGICOS4
                                   #and pregunta Y esto Y esto
#print(4 < 6 and 7 > 9)  #and    PREGUNTA SI ES VERDADERO Y VERDADERO SI HAY UN FALSE SERA FAL
                                  #LOS DOS TIENEN QUE SER VERDADERO  
#print(4 < 6 or 7 > 9)  #or      #tan solo con que tengamos un true nos dara true
                               # OR nos pregunta esto o ESTO
                               
print( True and False) #and 
print(True or False)  #or
print(not(4 < 6))    #not Cambia si es verdadero o falso Si ponemos el not
                        #delante del 4 aunque sea menor que seis lo cambiaemos
                            #a que es mayor
                            
#print((not(7 != 7) and 6 > 5) and ('rozar' < 'rotar' or not (3 ==5)))

#print((not(7 != 7) and 6 > 5) and ('rozar' < 'rotar' or not (3 == ##5)))     # 7!= 7 no es difrente por lo que seria falso pero al tener el not
                                                                                #lo cambiaria a true
#print((True and True) and (False or True)))

print(True and True)

                   
                                    