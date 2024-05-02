#condicionales   MAYOR QUE >  -- MENOR QUE <

if 4 > 6:
    print('4 es menor que 6')    #En este caso no lo imprimira porque 4 no es mayor que 6
    
if 4 < 6: 
    print('4 es menor que 6')    #EN este caso lo imprimira porque 4 es menor que 6
    print('perro')

    
    #print('4 es menor que 6')  #SI LA AFIRMACION ES CORRECTA LO IMPRIMIRA SI NO ES CORRECTA NO LO IMPRIMIRA
    
    
    
numero = 7
    
if 4 > 6 or numero == 7 :             # == #SI SOLO PUSIERAMOS UN = ESTARIAMOS  ASIGNANDO UN VALOR DICIENDO QUE 4 ES IGUAL A
                                       #8 SIN EMBARGO QUEREMOS PREGUNTAR 
                                         # SI 4 Y 8 SON IGIUALES O NO SON IGUALES EFECITVAMENTO NO ES IGUAL A 8 SERIA 4 ES  == 
    print('4 es menor que 6')      #tan solo con que tengamos un true nos dara true
                                   # OR nos pregunta esto o ESTO
                                   
Albion = ('albion es una cosa que no se que es pero la escribo por que tiene que tener mas de cien caracteres y me parece que no voy a llegar nunca por que nose cuanto es eso asi que voy a escribir un poco ma y tal vez algo mas ahora si ahora no ahora si ahora no ahora si ahora no ahora si ahora no')

if len(Albion) > 100:
   print('mucho texto bro')            #SI IMPRIME MUCHO TEXTO BRO POERQUE TIENE MAS DE 100 CARACTERES
    

Noemi = ('Noemi es tonta porque yo lo digo')

if len(Noemi) > 100:
    print('mucho texto bro')  #NO IMPRIME NADA POR QUE NO TIENE MAS DE 100 CARACTERES
    
    #ELSE  LO QUE HACE ES PREGUNTAR SI NO SE CUMPLE EL  'IF' SE APLICA EL ELSE
    
    if 4 >  6:
        print('4 es menor que 6')
    else: 
        print('no se cumplio la condicion')