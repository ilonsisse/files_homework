class Cookbook:

    def read_cookbook(self):
        with open('recipes.txt', 'r') as recipes:
            cook_book = {}
            ingredients = []

            for line in recipes:
                dish_name = line.strip()
                ingredients_number = int(recipes.readline().strip())
                for ingredient in range(ingredients_number):
                    ingredient_summary = recipes.readline().strip().split(sep='|')
                    ingredients.append({
                        'ingredient_name': ingredient_summary[0],
                        'quantity': ingredient_summary[1],
                        'measure': ingredient_summary[2]
                    })

            recipes.readline()
            cook_book[dish_name] = ingredients
            return cook_book


my_cookbook = Cookbook()
print(my_cookbook.read_cookbook())
