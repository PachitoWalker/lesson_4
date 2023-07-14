from pprint import pprint
# Лямбда функщия - функции, не имеющие названия и используемые в коде лишь 1 раз.

# лямбда функwии

# def is_odd(n):   # проверка n на нечетность
#     # 1 способ

#     # if n % 2 > 0:
#     #     return True
#     # else:
#     #     return False

#     # 2 способ

#     return n % 2 != 0   # n % 2 != 0 само по себе логическое выражение, и return в любом случае вернет True/False, поэтому конструкция как в 1 способе не нужна
        

# data = [5, 1, 2, 4, 3, 5, 10, 8, 9]
# print(sorted(data, key=is_odd))   # key - каким способом сортировать data.

# a = ['verdr', 'ghh', 'f', 'reteasd']
# print(sorted(a))   # вернет по алфавиту

# print(sorted(a, key = len, reverse = True))   # отсортирует по длине, от большего к меньшему


# data = [5, 1, 2, 3, 4, 6, 10, 8, 9]
# print(sorted(data, key= lambda n: n % 2 == 0))   # lambda функция, где n - значение (внутри массива)


# telNums = [
#     {
#         'name':'iPhone 14',
#         'brand':'Apple',
#         'price':1200
#     },
#     {
#         'name':'Samsung Galaxy A53',
#         'brand':'Samsung',
#         'price':500
#     },
#     {
#         'name':'Google Pixel 7',
#         'brand':'Google',
#         'price':650
#     },
#     {
#         'name':'iPhone 12',
#         'brand':'Apple',
#         'price': 1000
#     }
# ]

# pprint(sorted(telNums, key= lambda t: t['price']))   # t - элемент в telNums ==> отсортировать элементы в telNums по 'price'

# ---------------------------------

# функция filter()
# data = [2, 1, 2, 4, 3, 6, 10, 8, 9]
# pprint(list(filter(lambda n: n % 2 == 0, data)))   # отфильтровать элементы в data (n) по: n делить на 2 равно число без остатка, то есть оставить только четные и записать в list

# pprint(list(filter(lambda apple: apple['brand'] == 'Apple', telNums)))   # вывести только iPhons

# ---------------------------------


# функция map()
# 4 2 5 => ['4', '2', '5']   ?  [4, 2, 5]

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# num1, num2, num3 = map(int, input().split())   # split делит строку по пробелам (num1 - значение до 1 пробела, num2 - до 2, num3 - до 3), map - делает input().split() числами
# print(num1, num2, num3)


names = ['Иван', 'Петя', 'Настя']
surnames = ['Петров', 'Иванова', 'Сидорова']

full_names = list(map(lambda name, surname: f'{name} {surname}', names, surnames))   # брать name из names и surname из surnames, вывести name + ' ' + surname
print(full_names)

full_names = list(lambda name, surname: f'{name} {surname}', names, surnames)   # брать name из names и surname из surnames, вывести name + ' ' + surname
print(full_names)