class Human:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age 

    # Создаю геттер через property для name
    @property
    def name(self):
        return self.__name
    
    # Создаю геттер через property для age
    @property
    def age(self):
        return self.__age
    
    # Создаю сеттер через property для name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @age.setter
    def age(self, new_age):
        if int(new_age) >= 0:
            self.__age = new_age
        else:
            raise ValueError('Отрицательное значение возраста')   # создать исключение 
        
    # Создаю делитер для age и name
    @age.deleter
    def age(self):
        self.__age = None
    
    @name.deleter
    def name(self):
        self.__name = None


person = Human('Pit',23)
print(f'{person.name}, {person.age}')

person.name = 'Rick'   # так можно менять значения при создании сеттеров через property
person.age = '0'

print(f'{person.name}, {person.age}')


del person.name
del person.age

print(f'{person.name}, {person.age}')