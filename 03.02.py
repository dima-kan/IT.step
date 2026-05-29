secret_word = "server"


while True:
    word = input("Введіть слово")

    letter_green = 0
    letter_yellow = 0

    if len(word) != len(secret_word):
        print("Слово повинно мати", len(secret_word), "літер")
        continue

    for i in range(0,len(secret_word)):
        if secret_word[i] == word[i]:
            letter_green += 1
        elif secret_word[i] in word:
            letter_yellow += 1

    print("Зелених:", letter_green)
    print("Жовтих:", letter_yellow)

    if word == secret_word:
        print("Ти вгадав слово!")
        break
    if word == "Exit":
        print(secret_word)
        break