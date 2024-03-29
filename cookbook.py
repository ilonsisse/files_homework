class Cookbook:

    def read_cookbook(self):
        """ This function reads file in format like recipes.txt line by line and returns file data as cook_book
        dictionary.
        1st task.

        """
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

    def get_shop_list_by_dishes(self, dishes, person_count):
        """This function takes a list of dishes from cook_book and the number of people and returns a dictionary with
        the name of the ingredients and their quantities for the dish.
        2nd task.

        """
        shop_list = {}
        cook_book = self.read_cookbook()
        for dish in dishes:
            if dish in cook_book:
                for ingredient in cook_book[dish]:
                    ingredient['quantity'] *= person_count
                    shop_list.setdefault(ingredient['ingredient_name'], ingredient)

        return shop_list


my_cookbook = Cookbook()
print(my_cookbook.read_cookbook())
print(my_cookbook.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
