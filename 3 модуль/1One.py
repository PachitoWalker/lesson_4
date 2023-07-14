# # Программа "Сотрудники и зарплаты"

# # Простая реализация работника
# name = "Игорь"
# salary = 200_000 #-- 200000 и 200_000 равнозначны

# # вывод информации на экран 
# print(f"Имя работника: {name}, З/П в месяц {salary}")
# print(f"З/П в год: {salary * 12}")

#---------------------------------------------------------------------------------------------------------------------------------------

# -------------Реализация работника через словарь 

# employee = {
#     "name":"Игорь",
#     "salary":200_000
# }

# employes = [ 
#     {
#     "name": "Дима",
#     "salary": 300_000
#     },
#     {
#     "name": "Игорь",
#     "salary": 200_000
#     },
#     {
#     "name": "Вася",
#     "salary": 150_000
#     }
# ]


# # -------------Уволняем игоря
# print(employes)

# del employes[1] #--- Плохой способ, т.к если бы сотрудников было много то искать его индекс пришлось бы слишком долго
# print(employes)

# for employee in employes:  
#     if employee['name'] == "Игорь":
#         employes.remove(employee)
#         break

# # -------------Нанимаем нового сотрудника
# new_employee = {
#     "name": "Кирилл",
#     "salary": 200_000
# }

# #  --------------Добавляем сотрудника в список

# employes.append(new_employee)

# #----------------Узнаем кол-во сотрудников

# print(f"Текущее количество сотрудников: {len(employes)}")

# print(employes)

#--------------------------------------------------------------------------------------------------------------------------

class Employee:
    def __init__(self, name, salary, on_vocation, is_good_employee) -> None:
        self.name = name
        self.salary = salary
        self.is_good_employee = is_good_employee
        #Поля для статуса отпуска сотрудника
        self.on_vocation = on_vocation

    # Метод получения текущей информации по сотруднику
    def get_info(self):
        return f"У сотрудника по имени {self.name} З/П в месяц: {self.salary}, В отпуске? {self.on_vocation}. Хороший сотрудник? {self.is_good_employee}"




# создаем список сотрудников

employees = [Employee("Игорь", 200_000, False, True), Employee("Никита", 200_000, True, True), Employee("Роман", 300_000, True, True), Employee("Petya", 100_000, False, False)]



#------------Добавляем нового сотрудника 

new_name = input("Введите имя:")
new_salary = int(input("Введите зарплату:"))
new_on_vocation = input("Сотрудник в отпуске? True/False: ")
new_is_good_employee = input("Сотрудник выполняет работу качественно? True/False: ")

employees.append(Employee(new_name,new_salary, new_on_vocation, new_is_good_employee))



# ---------- Выводим info о сотрудниках
for employee in employees:
    print(employee.get_info())

# ---------- Увольняем сотрудника, работающего не качественно
for employ in employees:
    if employ.is_good_employee == False:
        employees.remove(employ)

for employee in employees:
    print(employee.get_info())