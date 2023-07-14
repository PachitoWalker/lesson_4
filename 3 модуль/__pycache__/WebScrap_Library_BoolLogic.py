# var_1 = True # или любой набор символов - true
# var_2 = False # или 0 - false

# print(type(var_1)) #bool - логическая переменная

# var_1 = 5 > 1
# print(var_1)

# if False:
#     pass
# else:
#     print("Условие не выполнилось")
#     a = int(input())
#     b = int(input())
#     c = int(input())

# if a > b:
#     if a > c:
#         maxf = a
#     else:
#         maxf = c
# elif b > c:
#     maxf = b
# else:
#     maxf = c    
# print(max)    

# print(max(a,b,c))
# print(min(a,b,c))







import requests
import json

url = "https://swapi.dev/api/"
response = requests.get(url)
response = response.json() #с помощью json можно получать информацию с сайта в виде списка
people = response.get("people") #взять из response значение с ключом people
planets = response.get("planets")
#print(people)

def check_people(url):
    for i in range(10):
        response = requests.get(f"{url}/{i}")
        response = response.json()
        print(response.get("name"))
#check_people(people)

def check_planets(url):
    for i in range(10):
        response = requests.get(f"{url}/{i}")
        response = response.json()
        print(response.get("name"))

def check_diameter(url):
    diameters_list = []
    for i in range(1,61):
        response = requests.get(f"{url}/{i}").json()
        diam = response.get("diameter")
        name = response.get("name")
        diameters_list.append({name:diam})
    for i in range(0, len(diameters_list) + 1):
        max_diam = 0
        if int(diameters_list[i][name]) > max_diam:
            max_diam = diam[i]
    print(max_diam)


    print(diameters_list)
check_diameter(planets)
# print(requests.get(planets).json())
# check_planets(planets)