import threading

numbers = []

finished_input = threading.Event()

def input_numbers():
    while True:
        value = input("Число: ")

        if value == "":
            break

        number = float(value)
        numbers.append(number)

    finished_input.set()


def calculate_sum():
    finished_input.wait()

    total = sum(numbers)

    print("Сума чисел:", total)


def calculate_average():
    finished_input.wait()

    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
    else:
        average = 0

    print("Середнє арифметичне:", average)


thread1 = threading.Thread(target=input_numbers)
thread2 = threading.Thread(target=calculate_sum)
thread3 = threading.Thread(target=calculate_average)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
