import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5880205173:AAHLlxseNqYEyHqzeJ9T9AH5FTb5ApnVE48'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Факт")
    button2 = telebot.types.KeyboardButton("Фото кота")
    button3 = telebot.types.KeyboardButton("Аудио")
    button4 = telebot.types.KeyboardButton("Стих")
    button5 = telebot.types.KeyboardButton("Стикер")
    keyboard.add(button1,button2,button3,button4,button5)
    bot.send_message(message.chat.id,  welcome_text, reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text == "Факт":
        send_fact(message)
    elif message.text == "Фото кота":
        send_cat(message)
    elif message.text == "Аудио":
        send_audio(message)
    elif message.text == "Стих":
        send_poem(message)
    elif message.text == "Стикер":
        send_sticker(message)
    else:
        print(message.text)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEG875jpH7IUNNPuG_tijjWQlrX5kFpawAC1SIAAp3hKUnuxxbQRcdudSwE")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link =  fact.a.attrs['href']
    # создание инлайн кнопки
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_1 = telebot.types.InlineKeyboardButton("Перейти",url=fact_link)
    keyboard.add(button_1)
    # отправка сообщения
    bot.send_message(message.chat.id, fact.text.strip(),reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=['audio'])
def send_audio(message):
    audio = open("happy.mp3","rb")
    bot.send_audio(message.chat.id,audio)


bot.polling()

