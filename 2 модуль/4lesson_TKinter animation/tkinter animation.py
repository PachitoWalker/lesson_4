import tkinter as tk
import random

window = tk.Tk()

w = 600   # ширина, которую я позже задам окну
h = 600   # высота, которую я позжу задам окну
window.geometry(f"{w}x{h}")   # укзываю размер окна WxH


canvas = tk.Canvas(window, width=w, height=h)   # указываю, где поместить холст(в window), его ширину и высоту
canvas.place(in_=window,x=0,y=0)   # указываю, куда поместить холст и по каким координатам
bg_photo = tk.PhotoImage(file="bg_2.png")   


class Knight:   # Создаю класс кнайт
    def __init__(self):   # __init__ - конструктор классов
        # координаты 
        self.x = 70
        self.y = h//2
        # скорость
        self.v_y = 0
        self.v_x = 0
        # изображение
        self.photo = tk.PhotoImage(file="knight.png")
    def up(self,event):
        self.v_y = -3
        if knight.y < 50:
            knight.stop(knight)
    def down(self,event):
        self.v_y = 3
        if knight.y > (h - 50):
            knight.stop(knight)
    def stop(self,event):   # event - обрабатывает нажатие клавиш
        self.v_x = 0
        self.v_y = 0
    def forward(self,event):
        self.v_x = 3
        if knight.x > (w - 50):
            knight.stop(knight)
    def back(self,event):
        self.v_x = -3
        if knight.x < 50:
            knight.stop(knight)

class Dragon:
    def __init__(self) :
        self.x = random.randint(750,1500)
        self.y = random.randint(100,500)

        self.v = random.randint(1,2)
        self.photo = tk.PhotoImage(file="dragon.png")

    
knight = Knight()   # создаю экземпляр knight класса Knight в памяти
dragons = []   # создаю список dragons
for i in range(40):
    dragons.append(Dragon())   # добавить в список dragons экземпляр класса Drangon

def game():
    canvas.delete("all")   # удаляю все объекты с холста
    canvas.create_image(h/2 ,w/2, image=bg_photo)   # создаю на холсте изображение размером 300х300, изображение = bg_photo
    knight.y += knight.v_y
    knight.x += knight.v_x
    canvas.create_image(knight.x,knight.y,image=knight.photo)
    kill_dragon = -1
    for i,dragon in enumerate(dragons):   # enumerate разыменовывает список, 1 элемент - индекс(i), 2 - значение этого индекса (dragon)
                
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)
        
        if ((dragon.x-knight.x)**2 + (dragon.y-knight.y)**2) <= 95**2:   #пока что не пытайся понять, тут геометрия, которую я еще не проходил в школе, данная строка говорит, что если дракон столкнулся с рыцарем, нужно...
            kill_dragon = i

        if dragon.x <= -50:
            canvas.delete("all")
            canvas.create_text(w//2, h//2, text="You lose!", font=("Verdana", 42),fill="red")  
            break

    if kill_dragon > -1:   # если в списке dragons еще есть dragon, выпролнить...
        del dragons[kill_dragon]   # удалить из dragons элемент i

    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text="You are win!", font=("Verdana", 42), fill="green")

    window.after(5,game)   #создаю задержку отрисовки в 5 мс


window.bind('<Key-Up>', knight.up)   # при нажатии на клавиатуре Key-Up (стрелочки вверх) выполнить knight.up
window.bind('<Key-Down>', knight.down)  # при нажатии на клавиатуре Key-down (стрелочки вниз) выполнить knight.down
window.bind('<KeyRelease>', knight.stop)   # если не нажата ни 1 кнопка, выполнить knight.stop
window.bind('<w>', knight.up)
window.bind('<s>', knight.down)
window.bind('<d>', knight.forward)
window.bind('<Key-Left>', knight.back)
window.bind('<a>', knight.back)
window.bind('<Key-Right>', knight.forward)
game() 


window.mainloop()