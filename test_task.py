# Ввід, вивід та арифметичні операції
# 1. Добуток двох чисел
# Введіть два числа з клавіатури та виведіть результат їхнього множення.
# Підказка: Використайте input() та перетворення на int або float.
from sqlalchemy.sql.functions import percentile_cont

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

price_item = int(input("enter price"))
percent = int(input("enter percent"))
total = price_item * (1 -percent / 100)
