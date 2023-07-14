# from fpdf import FPDF
# from datetime import datetime

# pdf = FPDF('P', 'mm', 'A4') #задаю в памяти ПК параметры пдф файла,  'P' - ориентация шрифта(портретная), 'mm' - единица измерения, 'A4' - размер как А4 (можно записать как w='' и h='')
# pdf.add_page() #создаю страницу пдф с заданными выше параметрами

# pdf.image('астронавт.jpg', h=297, w=210, x=0, y=0) # добавляю картинку с именем 'астронавт.jpg', высотой h=297 (mm) и шириной w=210 (mm) в координатах x=0 и y=0

# pdf.add_font('comic', '', 'C:\Windows\Fonts\comic.ttf', uni=True) #добавляю шрифт, называю его comic, в '' должен быть стиль(вводить имя стиля не обязательно, но '' надо ставить)
# #указываю путь до шрифта, названного мною comic, ('C:\Windows\Fonts\comic.ttf'), указываю, что использую юникод, использовать надо что бы символы были разборчивыми(uni = True)
# pdf.set_font('comic', size=37) #говорю что я использую шрифт comic с размером 37
# pdf.set_text_color(0,0,0) #задаю цвет текста (RGB)

# name = input('Кому отправите открытку?ФИО: ')

# pdf.cell(0, 95, ln=1) #добавляем пустую ячейку с (текстом) где w=0(сохраняет размер текста в длину по умолчанию), h=95 (по итогу добавляем линию)
# pdf.cell(0, 20, txt='Дорогой ' + name + '!', align='c', ln=10) #добавляем ячейку с текстом 'Дорогой '+ имя + '!', c alight='C' (Выравнивание п центру), 

# pdf.set_font('comic', size=18)
# text = input('Введите текст поздравления: ')
# pdf.set_right_margin(50) #задаю отступ справа в 50 мм
# pdf.set_left_margin(50) #слева
# pdf.multi_cell(0, 20, txt=text, align='C') #multi cell - большой текст

# today = datetime.today().strftime('%d.%m.%y') #добавляем дату отправления - из datetime берем today, при помоци .strftime('%d.%m.%y) задаем, что формат будет %d - day - день, .%m - month - месяц, .%y - year - год (день.месяц.год)
# pdf.set_text_color(124, 189, 23)

# pdf.cell(0, 10, txt=today, align='R', ln=1)
# author_name = input('Введите свое имя')
# pdf.cell(0, 10, txt=author_name, align='R', ln=1)

# pdf.output('holiday.pdf')








#-------------------------------------------------------------------------------------------------------------------------------------------------------










import tkinter as tk
import bs4
import random
import requests



def rand():
    response = requests.get('https://i-fakt.ru/')   # с помощью requests.get я могу получать информацию с какого-либо внешнего источника (например сайта, адрес который я положил в '')
    response = response.content   # из всего response (смотри в отладчики в Locals) мне нужно получить только content
    html = bs4.BeautifulSoup(response, 'lxml')   # BeautifulSoup получает на вход нашш запрос и информацию от том, из чего он состоит, мы говорим ему что это будет lxml
    fact = random.choice(html.find_all(class_='p-2 clearfix'))   # я говорю html: найди внутри себя все, в чем class = "p-2 clearfix", и выбери случайный (random.choice)
    label = tk.Label(text=fact.text + '\n' + fact.a.attrs['href'], fg='black', bg='white', width = 0, height = 0)
    label.place(x=18, y=60)

def dr_menu():
    clear()
    menu_title = tk.Label(text="Что бы вы хотели сделать?", font=("Arial", 24), fg="white", bg="orange")
    menu_title.place(width=700, height=50, x=0, y=0)
    btn1 = tk.Button(text="Узнать что-то новое", font=("Arial",18), fg="black", command=rand)
    btn1.place(x=25,y=75, width = 300)

    btn2 = tk.Button(text="Посмотреть на котиков", font=("Arial", 18), fg="black")
    btn2.place(x=375, y = 75, width = 300)

def clear():
    all_widgets = window.place_slaves() #.place_slaves дает расположение всех объектов в window
    for wid in all_widgets:
        wid.destroy()
    dr_home_btn()

def dr_home_btn():
    btn_home = tk.Button(text="Домой", font=("Arial", 20), bg='white', fg='black', command=dr_menu)
    btn_home.place(x=25, y=500, width=150)

window = tk.Tk()
window.geometry("700x600")

dr_menu()

window.mainloop()