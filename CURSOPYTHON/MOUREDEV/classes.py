#CLASES #los nombres de las clases no van con snakes cases van al reves

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

