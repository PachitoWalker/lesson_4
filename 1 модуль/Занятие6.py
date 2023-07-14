# # Функции. Работа с файлами
# import math
# import random

# def my_add(x,y):   # объявляем функцию my_add
#     c = x + y
#     return c

# def circle_square(r, pi=math.pi):   # pi=math.pi означает, что если в функцию будет передано pi, то оно будет равно pi, если не будет передано, то pi=math.pi
#     return math.pi*r*r


# z = my_add(3,4)   # записываем в переменную z то, что вернет функщия my_add при x = 3 и y = 4
# print(z)

# r = int(input('Радиус:'))
# print(circle_square(r))




# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# a = int(input("Введите число А: "))
# b = int(input("Введите число B: "))
# op = input("Введите знак операции ")

# if op == "+":
#     print(add(a,b))
# elif op == "-":
#     print(sub(a,b))
# else:
#     print("Операции нет ")



# def my_max(array):
#     global count
#     maximum = 0
#     for i in array:
#         if i > maximum:
#             maximum = i
#     return maximum

# def my_min(array):
#     minimum = 0
#     for i in array:
#         if i < minimum:
#             minimum = i
#     return minimum
        

# def generate_array(lbound,rbound,count):
#     # array=[]
#     # for i in range(count):
#     #     array.append(random.randint(lbound,rbound))
#     # return array
#     return [random.randint(lbound,rbound) for i in range (count)]

# temp = generate_array(-10,10,20)
# print(temp)

# array = generate_array(-100,100,19)
# print(array)
# print(my_min(array))






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# myfile = open('text.txt', "w")

# # data = myfile.read()   # 'Hello /nworld'(если посмотреть под отладчиком)   /n - перевод строки 
# # print(data)
# # for line in myfile.readlines():
# #     print(line)   # /n не будет если открывать так

# myfile.write("TI NE LOH")

# myfile.close()   #закрывать ВСЕГДА ОБЯЗАТЕЛЬНО



myfile  = open("text.txt")

for line in myfile.readlines():
    print(line, end="")

myfile.close()