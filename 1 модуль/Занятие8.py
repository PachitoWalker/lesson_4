import tkinter as tk

window = tk.Tk()
window.geometry('900x300')
window.resizable(width=False, height=False)   # отключает изменение окна
window.config(bg='black')   # с помощью config можно изменить цвет фона окна (config - внутренние настройки)

text = tk.Label(text='ВАШ КОМПЬЮТЕР ЗАРАЖЕН',
                font=('Corier New', 39),
                fg='green', 
                bg='black')
text.place(x=100, y=100)
count_text = tk.Label(text='6', fg='green', bg='black', font=('Courier New', 38))
def count_start():
    if int(count_text['text']) > 0:
        count_text.place(x=400, y=25)
        count_text['text'] = int(count_text['text']) - 1
        window.after(1000, count_start)   # через 1000 мс включать count_start

    else:
        count_text['text'] = '0'
        width = window.winfo_screenwidth()   # считываю информацию о длине экрана
        height = window.winfo_screenheight()   # о ширине
        window.geometry(str(width)  + 'x' + str(height))   # меняю размены окно под размер экрана
        photo = tk.PhotoImage(file='file.gif')
        label = tk.Label(image=photo, bg='black')   # image = photo - изображение = фото
        label.image = photo   # нужно чтоб была фотография а не черный экран
        label.place(x=0,y=0, width=width, height=height)

def on_close():
    print('Closing')
    count_start()
    # window.destroy()   # эта команда искусственно закрывает окно

window.protocol("WM_DELETE_WINDOW", on_close)   # при нажатии на кнопку "закрыть" выполнять on_close вместо закрытия

window.mainloop()



# Для того, что бы загрузить вирус в .exe нужно 1) скачать pyinstaller (pip install pyinstaller)   2) набрать python -m PyInstaller название_файла.py, появятся папки и в них лежат exe