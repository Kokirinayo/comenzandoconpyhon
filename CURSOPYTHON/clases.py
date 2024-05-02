#CLASES la forma de escribir las clases es diferente a la forma en la que escribimos las variable y sin espacios
#en este caso no usamos barrajabaja ponemos 1 letra en minuscula y despues cada palabra primera en mayuscula #self es la forma de guardar cosas
class unHumano: 
    def __init__(self, altura, edad, peso):   # usamos def para usar el constructor de claes

        self.altura = altura #así le damos el nombre a la variable altura, edad, peso
        self.edad = edad 
        self.peso = peso   
        
    def comer(self): #para añadir una accion 
        print(f' el humano de {self.edad} esta comiendo')   #ponemos self para llamar a altura,edad,peso
        
humano_1 = unHumano(1.80, 23, 58)
        
print(humano_1.altura)
print(humano_1.edad)
print(humano_1.peso)

print(f'el humano 1 mide {humano_1.altura} cm, pesa {humano_1.peso} kg y tiene edad {humano_1.edad} años')

humano_1.comer()


