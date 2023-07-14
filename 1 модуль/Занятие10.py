# # Цикл while. Генератор pdf

# i = 1

# while i <= 10:    # пока i мменьше или равно 10
#     print(i**2)   # вывести в консоль i в квадрате
#     if (i**2) % 2 != 0:   # если i в квадрате делится на 2, и в остатке остается 0, то
#         i+=2   # i = i + 2
#     else:   # иначе
#         i+=1   # i = i + 1

# sum_now = 0
# mounth = 0
# sum = int(input('Сколько ты хочешь накопить?'))
# proc = int(input('Сколько процентов от З/П ты готов откладывать?'))
# while sum_now < sum:
#     sum_now += int(input('Сколько ты получил за этот месяц?')) * (proc / 100)
#     mounth += 1
# print(mounth)


# while True:   # бесконечный цикл
#     print('бесконечный')
#     break   # заканчивает выполнение цикла



# ----------------------------------------------------------------------------

import fpdf

Pdf = fpdf.FPDF(
    orientation= 'P',   #P - портретная, L - альбомная
    unit='cm',   # Единицы измерения (pt - точки, mm - милиметры, cm - сантиметры)
    format=(10,10),   # размеры(можно задавать А3, А4 и т.п)
)
Pdf.add_font('arial', style='',fname='C:\Windows\Fonts\Arial.ttf',uni=True)   #style - тип шрифта(жирный, курсив) fname - путь к шрифту, uni - использование юникода
Pdf.add_page()

Pdf.set_font('arial', size=16)
Pdf.set_text_color(0,255,0)
Pdf.set_fill_color(0,0,168)
Pdf.set_draw_color(0,0,225)
txt = 'I love python'
Pdf.cell(w=10, h=5, txt = ' Welcome to Python!', align='C', border=1, fill=True)   # w - длина, h - ширина, txt - текст, align - выравнивание, border - рамка, fill - заливка

Pdf.image('Занятие10.jpg', h=0, w=10, x=0, y=5)
Pdf.output('test_pdf.pdf')