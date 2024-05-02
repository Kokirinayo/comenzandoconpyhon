#EN ESTE MODULO VAMOS A HABLAR DE LAS EXCEPCIONES

#Ex

try:
    print(adfafas)    
        
except NameError as error:                      #ass guarda el error
     print('error de tipo NameError')     #podemos usar varios except segun necesidades
     
except TypeError:
    print('error de tipo TypeError')
     
else:
    print('Hola mundo')  #Else solo funciona cuando el try esta correcto si tiene '3' no funcionara porque no se ponen comillas y dara error
                          #tiene que estar sin comillas para que este correcto el resultado y pae a except
finally:
    print('subscribete')   #Lo utilizamos para cosas que pueden dar error (LAS EXCEPCIONES)
    
    
    