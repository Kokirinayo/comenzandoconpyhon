#clases
class MyEmptyPerson:
    pass
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person: #deberiamos tener un fichero solo con person  no esta bien tener todo mezclado
    def __init__(self, name, surname, city):   #init es un constructor de clases
        self.name = name
        self.surname = surname
        self.city = city
        
my_person = Person('Brais', 'Moure', 'Villena')
print(my_person.name)
print(my_person.surname)
print(my_person.city)



class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.full_name = f'{name}{surname}({alias})'
    def walk (self):
        print(f'{self.full_name} Está caminando')
        
my_person = Person('Brais ', 'Moure')
print(my_person.full_name)
my_person.walk()
my_other_person = Person('Brais', 'Moure', 'Mouredev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Héctor de León El loco de los perros'
print(my_other_person.full_name)