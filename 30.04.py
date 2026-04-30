import threading


# numbers = []
#
#
# n = int(input("Введіть кількість елементів списку: "))
#
# for _ in range(n):
#     num = int(input(f"Введіть елемент"))
#     numbers.append(num)
#
# def find_max():
#     maximum = max(numbers)
#     print("Максимум у списку", maximum)
#
# def find_min():
#     minimum = min(numbers)
#     print("Мінімум у списку", minimum)
#
# thread_max = threading.Thread(target=find_max)
# thread_min = threading.Thread(target=find_min)
#
# thread_max.start()
# thread_min.start()
#
# thread_max.join()
# thread_min.join()
#
#

# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

# def find_sum(numbers,result):
#     print("start finding sum")
#     time.sleep(2)
#     result["sum"] =sum(numbers)
#
#
# def find_average(numbers,result):
#     print("start finding average")
#     time.sleep(2)
#     result["average"] =sum(numbers)/len(numbers)
#
#
# numbers = []
# result = {}
#
# n = int(input("Введіть кількість елементів "))
#
# for _ in range(n):
#     num = int(input("Введіть елемент "))
#     numbers.append(num)
#
#
#
#
#
# thread_sum = threading.Thread(target=find_sum,args=(numbers,result))
# thread_average = threading.Thread(target=find_average,args=(numbers,result))
# thread_sum.start()
# thread_average.start()


# thread_sum.join()
# thread_average.join()

#
# print(result)


# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.


# def write_even(numbers, result):
#     even_numbers = []
#
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#
#     result["even_count"] = len(even_numbers)
#
#     with open("even_numbers.txt", "w", encoding="utf-8") as f:
#         for num in even_numbers:
#             print(num, file=f)
#
#
# def write_odd(numbers, result):
#     odd_numbers = []
#
#     for num in numbers:
#         if num % 2 != 0:
#             odd_numbers.append(num)
#
#     result["odd_count"] = len(odd_numbers)
#
#     with open("odd_numbers.txt", "w", encoding="utf-8") as f:
#         for num in odd_numbers:
#             print(num, file=f)
#
#
# file_path = input("Введіть шлях до файлу")
#
# with open(file_path, "r", encoding="utf-8") as f:
#     numbers = f.read().split()
#     numbers= list(map(int,numbers))
#
# result = {}
#
# t1 = threading.Thread(target=write_even, args=(numbers, result))
# t2 = threading.Thread(target=write_odd, args=(numbers, result))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(result)


# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.


def search_word(file_path, word):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().lower()

    count = content.count(word)

    if count > 0:
        print(f"Слово '{word}' знайдено {count} разів.")
    else:
        print(f"Слово '{word}' немає у файлі.")


file_path = input("Введіть шлях до файлу: ")
word = input("Введіть слово для пошуку: ").lower()

search_thread = threading.Thread(target=search_word, args=(file_path, word))
search_thread.start()
search_thread.join()
