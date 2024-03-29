with open('recipes.txt', 'r') as recipes:
    cook_book = {}
    for line in recipes:
        dish_name = None