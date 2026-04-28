# import json
# import pickle

# Завдання 1
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle


# def add_product(items:list[str]):
#     product = input("Add product: ")
#     items.append(product)
#     print(f"{product} is added to the list")
#
#
# def show_product(items:list[str]):
#     for item in items:
#         print(item)
#
#
# def save_product_json(items:list[str]):
#     with open("products.json", "w",encoding="utf-8") as file:
#         json.dump(items, file,indent=4)
#
#
# def save_product_pickle(items:list[str]):
#     with open("products.pickle", "wb") as file:
#         pickle.dump(items, file)
#
#
# def load_product_pickle():
#     with open("products.pickle", "rb") as file:
#         return pickle.load(file)
#
#
#
# def load_product_json():
#     with open("products.json", "r",encoding="utf-8") as file:
#         return json.load(file)
#
#
# products =[]
# add_product(products)
#
# add_product(products)
# add_product(products)
#
#
# save_product_pickle(products)
# save_product_json(products)
#
# items_pkl = load_product_pickle()
# item_json = load_product_json()
#
# show_product(items_pkl)
# show_product(item_json)
# #


# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json


# class Student:
#     def __init__(self, name:str, specialization:str,):
#         self.name = name
#         self.specialization = specialization
#         self.grades = []
#
#
#     def add_grade(self, grade:int):
#         self.grades.append(grade)
#
#
#     def show_info(self):
#         print(f"Ім’я {self.name}")
#         print(f"Спеціалізація {self.specialization}")
#         if self.grades:
#             avg = sum(self.grades) / len(self.grades)
#             print(avg)
#         else:
#             avg = 0
#             print(avg)
#
#     def save_json(self):
#         with open("students.json", "wb") as file:
#             pickle.dump(self.get_state_dict(), file)
#
#     def get_state_dict(self):
#         return {
#             "name": self.name,
#             "specialization": self.specialization,
#             "grades": self.grades
#         }
#
#
#     def _set_state_dict(self, state_dict):
#         self.name = state_dict["name"]
#         self.specialization = state_dict["specialization"]
#         self.grades = state_dict["grades"]
#
#
#     def load_json(self):
#         with open("students.json", "r") as file:
#             state_dict = pickle.load(file)
#
#         self._set_state_dict(state_dict)
#
#     def save_pickle(self):
#         with open("students.pickle", "wb") as file:
#             pickle.dump(self.get_state_dict(), file)
#
#
#     def load_pickle(self):
#         with open("students.pickle", "rb") as file:
#             state_dict = pickle.load(file)
#
#         self._set_state_dict(state_dict)
#
#
# s1 = Student("Олена", "Комп'ютерні науки")
# s2 = Student("Іван", "Математика")
# s3 = Student("Марія", "Фізика")
#
#
# s1.add_grade(80)
# s2.add_grade(69)
# s3.add_grade(89)
#
#
#
# s1.show_info()
# s2.show_info()
# s3.show_info()
#
# s1.save_json()
# s2.save_json()
# s3.save_json()
#
#
# s1.save_pickle()
# s2.save_pickle()
# s3.save_pickle()
#
# s1.load_json()
# s2.load_json()
# s3.load_json()
#
# s1.show_info()
# s2.show_info()
# s3.show_info()


#
# Завдання
# Є словник з друзями, де ключ – людина, а значення –
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.


# Додати друга
# Зберігти файл
# Загрузити файл

#
#
# )
# def add_friends(friends:dict[str,list[str]]):
#
#
#     friend1 = input("Введіть ім'я:")
#     friend2 = input("Введіть ім'я:")
#
#     if friend1 not in friends:
#         friends[friend1] = []
#     if friend2 not in friends:
#         friends[friend2] = []
#
#     friends[friend1].append(friend2)
#     friends[friend2].append(friend1)
#
#
# def save_json(friends:dict[str,list[str]],filename:str = "friends.json",):
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(friends, file, indent=4, ensure_ascii=False)
#
#
# def load_json(filename:str = "friends.json")->dict[str,list[str]]:
#     with open(filename, "r", encoding="utf-8") as file:
#         return json.load(file)
#
# def save_pickle(friends:dict[str,list[str]],filename:str = "friends.pickle"):
#     with open(filename, "wb") as file:
#         pickle.dump(friends, file)
#
#
# def load_pickle(filename:str = "friends.pickle")->dict[str,list[str]]:
#     with open(filename, "rb") as file:
#         return pickle.load(file)
#
#
#
#
# friends ={}
# add_friends(friends)
# add_friends(friends)
#
# save_json(friends)
# loads_friends = load_json()
#
# print(loads_friends)
#
# save_pickle(friends)
# load_pickle()


# Реалізуйте телефонну книгу.
# Контакт містить:
# ім’я
# телефон
# email
# Функціонал:
# додати контакт
# видалити контакт
# знайти контакт за ім’ям
# показати всі контакти
# зберегти/завантажити через json
# зберегти/завантажити через pickle

#
# def add_contact(book: dict[str, dict[str, str]]) -> None:
#     name = input("Введіть ім'я")
#     phone = input("Введіть телефон")
#     email = input("Введіть емейл")
#
#     book[name] = {"phone": phone, "email": email}
#
#
# def save_json(book: dict[str, dict[str, str]]) -> None:
#     with open("book.json", "w") as file:
#         json.dump(book, file, ensure_ascii=False)
#
#
# book = {}
# add_contact(book)
# save_json(book)
