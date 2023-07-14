# # Геттер - функция, возвращающая какое-либо значение атрибута.
# # Сеттер - функция, устанавливающая какое-либо значение атрибуту.
# # Делитер - функция, определяющая поведение при удалении атрибута или метода.
# # set(get)_(названиеАтрибута)

# class Year:
#     def __init__(self, days, season):
#         self.__days = days   # __days означает что days это приватное поле
#         self.__season = season

#     # Создаем геттер для получения кол-ва дней
#     def get_days(self):   # геттер
#         return self.__days
    
#     # Создаем геттер для получения сезона
#     def get_season(self):
#         return self.__season 

    
#     # Создаем сеттер для изменения кол-ва дней
#     def set_days(self, new_days):

#         # валидация переданного параметра new_days
#         if new_days <=366 and new_days >= 365:
#             self.__days = new_days
#         else:
#             raise Exception('Некоретное значение')

        
#     # Создаем сеттер для изменения сезона
#     def set_season(self, new_season):
#         self.__season = new_season
    
# my_year = Year(365, 'Winter')


# print(my_year.get_days())
# my_year.set_days(366)   # так правильно
# my_year.__days = 9384   # а так нет (__days - приватная функция)
# print(my_year.get_days())


# print(my_year.get_season())
# my_year.set_season('Summer')
# print(f'{my_year.get_days()} days in this year, it is {my_year.get_season()} now')




# ---------------------------------------------------------------------------------------------------------------------

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

person = Human('Pit',23)
print(f'{person.name}, {person.age}')

person.name = 'Rick'   # так можно менять значения при создании сеттеров через property
person.age = '0'

print(f'{person.name}, {person.age}')