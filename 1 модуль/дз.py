password = 235

user_password = int(input('введите пин-код'))

while user_password != password:
    print('Пин-код не верный! Попробуйте снова!')
    user_password = int(input('введите пин-код'))

print('Пин-код подошел! Выполняется вход...')