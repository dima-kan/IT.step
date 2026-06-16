# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.
from typing import List

# start = int(input("Enter a number: "))
# stop = int(input("Enter second number: "))
# total = 0
# for i in range(start, stop+1):
#
#     total +=i
# print(total)

# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

# total = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         total  += i
#
# print(total)


# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# words = input("Enter words: ")
# for letter in words:
#     print(letter)

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

# even_number = []
# list1 = []
# count_even_number = int(input("Введіть кількість чисел у списку "))
# for i in range(count_even_number):
#     num = int(input("enter a number: "))
#     list1.append(num)
#
# for i in list1:
#     if i % 2 == 0:
#         even_number.append(i)
# print(even_number)
#


# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.




# def  get_capital_letter_list(list1):
#     result = []
#
#     for word in list1:
#         if word and word[0].isupper():
#             result.append(word)
#
#     return result
#
# print(get_capital_letter_list(["Letter g4g4 ","word"]))


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python




# def get_find_ford(list1):
#     find_ford_word = "Python"
#     result = []
#
#     for word in list1:
#         if find_ford_word in word:
#             result.append(word)
#
#     return result
#
# print(get_find_ford(["Python","Java","C++""Python - це мова програмування "]))


# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.

# data = {}
#
# while True:
#     action = input("Введіть дію бо стоп для виходу")
#     if action == "стоп":
#         break
#
#     if action == "додати":
#         name = input("введіть ключ ")
#         value = input("введіть значення")
#
#         data[name] = value
#         print("succeed")
#
#     elif action == "видалити":
#         name = input("введіть ключ ")
#
#         if name in data:
#             del data[name]
#         print("succeed")
#
#     elif action == "знайти":
#         name = input("введіть ключ ")
#         if name in data:
#             print(data)
#



    # print(data)




# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.



class WebPage:
    def __init__(self, title:str, content:str, publish_date:str):
        self.title = title
        self.content = content
        self.publish_date = publish_date

    def _display_details(self):
        print(f"Заголовок {self.title}")
        print(f"Дата публікації {self.publish_date}")
        print(f"Вміст {self.content}")

class Website:
    def __init__(self, name:str, url:str):
        self.name = name
        self.url = url
        self.pages: List[WebPage] = []

    def _add_page(self,page:WebPage):
        self.pages.append(page)


    def _remove_page(self, title: str):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print(f"Сторінку {title} видалено")
                return
        print(f"Сторінку {title} не знайдено")

    def _display_info(self):
        print(f"Назва сайту {self.name}")
        print(f"URL сайту {self.url}")
        print("Сторінки сайту:")

        if not self.pages:
            print("Сторінок немає")
        else:
            for page in self.pages:
                print(f"{page.title}")



page1 = WebPage(
    "Головна",
    "Ласкаво просимо",
    "16.06.2026"
)

page2 = WebPage(
    "Новини",
    "Останні новини",
    "17.06.2026"
)

site = Website(
    "Мій сайт",
    "https://mysite.com"
)


site._add_page(page1)
site._add_page(page2)


site._display_info()


page1._display_details()

site._remove_page("Новини")
site._display_info()







