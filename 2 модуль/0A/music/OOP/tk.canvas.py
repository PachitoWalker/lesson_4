import tkinter as tk

window = tk.Tk()
window.geometry("600x600")

canvas = tk.Canvas(window, width=600, height=600,background="white")
canvas.pack()


canvas.create_rectangle(10, 10, 110, 110, fill="yellow", outline="green") #rectangle - квадрат, первое значение - х1, второе - у1, третье - х2, четвертое -у2, fill - цвет, outline - цвет контура
# canvas.create_rectangle(120,120, 140, 140,fill="red",outline="black")
# canvas.create_rectangle(180,180, 220, 220,fill="red",outline="black")
# canvas.create_rectangle(300,300, 360,360,fill="red",outline="black")

canvas.create_polygon(10, 180, 60, 120, 110, 180, fill="black", outline="green")#polygon - треугольник, первые 2 значения - х1 и у1, вторые 2 - х2 и у2, третьи 2 - х3 и у3, fill и outline - так же как в квадрате

def create_home():
    canvas.create_rectangle(200 ,200, 260, 260, fill = "red", outline="black")
    canvas.create_polygon(180, 200, 230,150, 280,200)
    canvas.create_rectangle(220, 220, 240, 240, fill = "azure", outline="black")

window.mainloop()