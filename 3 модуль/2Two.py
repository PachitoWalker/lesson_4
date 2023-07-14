import vk_api
from APIcb import get_curs

token = 'vk1.a.uFX46bozuaoj1I2khlVaoPxvgXwnhIhFlNuybqTRJDJiHEXEz4UQ7Y15ooPEjSGBx_geMpBbZDuIO_7LrhM-8h3W3djTvST5e4Iqgc5MywK2xZmywH8to7kuUhXYuw89IWckoHlICtYBn3uzHTEx_JbSee4Yhi-IaTDvPGMbC4P_8UpQZW5ckIXXhhkhk8-_hC87lVxjYg9Tgso0bQh1cQ'

#Создаем объект управления ботом
vk = vk_api.VkApi(token=token)

#Запускаем авторизацию бота по указанному токену
vk._auth_token()

while True:
    #получение сообщений из чата
    messages = vk.method (
        "messages.getConversations",
        {"count": 20, "filter": "unanswered"} # count - число ответов, которые может получить бот при одном запросе. Минимум 20, максимум 200 
        # filter - какие диалоги мы читаем. (all - все, unread - непрочитанные, important - важные, unanswered - непрочитанные только для сообществ)
    )
    if messages['count'] > 0:
            user_id = messages['items'][0]['last_message']['from_id']   # получить id пользователя написавшего последнее сообщение
            text = messages['items'][0]['last_message']['text']    # получить последние сообщение
            text_id = messages['items'][0]['last_message']['id']    # получить кол-во отправленных в чат сообщений (удаленные тоже идут в счет)
            # бот отвечает пользователю
            # vk.method('messages.send', {'peer_id' : user_id, 'random_id' : text_id, 'message' : 'текст сообщения'})
            print(text)
            if text.lower() == 'привет':
                vk.method('messages.send', {'peer_id' : user_id, 'random_id' : text_id, 'message' : 'Привет'})
            elif text.lower() == 'курс доллара':
                vk.method('messages.send', {'peer_id' : user_id, 'random_id' : text_id, 'message' : get_curs('R01235')})
            else:
                vk.method('messages.send', {'peer_id' : user_id, 'random_id' : text_id, 'message' : 'я вас не понимаю'})



