# # class People:
# #     # магический метод - метод который вызывается в определенный момент, когда мы создаем класс
# #     def __init__(self, name, age):
# #         # self - ссылка на объект
# #         self.name = name
# #         self.age = age
# #         print("Я родился")

# #     def info(self):
# #         print(f"{self.name}{self.age}")

# # #объект (экземпляр класса)
# # people1 = People("Pavel", 21) 

# # people1.info()  #автоматически подставляется self
# # People.info(people1)   #сам подставил



# class A:
#     def __init__(self,q,w,e,r,t):
#         self.q = q
#         self.w = w
#         self.e = e 
#         self.r = r
#         self.t = t
#     def one(self):
#         print("one is A")
#     def two(self):
#         print("two is A")

# class C:
#     def one(self):
#         print("onec is C")

#     def twoc(self):
#         print("twoc is C")

# class B(A,C): #class B наследует class A, он может использовать методы класса А
#     def __init__(self, q, w, e, r, t, new):
#         super().__init__(q, w, e, r, t)   # данная строка нужна для того, что бы не дублировать весь код родительского класса А, этой строкой можно сказать я его итак вызываю
#         self.new=new
    
#     def one(self):
#         print("one is B")   #теперь при вызове b.one будет писаться one is B, а при вызове a.one, как и до этого, one is A
    
#     def three(self):
#         super().one()
#         print("three is B") 

# a = A(1,2,3,4,5)
# a.one()
# a.two()
# print("-"*200)
# b = B(1,2,3,4,5,6)   #если у родительского класса есть атрибуты, их надо указывать и в дочернем классе
# b.one()
# # b.two()
# # b.three()
import random


class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health
    
    def info(self):
        print(f"{self.model} имеет лобовую броню {self.armor} мм при {self.health} ед.здоровья и уронe {self.damage} ед")

    def shot(self,enemy):   #enemy - вражеский танк
        enemy.health -= round(self.damage - self.damage * enemy.armor / 100, 2)   #round округляет, в конце (сейчас там 2) указывается кол-во знаков после запятой, до которых нужно округлить
        print(f"\n{self.model}:")   # модель танка, который стреляет
        print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")

class SuperTank(Tank):
    def __init__(self, model, armor, min_damage, max_damage, health, double_shot_change):
        super().__init__(model, armor, min_damage, max_damage, health)
        self.double_shot_change = double_shot_change

    def shot(self,enemy):
        if random.randint(1,100) <= self.double_shot_change:
            print("\n ДВОЙНОЙ ВЫСТРЕЛ!")
            super().shot(enemy)
            super().shot(enemy)
        else:
            super().shot(enemy)

tank1 = Tank("Pz.Kpfw. I", 10, 50, 75, 340)
tank2 = SuperTank("T80", 15, 35, 55, 376, 30)