# # Ленивые выисления и with
import time


# # создаем список из 10 млн чисел (строгие вычисления)
# list = [i for i in range(100000000)]

# # создаем такой же список, но ленивыми вычислениями
# num_list = (i for i in range(100))
# for i in num_list:   
#     print(i)

# time_list = [ time.sleep(i) for i in range(1,4)]   # программа будет работать 6 сек (1 + 2 + 3 сек)
# print(time_list)
# print('Программа завершена')

# time_list = ( time.sleep(i) for i in range(1,4))   # программа завершить работу мгновенно
# print(time_list)
# print('Программа завершена')
# for i in time_list:   # программа будет работать 6 секунд, она вызывает i из time list в памяти. Это помогает оптимизировать программу и ускорить ее работу. Вычисляется в тот момент как мне надо
#     print(i)


# num_list = (i for i in range(100))   # нет в программе, только инструкция, что делать

# new_list = list(num_list)   # работу num_list начинает только сейчас, до этого она лежала ПК. Иначе говоря, происходит построение списка num_list по инструкции в памяти
# print(new_list)

# num_list = list(range(100))   # по факту range тоже является генератором. Все генераторы - ленивые функции
# print(num_list)
# num = range(1,1000)
# print(num)   # будет выведено range(1,1000)
# for i in num:
#     print(i)   # будут выведены числа от 1 до 1000


# создаю функцию-генератор
def my_func():
    for i in range(10):  #2
        # return i    # ничего не будет выведено
        print(f'До {i}')  #3
        yield i  #4
        print(f'После {i}')   #6
    
for i in my_func():   #1
    print(i)   #5


#  генератор можно реализовать:

# функцией
def my_gen():
    for x in range(100):
        yield x


# круглыми скобками
my_gen = (x for x in range(100))







# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# with

# with open('test.txt', 'w') as f:   # with позволяет задавать временный контекс и автоматически ликвидировать его после выполнения нужной операции(например сейчас файл закрывать не придется)
#     f.write('Hello \nworld!')      # as f необязыательная часть, нужна что бы сохранить файл в переменную f
# print(f.closed)

# f = open('text.txt', 'w')   # то же самое, что и прошлый 
# f.write('Hello \nworld')
# f.close()


# Создаю собственный менеджер контекста
import contextlib

@contextlib.contextmanager
def str_rewerse(my_str):
    print('Входим в контекстный менеджер:')
    yield my_str[::-1]
    print('Выходим из контекстного менеджера')

with str_rewerse('Hello, world!') as reversed_str:
    print(f'Выполняется код: {reversed_str}')



# ---------------------------------------------------------------------------------------------------------------------
# *args и **kwargs
# *args - это неограниченное кол-во позиционных аргументов, **kwargs - именованных аргументов

def some_func(*args,**kwargs):
    print(args,kwargs)
    print(type(args))
    print(type(kwargs))

some_func(1, 2, 3, a=4, b=5, c=6)