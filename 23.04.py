import json

# Є словник з логінами(ключ) та паролями(значення)
# користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.

FILENAME = "users.json"


def load_users():
    with open(FILENAME, encoding="UTF-8") as file:
        data = json.load(file)
        return data


def save_users(data):
    with open(FILENAME, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def add_users(data):
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    if login in data:
        print("Користувач вже існує")
        return
    data[login] = password


def delete_users(data):
    login = input("Введіть логін")
    if login not in data:
        print("Користувача з таким логіном не існує")
        return
    else:
        del data[login]


def change_password(data):
    login = input("Введіть логін:")

    if login not in data:
        print("Користувача з таким логіном не існує")
        return

    old_pass = input("Введіть старий пароль: ")

    if data[login] != old_pass:
        print("Невірний старий пароль!")
        return

    new_pass = input("Введіть новий пароль: ")
    data[login] = new_pass


def login_user(data: dict[str, str]):
    login = input("Логін: ")
    password = input("Пароль: ")
    if login in data and data[login] == password:
        print("Вхід виконано")


def main():
    data = load_users()

    while True:
        print("1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Змінити пароль")
        print("4. Вхід у систему")
        print("5. Перезавантажити з файлу")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_users(data)
        elif choice == "2":
            delete_users(data)
        elif choice == "3":
            change_password(data)
        elif choice == "4":
            login_user(data)
        elif choice == "5":
            data = load_users()
            print("Дані перезавантажено з файлу.")
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print(" Невірний вибір")


# дання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(fiename) – зберегти дані у файл(за
# замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за
# замовчуванням cart.json)


class Cart:
    def __init__(
        self,
        user: str,
    ):
        self.user = user
        self.total: float = 0.0
        self.items: list[str] = []

    def add(self, item: str, price: float):
        self.items.append(item)
        self.total += price

    def delete(self, item: str):
        if item in self.items:
            print("Item not found")
            return

        self.items.remove(item)

    def info(self):
        print(f"user {self.user}")
        print(f"total {self.total}")
        print(f"items {self.items}")

    def save(self, filename="cart.json"):
        data = {
            "user": self.user,
            "items": self.items,
            "total": self.total,
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load(self, filename="cart.json"):
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
        self.user = data["user"]
        self.items = data["items"]
        self.total = data["total"]


cart = Cart("Mary")
cart.add("Яблука", 45.50)
cart.add("Хліб", 25.00)
cart.add("Молоко", 32.80)


# Створіть файл settings.json з базовими налаштуваннями
# програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу


with open("settings.json", "w", encoding="utf-8") as file:
    data = {
        "size": "500x600",
        "color": "grey",
        "button_color": "bright grey",
        "placement_buttons": [100, 50],
        "instructions": "Be a simple kind of man",
    }

    json.dump(data, file, indent=4, ensure_ascii=False)


def load_settings():
    with open("settings.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


def save_settings(data):
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def change_size(new_size):
    data = load_settings()
    data["size"] = new_size
    save_settings(data)


def change_color(new_color):
    data = load_settings()
    data["color"] = new_color
    save_settings(data)


change_color("blue")
change_size("400x444")
