import tkinter as tk
import random 
import time

window = tk.Tk()

window.title("Ping-pong")
window.geometry("500x400")
window.wm_attributes("-topmost", 1)   # Что бы мое окно было поверх других окон                

canvas = tk.Canvas(window, height= 50, width= 75, bg= "green")

while True:     # то же самое, что и mainloop() только сделанное самостоятельно
    window.update()
    time.sleep(0.01)