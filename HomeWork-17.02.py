import random
# Напишіть гру Правда або Дія.
# Опис:
# 1. Спочатку, введіть імена гравців.
# 2. Кожен гравець по черзі обирає "Правда" або "Дія".
# 3. Якщо гравець обрав "Правда", йому задається
# запитання, на яке він повинен відповісти правдиво.
# 4. Якщо "Дія", гравець повинен виконати вказане
# завдання.
# 5. Після завершення кожного раунду, виведіть
# результати.
# Функції:
#  get_player_names(): Запитайте імена гравців і поверніть
# їх у вигляді списку.
#  ask_truth_or_dare(player): Функція, яка приймає ім'я
# гравця та запитує його, чи обирати "Правда" чи "Дія".
#  ask_truth_question(player): Функція, яка приймає ім'я
# гравця, виберє одне запитання випадковим чином та
# просить гравця дати відповідь.
#  perform_dare(player): Функція, яка приймає ім'я гравця
# та вибирає одне завдання випадковим чином та
# просить гравця виконаи його.
# Домашнє завдання
#  play_game(players): Функція, яка керує ходом гри.
# Послідовно запитайте кожного гравця, чи обирати
# "Правда" чи "Дія", а потім відповідно викликайте
# функцію ask_truth_question або perform_dare.
# Константи:
#  questions – список питань
#  dares – список завдань


# get_player_names(): Запитайте імена гравців і поверніть
# # їх у вигляді списку.

questions = [
    "Який твій найбільший страх?",
    "Яку найбільшу брехню ти говорив?",
    "Хто тобі подобається?",
    "Який твій найсмішніший випадок у житті?",
    "Що б ти змінив у собі?"
]

dares = [
    "Заспівай пісню.",
    "Станцюй 30 секунд.",
    "Розкажи смішний анекдот.",
    "Покажи смішну гримасу.",
    "Зроби 10 присідань."
]


def get_player_names():
    players = []

    count = int(input("Введіть кількість гравців: "))
    for i in range(count):
        name = input(f"Введіть ім'я гравця {i + 1}: ")
        players.append(name)
    return players



def ask_truth_or_dare(player):
    choice = input(f"{player}, оберіть 'Правда' або 'Дія': ").lower()
    return choice


def ask_truth_question(player):
    question = random.choice(questions)

    print(f"{player}, ваше запитання:")
    print(question)

    answer = input("Ваша відповідь: ")

    return f"{player} відповів: {answer}"


def perform_dare(player):
    dare = random.choice(dares)

    print(f"{player}, ваше завдання:")
    print(dare)

    return f"{player} виконав завдання: {dare}"


def play_game(players):
    results = []

    for player in players:
        choice = ask_truth_or_dare(player)

        if choice == "правда":
            result = ask_truth_question(player)

        elif choice == "дія":
            result = perform_dare(player)

        else:
            print("Неправильний вибір! Пропуск ходу.")
            result = f"{player} пропустив хід."

        results.append(result)


    print("Результати раунду:")
    for r in results:
        print(r)


players = get_player_names()
play_game(players)