def shopping_cart(*args):
    meal_dict = {}
    for meal in args:
        if meal != "Stop":
            meals = meal[0]
            product = meal[1]
            if not meals in meal_dict:
                meal_dict[meals] = []
            meal_dict[meals].append(product)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
