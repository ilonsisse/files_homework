class Cookbook:
    """Represents a tool for working with culinary recipes.
    Methods: read_cookbook, get_shop_list_by_dishes.

    """

    def read_cookbook(self):
        """ Reads file in format like recipes.txt line by line and returns file data as cook_book
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
        """Takes a list of dishes from cook_book and the number of people and returns a dictionary with
        the name of the ingredients and their quantities for the dish.
        2nd task.

        """
        shop_list = {}
        cook_book = self.read_cookbook()
        for dish in dishes:
            if dish in cook_book:
                for ingredient in cook_book[dish]:
                    ingredient['quantity'] *= person_count
                    if ingredient['ingredient_name'] in shop_list:
                        # Увеличивает количество ингредиента в списке покупок на количество ингредиента из текущего
                        # блюда
                        shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']
                    else:
                        # Если ингредиент отсутствует в списке покупок, то добавляет его
                        shop_list[ingredient['ingredient_name']] = {
                            'quantity': ingredient['quantity'],
                            'measure': ingredient['measure']
                        }

        return shop_list


my_cookbook = Cookbook()
print(my_cookbook.read_cookbook())
print(my_cookbook.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print(my_cookbook.get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
