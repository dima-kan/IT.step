import json
import pickle


def add_band(groups):
    name = input("Введіть назву гурту: ")
    if name not in groups:
        groups[name] = []
        print("Гурт додано.")
    else:
        print("Такий гурт вже існує.")


def add_album(groups):
    name = input("Введіть назву гурту: ")

    if name in groups:
        album = input("Введіть назву альбому: ")
        groups[name].append(album)
        print("Альбом додано.")
    else:
        print("Гурт не знайдено.")


def save_json(groups):
    with open("groups.json", "w", encoding="utf-8") as file:
        json.dump(groups, file, ensure_ascii=False)

    print("Дані збережено")


def load_json():
    with open("groups.json", "r", encoding="utf-8") as file:
        groups = json.load(file)

    print("Дані завантажено")
    return groups


def save_pickle(groups):
    with open("groups.pkl", "wb") as file:
        pickle.dump(groups, file)

    print("Дані збережено")


def load_pickle():
    with open("groups.pkl", "rb") as file:
        groups = pickle.load(file)
    print("Дані завантажено")
    return groups


groups = {}

add_band(groups)
add_band(groups)

add_album(groups)
add_album(groups)

print("Початкові дані:")
print(groups)

save_json(groups)
save_pickle(groups)

groups_json = load_json()
print("Завантажено з JSON:")
print(groups_json)

groups_pickle = load_pickle()
print("Завантажено з Pickle:")
print(groups_pickle)