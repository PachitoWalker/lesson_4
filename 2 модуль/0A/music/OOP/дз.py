import random

class User:
    def __init__(self, name, health, min_damage, max_damage):
        self.health = health
        self.damage = random.randint(min_damage, max_damage)
        self.name = name
    def attack(self):
        print(f"{self.name} нанес {self.damage} урона врагу")

class Wizard(User):
    def __init__(self, name, health, min_damage, max_damage):
        super().__init__(name, health, min_damage, max_damage)

class Warrior(User):
    def __init__(self, name, health, min_damage, max_damage):
        super().__init__(name, health, min_damage, max_damage)

class Archer(User):
    def __init__(self, name, health, min_damage, max_damage):
        super().__init__(name, health, min_damage, max_damage)


user1 = User("Пользователь", 100,5,20)
user1.attack()

user2 = Wizard("Маг",50,20,40)
user2.attack()

user3 = Warrior("Воин",150, 30, 31)
user3.attack()

user4 = Archer("Лучник",75, 10, 15)
user4.attack()