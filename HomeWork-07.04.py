# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self.time = time

    def __str__(self):
        return f" Назва страви: {self._name}"

    def __contains__(self, item):
        for ingredient in self._ingredients:
            if item == ingredient:
                return True
        return False

    def __gt__(self, other):
        return self.time > other.time

    def display_info(self):
        print(f"Назва страви: {self._name}")
        print(f"Час приготування: {self.time} хв.")
        print(f"Інгредієнти: {', '.join(self._ingredients)}")
        print(f"Рецепт: {self._text}")


recipe1 = Recipe(
    "Піца",
    ["борошно", "вода", "дріжджі", "томат", "сир"],
    "Готуємо тісто, додаємо інгредієнти та запікаємо",
    30,
)

recipe2 = Recipe(
    "Салат",
    ["томат", "огірок", "зелень", "олія"],
    "Нарізаємо овочі, додаємо зелень та поливаємо олією",
    10,
)
recipe3 = Recipe(
    "Суп",
    ["вода", "картопля", "морква", "м'ясо"],
    "Варимо всі інгредієнти до готовності",
    45,
)

recipes = [recipe1, recipe2, recipe3]
for recipe in recipes:
    if "томат" in recipe:
        print(recipe)

fastest_recipe = recipe1

if recipe2.time < fastest_recipe.time:
    fastest_recipe = recipe2

if recipe3.time < fastest_recipe.time:
    fastest_recipe = recipe3

print("Найшвидший рецепт:")
fastest_recipe.display_info()
