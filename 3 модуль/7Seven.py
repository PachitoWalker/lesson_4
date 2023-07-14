# # встроенный метод __add__

# # создаем класс для описания товара

# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

#     def __add__(self, other):

#         # проверяем, что работаемм с объектом класса Item
#         if isinstance(other,Item):   # возвращает True/False

#             return self.price + other.price   # так я сделал сначала. int object has no attribute 'price'
        
#         if isinstance(other,int):
#             return self.price + other
        

# item_1 = Item('Видеокарьа', 50_000, 2)
# item_2 = Item('Процессор', 30_000, 0.3)

# # 1 способ, но не очень хороший, т.к price может быть приватным полем
# total_price = item_1.price + item_2.price
# print(total_price)   

# # 2 способ, уже лучше
# total_price = item_1 + item_2   # сработает, т.к есть функция __add__ в классе
# print(total_price)

# # непредвиденная ситуация:
# total_price = item_1 + 3000
# print(total_price)



# ------------------------------------------------------------------------------------------------------------------------------------------------------

# ИГРА 'Алхимия'

import tkinter as tk
from random import randint


window = tk.Tk()
window.geometry('600x600')


# -------
# Создаю классы различных элементов природы
class Fire:
    image = tk.PhotoImage(file='fire.png').subsample(8,8)   # сохраняю fire.png в переменную image как изображение

    def __add__(self, other):
        # проверка, что объект который мы объединяем  огнем - earth
        if isinstance(other, Earth):
            return Clay
        

class Wind:
    image  = tk.PhotoImage(file='wind.png').subsample(8,8)   # subsample уменьшает изображение по оси x и y в n (сейчас 8) раз

class Water:
    image = tk.PhotoImage(file='water.png').subsample(8,8)


class Earth:
    image = tk.PhotoImage(file='earth.png').subsample(8,8)
    
    def __add__(self, other):
        if isinstance(other, Earth):
                return Clay

class Clay:
    image = tk.PhotoImage(file='clay.png').subsample(8,8)
# -----

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)   # find_overlapping создает что-то на подобии хитбокса
    # Перемещаем изображение за курсором
    canvas.coords(images_id, event.x, event.y)   # event.x u event.y это координаты курсора

    #соединение элементов
    if len(images_id) == 2:
        elem_id_1 = images_id[0]
        elem_id_2 = images_id[1]

        element_1 = elements[elem_id_1 - 1]
        element_2 = elements[elem_id_2 - 1]

        new_element = element_1 + element_2

        # проверка, что появился новый элемент
        if new_element:
            # Проверка, что такого элемента еще не было
            if new_element not in elements:
                # Отрисовываем на холсте новый элемент
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)
# Создаю и размещаю холст

canvas = tk.Canvas(window, width = 600, height= 600)   
canvas.pack()

# Создаем список с элементами
elements = [Earth(), Water(), Wind(), Fire()]

# Размещаем элементы на холсте
for elem in elements:
    canvas.create_image(randint(50, 550), randint(50,550), image = elem.image)   # создать изображение, с координатой x/y от 50 до 550 пт и изображением = image у elem

# Связываем левую кнопку мышки с перемещением картинки (бинд клавишц)
window.bind('<B1-Motion>', move)


window.mainloop()