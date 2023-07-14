import tkinter as tk
import random
import requests
import bs4 
import datetime 

# window = tk.Tk()
# window.title("окошко") #текст заголовка окна
# window.geometry("600x800+300+100") #x = 300, y = 100

# label = tk.Label(window, text="sath", font = ("Arial", 18), bg="#d899ff", fg="gold") 
# label.place(x=100,y=100)

# label["text"] = "Какой-то текст"
# count = 10
# color = ["red", "black", "white"]
# def func():
#     global count, color
#     count+=1
#     label["bg"] = random.choice(color)
#     btn["text"] = str(count)

# btn = tk.Button(window, text=("click me"), font=("Arial",16), bg="white", fg="black",command = func )
# btn.place(x=100,y=200)
# window.mainloop()


url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.datetime.today().strftime("%d/%m/%Y")

response = requests.get(url, params={"date_req":today})
response = response.content
xml = bs4.BeautifulSoup(response, 'lxml')

def get_course(chr):
    chr = xml.find("charcode", text=chr)
    chr = chr.parent #<Valute ID="R01020"> </Valute>
    chr = chr.value
    return chr.text

print(get_course("USD")[:-2]) # обрезаю число до 2 символов после запятой ( до этого их было 4 )

window = tk.Tk()
window.geometry("400x350+300+300")
window.title("Курс валют")
window.resizable(width = False, height = False)

label = tk.Label(window, text="Курс валют \n ИМБанк", font=("Comic",24), fg="white", bg="#4a814f")
label.place(y = 25, x = 150)

info_course = tk.Label(window,text = "Курс валют на: ", font=("Comic", 16), fg="black") #replace заменяет / на .(сейчас)
info_course.place(y=150,x=90)

date = tk.Label(window,text = str(today.replace("/",".")), font=("Comic", 16), fg="red", border=True) #replace заменяет / на .(сейчас)
date.place(y=150,x=245)

usd_course = tk.Label(window,text = "$ " + get_course("USD")[:5], font=("Comic", 16), fg="black")
usd_course.place(x=100,y=190) 

eur_course = tk.Label(window,text = "€ " + get_course("EUR")[:5], font=("Comic", 16), fg="black")
eur_course.place(x=100,y=230)

btc_course = tk.Label(window,text = "¥ " + get_course("CNY")[:5], font=("Comic", 16), fg="black")
btc_course.place(x=100, y=270)

img = tk.PhotoImage(file="logo.png")
logo = tk.Label(window, image=img)
logo.place(x= 0, y = 0)

window.mainloop()