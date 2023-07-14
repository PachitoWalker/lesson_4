# Условный оператор (if, else, elif)
import random

# summ = 0
# dayscount = 7
# for i in range(dayscount):
#     weather = int(input('сколько сегодня на улице градусов?'))
#     summ += weather

# sr_weather = summ / dayscount 

# print(sr_weather)


# if a == b:  если a равно b 
# if a != b:  если a не равно b
# if a > b: если a больше b
# if a < b: если а меньше b
# логические оператор and и or; if a == b and c == b: если a равно b и c равно b; if a == b or c == b: если а равно b или  c равно b;


# number = random.randint(1,10)
# for i in range(1,4):
#     user_answer = int(input('Назовите случайное число от 1 до 10: '))
#     if user_answer == number:
#         print('Поздравляю! Вы угадали!')
#         break
#     elif user_answer != number:
#         if number - user_answer == 1 or number - user_answer == -1:
#             print('Вы почти угадали!')
#         else:
#             print('Вы не угадали! Попробуйте снова!')



number = random.randint(1,10)
print(number)
for i in range(1,4):
    user_answer = int(input('Назовите случайное число от 1 до 10: '))
    if user_answer == number:
        print('Поздравляю! Вы угадали!')
        break
    elif user_answer != number:
        if number - user_answer == abs(1):
            print('Вы почти угадали!')
        else:
            print('Вы не угадали! Попробуйте снова!')