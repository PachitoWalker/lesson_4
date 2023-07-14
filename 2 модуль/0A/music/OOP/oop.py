import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=600, height=600,background="white")
canvas.pack()

class House: #объект 
    def __init__(self,wall_color,roof_color,number,height = 100,width = 80):  #функция init класса house? в ней я указываю цвет крыши, цвет стен, высоту,ширину, self показывает, что это свойство относится именно а house, 
        self.number = number
        self.wall_color = wall_color
        self.roof_color = roof_color #атрибуты класса
        self.height = height
        self.width = width
        self.roof = None
        self.wall = None
 
    def build_house(self,x,y): # методы класса (функции внутри класса)
        self.y_roof = y - (2.5)*self.height/13 
        self.wall = canvas.create_rectangle(x - self.width/2 + 10, self.y_roof, x + self.width/2 - 10,  y + self.height/2, fill = self.wall_color, outline="black")  #x,y - середина всего дома(только сейчас); создаю стену для домика
        self.roof = canvas.create_polygon(x - self.width/2, self.y_roof, x, y - self.height/2,x + self.width/2,self.y_roof, fill= self.roof_color, outline="black") #создаю крышу для домика
        # canvas.create_rectangle(220, 220, y + self.height, 240, fill = "azure", outline="black")

    def info(self): #нужно обязательно, для ВСЕХ методов класса передавать self
        print("Номер дома: ", self.number) 
        print("Цвет стены ", self.wall_color)
        print("Цвет крыши:", self.roof_color)

        
house1 = House("yellow","green",1) # экземпляр объекта
house2 = House("azure", "lavender",2)

house2.wall_color = "purple"
house2.info()

house1.build_house(50,50)
house2.build_house(200,200)

window.mainloop()