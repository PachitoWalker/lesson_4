import telebot as tb
import requests
import random
import bs4
import os

bot_token = "5648181385:AAEZddHttGi3r9tOurrgF_pWuSYLKlVy7-M"

bot = tb.TeleBot(bot_token) #создаю бот с токеном bot_token


# def func_decorator(func_to_decorate):
#     def decorated_func():
#         print("Start working")
#         func_to_decorate()
#         print("finished!")

#     return decorated_func

# @func_decorator # при вызове func, сначала активируется func_decorator, при этом функция func станет ее аргументом, заменит func_to_decorate, то есть func_to_decorate == func() 
# def func():
#     print("I'm working")

# func()
def get_interesting_fact():
    response = requests.get('https://i-fakt.ru')
    response = response.content
    html = bs4.BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    return(fact.text + ' ' + fact.a.attrs['href'])
    
def mem():
    return random.choice(os.listdir('мемы')) #os.listdir позволяет пайтон просмотреть объекты из ос, сейчас из папки "мемы"

@bot.message_handler(commands=['fact']) # спец. декоратор, который запускает следующую функцию после того, как пришло сообщение; в скобках написано ("запусти функцию, только если в сообщении написано fact")
def message_processing(message):
    # print("Message: {}".format(message.text)) # .format позволяет вставлять значения (если из много то писать последовательно, чероез запятую) в фигурные скобки {}
    # bot.send_message(message.chat.id, message.text) # помогает присылать сообщения: в messege есть информация, какой id чата, с которого пришло сообщение: я беру из него это id (.chat.id) и отправляю текст сообщения пользователю
    bot.send_message(message.chat.id, get_interesting_fact())

@bot.message_handler(commands=['mem']) # спец. декоратор, который запускает следующую функцию после того, как пришло сообщение
def message_processing(message):
    file = open("мемы/" + mem() ,"rb") # в первые "" указываю путь, во 2 "" - rb, без этого аргумента будет ошибка
    bot.send_photo(message.chat.id, file)
    file.close()

@bot.message_handler(content_types=["photo"])
def message_processing_photo(message):
    fileID = message.photo[-1].file_id
    print('fileID=', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path = ', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('мемы/image.jpg', 'wb') as new_file:
        new_file.write(downloaded_file)

bot.polling(non_stop=True)