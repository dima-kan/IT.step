import random
# Ввід, вивід та арифметичні операції
# 1. Добуток двох чисел
# Введіть два числа з клавіатури та виведіть результат їхнього множення.
# Підказка: Використайте input() та перетворення на int або float.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# total = num1 * num2





# 2. Середнє арифметичне
# Введіть три числа. Обчисліть та виведіть їх середнє арифметичне.
# Підказка: Середнє = сума / кількість чисел.


# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))
#
# total=num1+num2+num3
# avg = total/3





# 3. Площа прямокутника
# Введіть довжину та ширину прямокутника. Виведіть його площу.
# Підказка: Площа = довжина * ширина.

# width = int(input("Enter width: "))
# height = int(input("Enter height: "))
# area = width * height


# 4. Периметр трикутника
# Введіть три сторони трикутника. Обчисліть та виведіть периметр.
# Підказка: Периметр = a + b + c.

# side1 = int(input("Enter side 1: "))
# side2 = int(input("Enter side 2: "))
# side3 = int(input("Enter side 3: "))
#
#
# perimeter = side1 + side2 + side3





# 5. Конвертація температури
# Введіть температуру в градусах Цельсія. Перетворіть і виведіть значення у
# Фаренгейтах.
# Підказка: Формула: F = C * 9/5 + 32.

# celsius_temp = int(input("Enter temperature in Celsius: "))
# fahrenheit_temp = celsius_temp * 9/5 + 32
# print(fahrenheit_temp)


# 6. Конвертація часу
# Введіть кількість хвилин. Виведіть відповідь у форматі "X год Y хв".
# Підказка: Використайте оператори // та %.

# number_of_minutes = int(input("enter number of minutes: "))
# clock = number_of_minutes // 60
# minutes = number_of_minutes % 60
#
# print(f"{clock}h {minutes} minutes")




# 7. Остача від ділення
# Введіть два числа. Виведіть остачу від ділення першого на друге.
# Підказка: Оператор % повертає остачу.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# remaining_amount = num1 % num2
# print(remaining_amount)
#



# 8. Перевірка парності
# Введіть ціле число. Визначте та виведіть, чи є воно парним чи непарним.
# Підказка: Число парне, якщо n % 2 == 0.


# num1 = int(input("Enter first number: "))
#
# if num1 % 2 == 0:
#     print("even")
# else:
#     print("odd")



# 9. Ділення на 3 і 5
# Введіть ціле число. Визначте, чи ділиться воно одночасно на 3 і на 5. Виведіть
# відповідь.
# Підказка: Умова: n % 3 == 0 and n % 5 == 0.
#
# num1 = int(input("Enter first number: "))
#
# if num1 % 5 == 0 and num1 % 3 == 0:
#     print("Діляться на 3 и на 5 ")
# else:
#     print(" не діляться на 3 и на 5 ")




# 10. Вартість зі знижкою
# Введіть початкову ціну товару та відсоток знижки. Обчисліть і виведіть кінцеву
# вартість.
# Підказка: Кінцева ціна = ціна * (1 - знижка / 100).

# price_item = int(input("enter price"))
# percent = int(input("enter percent"))
# total = price_item * (1 -percent / 100)


# Умовні оператори
# 11. Більше з двох чисел
# Введіть два числа. Визначте і виведіть, яке з них більше, або повідомте, що вони рівні.
# Підказка: Використайте if / elif / else.


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if num1 > num2:
#     print(num1, "is greater than num2")
# elif num1 < num2:
#     print(num2, "is less than num1")
# else:
#     print("number 1 equals number 2")
#


# 12. Найбільше з трьох чисел
# Введіть три числа. Знайдіть і виведіть найбільше з них без використання функції
# max().

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num_max = max(num1, num2, num3)
# print(num_max)
# Підказка: Порівнюйте попарно: якщо a > b і a > c, то a — найбільше.

# 13. Знак числа
# Введіть число. Визначте та виведіть: додатне воно, від'ємне, чи нуль.
# Підказка: Три гілки: n > 0, n < 0, n == 0.


# num1 = int(input("Enter first number: "))
# if num1 >0:
#     print("num1 is greater than 0")
# elif num1 < 0:
#     print("num1 is less than 0")
# else:
#     print("num1 is equal to 0")



# 14. Оцінка за балом
# Введіть бал від 0 до 100. Виведіть оцінку: 90–100 → 12 балів, 75–89 → 9–11, 60–74 →
# 6–8, нижче 60 → незадовільно.
# Підказка: Використайте elif для кожного діапазону.

# # Введення балу
# ball = int(input("Введіть бал від 0 до 100: "))
#
# # # Перевірка та виведення оцінки
# # if 90 <= ball <= 100:
# #     print("12 балів")
# # elif 75 <= ball <= 89:
# #     print("9-11 балів")
# # elif 60 <= ball <= 74:
# #     print("6-8 балів")
# # elif 0 <= ball < 60:
# #     print("незадовільно")
# # else:
# #     print("Помилка: бал має бути від 0 до 100")
#


# 15. Високосний рік
# Введіть рік. Визначте, чи є він високосним, і виведіть відповідь.
# Підказка: Рік високосний, якщо ділиться на 4, але не на 100, або ділиться на 400.

# year = int(input("enter year"))
# if year % 4 == 0 and year % 100 != 0:
#     print("leap year")
# else:
#     print("not leap year")





# 16. Існування трикутника
# Введіть три сторони. Перевірте, чи може існувати трикутник з такими сторонами.
# Підказка: Трикутник існує, якщо сума будь-яких двох сторін більша за третю.

# a = float(input("Введіть сторону a: "))
# b = float(input("Введіть сторону b: "))
# c = float(input("Введіть сторону c: "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("Трикутник з такими сторонами існує")
# else:
#     print("Трикутник з такими сторонами не існує")



# 17. Тип трикутника
# Введіть три сторони. Визначте тип трикутника: рівносторонній, рівнобедрений або
# різносторонній.
# Підказка: Рівносторонній: a==b==c; рівнобедрений: дві сторони рівні; решта —
# різносторонній.


# a = float(input("Введіть сторону a: "))
# b = float(input("Введіть сторону b: "))
# c = float(input("Введіть сторону c: "))
# if a == b == c:
#     print("рівносторонній")
# elif a == b or b == c or c == a:
#     print("рівнобедрений")
# else:
#     print("різносторонній")



# 18. Перевірка пароля
# Задайте правильний пароль у коді. Введіть пароль з клавіатури та виведіть, чи він
# правильний.
# Підказка: Порівняйте введений рядок з еталонним через ==.


# PASSWORD = "password"
# password = input("Enter your password: ")
# if password == PASSWORD:
#     print("Password is correct")

# 19. Система входу
# Задайте логін і пароль у коді. Введіть їх з клавіатури. Виведіть "Вхід успішний" або
# "Помилка".
# Підказка: Перевіряйте обидві умови одночасно через and.

# LOGIN = "8442"
# PASSWORD = "password"
# password = input("Enter your password: ")
# login = input("Enter your login: ")
#
# if password == PASSWORD and login == LOGIN:
#     print("Password and login correct")
# else:
#     print("Wrong password or login ")



# 20. Пора року
# Введіть номер місяця (1–12). Виведіть відповідну пору року.


# Введення номера місяця
# month = int(input("Введіть номер місяця (1–12): "))
#
# if month == 12 or month == 1 or month == 2:
#     print("winter")
# elif 3 <= month <= 5:
#     print("spring")
# elif 6 <= month <= 8:
#     print("summer")
# elif 9 <= month <= 11:
#     print("autumn")
# else:
#     print("номер місяця має бути від 1 до 12")



# Цикл while
# 21. Числа від 1 до 20
# Використовуючи цикл while, виведіть усі числа від 1 до 20 через пробіл або кожне на
# новому рядку.
# Підказка: Ініціалізуйте лічильник i = 1, збільшуйте на 1 поки i <= 20.

# i = 0
# while True:
#     i+=1
#     print(i)
#     if i==20:
#         break


# 22. Числа від 20 до 1
# Використовуючи цикл while, виведіть усі числа від 20 до 1 у зворотному порядку.
# Підказка: Ініціалізуйте i = 20, зменшуйте на 1 поки i >= 1.



# i = 20
# while i > 0:
#     print(i)
#     i-=1


# 23. Сума від 1 до N
# Введіть число N. За допомогою while обчисліть і виведіть суму всіх чисел від 1 до N.
# Підказка: Накопичуйте суму: total += i на кожному кроці.
# n = int(input("Enter a number: "))
# i = 1
# total = 0
# while i <= n:
#     total += 1
#     i += 1
# print(total)


# 24. Добуток від 1 до N
# Введіть число N. За допомогою while обчисліть добуток усіх чисел від 1 до N
# (факторіал).
# Підказка: Ініціалізуйте result = 1, множте на i на кожному кроці.
# n = int(input("Enter a number: "))
# i = 1
# total = 1
# while i <= n:
#     total *= i
#     i += 1
# print(total)


# 25. Факторіал числа
# Введіть ціле невід'ємне число N. Обчисліть і виведіть його факторіал (N!).
# Підказка: Факторіал 0 і 1 дорівнює 1. Далі: n! = 1 * 2 * 3 * ... * n.
# n = int(input("Enter a number: "))
#
# if n < 0:
#     print("N is negative")
# else:
#     i = 1
#     total = 1
#     while i <= n:
#         total *= i
#         i += 1
#     print(total)




# 26. Введення до нуля
# Постійно просіть користувача вводити числа, поки він не введе 0. Тоді завершіть
# програму.
# Підказка: Умова циклу: while True, вихід — break або while число != 0.


# while True:
#     n= int(input("enter a number"))
#     print(n)
#     if n == 0:
#         break



# 27. Кількість введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть кількість введених чисел
# (без нуля).

# total = 0
# while True:
#     n =int(input("enter the number"))
#     if n == 0:
#         break
#     total += 1
# print(total)
# Підказка: Використайте лічильник count, збільшуйте після кожного введення.

# 28. Сума введень
# Просіть вводити числа до введення 0. Порахуйте і виведіть суму всіх введених чисел
# (без нуля).
# Підказка: Накопичуйте суму total += число на кожній ітерації.

# total = 0
# while True:
#     n =int(input("enter the number"))
#     if n == 0:
#         break
#     total += n
# print(total)




# 29. Вгадай число
# Програма «загадує» число від 1 до 100 (задайте у коді). Користувач вводить здогадки,
# отримуючи підказки «більше» або «менше». Виводьте кількість спроб.
# Підказка: Для випадкового числа можна використати import random та random.randint(1,
# 100).
# n= random.randint(1,100)
# count = 0
# while True:
#     print(n)
#     num = int(input("enter a number"))
#     count += 1
#     if num > n:
#         print("the number is greater than the number")
#     elif num < n:
#         print("the number is less than the number")
#     if n == num:
#         print("the number is equal to the number")
#         break




# 30. Таблиця множення (while)
# Введіть число N. За допомогою while виведіть таблицю множення для цього числа від
# 1 до 10.
# Підказка: Виводьте рядки виду: "N * i = результат
# i = 0
# n= int(input("enter a number"))
# while True:
#     i += 1
#     total = i*n
#     print(total)
#
#     if i == 10:
#         break


