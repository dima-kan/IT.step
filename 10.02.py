# Напишіть функцію, яка повертає суму чисел з
# списку. Список передається як параметр
# def sum_list(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
#

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_list(nums))

# Напишіть функцію, яка повертає найбільше число з
# списку. Список передається як параметр.

# def max_list(items):
#     return max(items)
#

# items = [ 6,2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(min_list(items))

# Напишіть функцію, яка повертає кількість простих чисел з
# списку. Список передається як параметр.
# Для цього завдання вам потрібно написати функцію, яка
# отримує число як параметр, та повертає True якщо воно
# просте, та False в протилежному випадку.

# Напишіть функцію, яка видаляє всі від’ємні числа зі
# списку. Список передається як параметр. Функція має
# повернути кількість видалених чисел.
# def remove_negative(nums):
#     new_nums = nums.copy()
#     removed = 0

#     for num in nums:
#         if num <= 0:
#             removed += 1
#             new_nums.remove(num)
#     return removed

# nums = [1, -7, 7, -7, -7, -8, -4, -7, -7]
# removed = remove_negative(nums)
# print(removed)


# Напишіть функцію, яка шукає певне число в списку.
# Функція повинна повертати список усіх індексів цього
# Практичне завдання
# числа в списку. Якщо числа немає в списку, то потрібно
# повернути порожній список. Список та число
# передаються як два параметри.

# def find_all_indices(lst, number):
#     indices = []

#     for i in range(len(lst)):
#         if lst[i] == number:
#             indices.append(i)
#     return indices


# my_list = [1, 3, 7, 3, 5, 3]
# num_to_find = 3
#
# result = find_all_indices(my_list, num_to_find)
# print(result)


# Напишіть функцію, рахує факторіал кожного
# елемента списку. Результатом має бути список з
# факторіалами.
# Факторіалом числа n (позначають n!) називаю
# добуток усіх чисел від 1 до n. Наприклад 6! =
# 1*2*3*4*5*6. Якщо число від’ємне, то вважайте що
# його факторіал рівний Nonе. Факторіал число 0 вважають
# рівним 1.

# def factorial_list(numbers):
#     result = []
#     for n in numbers:
#         if n < 0:
#             result.append(None)
#         elif n == 0:
#             result.append(1)
#         else:
#             f = 1
#             for i in range(1, n + 1):
#                 f *= i
#             result.append(f)
#     return result
#

# nums = [5, 0, -3, 6]
# print(factorial_list(nums))


# def count_primes(lst):
#     count = 0
#     for n in lst:
#         if n < 2:
#             continue
#         prime = True
#         j = 2
#         while j < n:
#             if n % j == 0:
#                 prime = False
#                 break
#             j += 1
#         if prime:
#             count += 1
#     return count
#
#
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(count_primes(numbers))
