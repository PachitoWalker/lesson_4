# Словари

english_dict = {
    'яблоко':'apple',
    'молоко':'milk',
    'кошка':'cat'
}

# english_dict[user_answer]   # если значения user_answer не будет в english_dict, вернется ошибка
# english_dict.get(user_answer)   # если значения user_answer не будет в english_dict, вернется None, а если написать english_dict.get(user_answer, "Слова нет"),вернется "Слова нет"


# 1 Способ (предпочтительней, т.к меньше)
user_answer = input('Какое слово вы хотите перевести?')
print(english_dict.get(user_answer, "Слова в словаре нет"))   # если user_answer есть в english_dict, то он вернет значение user_answer, если его там нет, вернет "Слова в словаре нет"


# 2 Способ
if user_answer.lower() in english_dict:   # .lower() делает все буквы в переменной строчными (было КоШКа, стало кошка)
    # Вывожу в терминал значение ключа молоко (milk)
    print(english_dict[user_answer.lower()])   #english_dict['user_answer'] вернет значение к ключу usera_answer, то есть milk
else:
    print('К сожалению такого слова в словаре нет')


# Создаю массив со списками
questions = [
    {
        'question1':'1, 2, 3, 4',    # на месте question1 вводится вопрос, на месте 1, 2, 3, 4 - ответы
        'right_answer':'2'
    },{
        'question2':'1, 2, 3, 4',
        'right_answer':'2'
    },{
        'question3':'1, 2, 3, 4',
        'right_answer':'1'
    },{
        'question4':'1, 2, 3, 4',
        'right_answer':'4'
    },{
        'question5':'1, 2, 3, 4',
        'right_answer':'3'
    }
]

rightAnswers = 0
for i in range(len(questions)):
    print("Вопрос " + str(i + 1) + ': ' + str(questions[i].get('question'+str(i + 1))))
    user_answer = input('какой вариант ответа?')
    if user_answer == questions[i].get('right_answer'):
        print('ответ правильный!')
        rightAnswers += 1
    else:
        print('ответ неправильный!')
print('Правильных ответов: ', rightAnswers)