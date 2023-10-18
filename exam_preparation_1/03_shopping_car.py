def shopping_cart(*args):
    meal_dict = {"Soup": [], "Pizza": [], "Dessert": []}
    result = ""
    counter = 0
    for meal in args:
        if meal != "Stop":
            meals = meal[0]
            product = meal[1]
            if len(meal_dict["Soup"]) <= 2 and meals == "Soup":
                if product not in meal_dict["Soup"]:
                    meal_dict[meals].append(product)
                    counter += 1
            if len(meal_dict["Pizza"]) <= 3 and meals == "Pizza":
                if product not in meal_dict["Pizza"]:
                    meal_dict[meals].append(product)
                    counter += 1
            if len(meal_dict["Dessert"]) <= 1 and meals == "Dessert":
                if product not in meal_dict["Dessert"]:
                    meal_dict[meals].append(product)
                    counter += 1
        else:
            break
    if counter == 0:
        return "No products in the cart!"
    sorted_result = sorted(meal_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for i in sorted_result:
        result += f"{i[0]}:\n"
        sort_result = sorted(i[1])
        for j in sort_result:
            result += f" - {j}\n"
    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


