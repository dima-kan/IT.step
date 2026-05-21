import random
import json
import os


def new_game(wins, losses):
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Комп'ютер загадав число від 1 до 100.")

    while True:
        guess = int(input("Введіть ваше число: "))
        attempts += 1

        if guess < secret_number:
            print("Більше")
        elif guess > secret_number:
            print("Менше")
        else:
            print(f"Ви вгадали число за {attempts} спроб.")

            if attempts < 5:
                print("Переміг користувач")
                wins += 1
            else:
                print("Переміг комп'ютер")
                losses += 1
            break

    return wins, losses


def show_result(wins, losses):
    print("Результати:")
    print(f"Перемоги користувача: {wins}")
    print(f"Перемоги комп'ютера: {losses}")


def save_data(wins, losses):
    data = {
        "wins": wins,
        "losses": losses
    }

    with open("game_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    print("Дані успішно збережено у файл.")


def load_data():
    with open("game_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print("Дані успішно завантажено.")
    return data["wins"], data["losses"]


def menu():
    wins = 0
    losses = 0

    while True:
        print("Меню:")
        print("1 - Почати нову гру")
        print("2 - Вивести результат")
        print("3 - Зберегти дані")
        print("4 - Завантажити дані")
        print("5 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            wins, losses = new_game(wins, losses)
        elif choice == "2":
            show_result(wins, losses)
        elif choice == "3":
            save_data(wins, losses)
        elif choice == "4":
            wins, losses = load_data()
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


menu()