import telebot
import requests
import bs4 
import random 
import os

token = "5648181385:AAEZddHttGi3r9tOurrgF_pWuSYLKlVy7-M"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start", "help"])
def get_message(message):
    text = f"""Привет, {message.from_user.first_name,} {message.from_user.last_name}
    Я умею рассказывать факты, могу прислать фотки котиков и многое другое!
    """    # """ """ - тоже самое, что и "", но позволяет писать текст в несколько строк.
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False) #из подбиблиотеки types библиотеки telebot беру ReplyKeyboardMarkup, который создает клавиатуру(row width - кол-во столбцов,lesize_keyboard - подстраимование клавиатуры под девайс, one time keyboard - одноразовая ли клавиатура)
    keyboard2 = telebot.types.InlineKeyboardMarkup() # Создаю такую клавиатуру, к которой можно привязать такую кнопку, как под постами в тг с сылкой (ну прозрачные такие)
    button1 = telebot.types.KeyboardButton("Факт") #создаю кнопки
    button2 = telebot.types.KeyboardButton("Котики")   #Итог: кнопки бывают Inlain и replyne, сначала создается клавиатура (строки 16-17), потом кнопки (строки 18-21),
    button3 = telebot.types.KeyboardButton("Музыка")   #потом привязываем кнопки к клавиатурам.
    button4 = telebot.types.KeyboardButton("Стикер")
    button5 = telebot.types.KeyboardButton("Во что поиграть на ПК")
    keyboard.add(button1,button2,button3,button4,button5) # добавляю к клавиатуре кнопки
    bot.send_message(message.chat.id,text, reply_markup=keyboard) # присоединяю клавиатуру 


@bot.message_handler(commands=["fact"])
def send_fact(message):
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = bs4.BeautifulSoup(response, "lxml")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    keyboard2 = telebot.types.InlineKeyboardMarkup() # Создаю такую клавиатуру, к которой можно привязать такую кнопку, как под постами в тг с сылкой (ну прозрачные такие)
    buttonIn = telebot.types.InlineKeyboardButton("Перейти", url = fact.a.attrs["href"]) #Создаю кнопку как под постами в тг с сылкой (ну прозрачные такие), пишу текст на кнопке и ссылку на сайт, куда она переправляет
    keyboard2.add(buttonIn) # присоединяю кнопку к класиатуре
    bot.send_message(message.chat.id, fact.text, reply_markup=keyboard2)

@bot.message_handler(commands=["cat"])
def send_cats(message):
    def send_cat():
        return random.choice(os.listdir("котики"))
    cat = open("котики/" + send_cat(), "rb")
    bot.send_photo(message.chat.id, cat)
    cat.close()
    
@bot.message_handler(commands=["mp3"])
def send_mp3(message):
    def mp_3():
        return random.choice(os.listdir("music"))
    mp3 = open("music/" + mp_3(), "rb")
    bot.send_audio(message.chat.id, mp3)
    mp3.close()


@bot.message_handler(commands=["stick"])
def send_stick(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEHukhj6lSp6ijMTvEC0iM-9mpgqJ3O3gAC-iUAAgNrWEtiLk1ucLahoy4E")

@bot.message_handler(commands=["game"])
def send_games (message):
    response = requests.get("https://store.steampowered.com/?l=russian")
    response = response.content
    html = bs4.BeautifulSoup(response, "lxml")
    game = random.choice(html.find_all(class_="tab_item_name"))
    bot.send_message(message.chat.id,game.text)

    
@bot.message_handler(content_types=["text"]) # все комманды должны идти в самом конце
def answer(message): 
    if message.text == "Факт":
        send_fact(message)
        print(message.chat)
    elif message.text == "Музыка":
        send_mp3(message)
        print(message.chat)
    elif message.text == "Котики":
        send_cats(message)
        print(message.chat)
    elif message.text == "Стикер":
        send_stick(message)
        print(message.text)
    elif message.text == "Во что поиграть на ПК":
        send_games(message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используй комманды на кнопках!")
        print(message.chat)
        
    #bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name, } {message.from_user.last_name}")



bot.polling(non_stop=True)