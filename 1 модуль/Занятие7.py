import tkinter as tk

current_question = 0
score = 0

window = tk.Tk('Окно')   # tkinter.Tk создает окно
window.geometry('700x500')   # Устанавливаю размер для окна

def check():
    global current_question, score
    answer = var.get()   # записываем в answer информацию из var
    right_answer = facts[current_question]['right']
    if answer == right_answer:
        score += 1
    print(score)
    if current_question < len(facts)-1:
        current_question += 1
        fact['text'] = facts[current_question]['text']
    else:
        points_label = tk.Label(text='SCORE ' + str(score), font=('Arial', 34), fg='red', bg='white')
        points_label.place(x=0,y=0, width=700, height=250)
        
label_title = tk.Label(text='Test', font=('Arial', 24), fg='black', bg='red')   # виджет с текстом(1 строка): text-  текст виджета, font - (шрифт, размер), fg - цвет текста, bg - цвет фона
label_title.place(x=0, y=0, width=700, height=50)   # x, y - расположение виджета по оси x/y, width - длина, height - ширина

facts = [
    {'text':'Земля плоская?', 'right':0},
    {'text':'2+2=4?', 'right':1},
    {'text':'на руке пять пальцев', 'right':1},
    {'text':'У котов 1 хвост', 'right':1}
]

fact = tk.Message(text = facts[current_question]['text'], font=('Arial', 14), width=600, borderwidth=0)   # виджет с текстом(много строк): borderwidth - размер рамки
fact.place(x=10, y=70)

var = tk.IntVar()

rb_true = tk.Radiobutton(text='Правда', variable=var, value = 1)   # переключатель (может быть выбран только один), value - значение, которое передается в код в момент выбора данного
rb_false = tk.Radiobutton(text='Ложь', variable=var, value = 0)    # переключателя. Variable = var - значение передается в переменную var

rb_true.place(x=10,y=120)
rb_false.place(x=10, y=170)

btn_check = tk.Button(text='Ответить', font=('Arial', 14), fg='black', command=check)   # кнопка, command - то, что будет выполняться при нажатии на кнопку
btn_check.place(x=200, y = 130)
window.mainloop()   # нужно для того, что бы окно не пропадало