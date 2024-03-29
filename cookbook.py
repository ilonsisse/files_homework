class Cookbook:

    def read_cookbook(self):
        """ This function reads file line by line and returns file data as cook_book dictionary"""
        with open('recipes.txt', 'r') as recipes:
            cook_book = {}

            while True:  # Обработка файла с неизвестным количество строк
                dish_name = recipes.readline().strip()  # strip() удаляет лишние пробелы
                if not dish_name:  # Выходим из цикла, если дальше пустая строка
                    break

                ingredients_number = int(recipes.readline().strip())
                ingredients = []

                for ingredient in range(ingredients_number):
                    ingredient_summary = recipes.readline().strip().split(sep='|')  # split(sep='symbol') разделяет
                    # строку по символу и возвращает список
                    ingredients.append({
                        'ingredient_name': ingredient_summary[0].strip(),
                        'quantity': int(ingredient_summary[1].strip()),
                        'measure': ingredient_summary[2].strip()
                    })

                cook_book[dish_name] = ingredients

                # Пропускаем пустую строку между рецептами
                recipes.readline()

        return cook_book


my_cookbook = Cookbook()
print(my_cookbook.read_cookbook())
