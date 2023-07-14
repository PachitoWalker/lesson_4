from oop2 import *   #импортирую свою библиотеку, это делается для упрощения кода и разделения его на блоки. Теперь сама игра у меня находится в game.py, а классы написанны в oop2


tank1.info()
tank2.info()
while True:
    if tank1.health <= 0 and tank2.health <= 0:
        print("\n Ничья!")
        break
    elif tank1.health<=0:
        print("\n Выиграл ", tank2.model)
        break
    elif tank2.health<=0:
        print("]n Выиграл ", tank1.model)
        break
    tank1.shot(tank2)
    tank2.shot(tank1)