def shopping_list(budget, **kwargs):
    amount = 0
    counter = 0
    result = ""
    if budget < 100:
        return "You do not have enough budget."
    else:
        for key, value in kwargs.items():
            price = float(value[0])
            quantity = int(value[1])
            amount = price * quantity
            if budget < amount:
                continue
            else:
                budget -= amount
                counter += 1
                if counter == 6:
                    break
                result += f"You bought {key} for {amount:.2f} leva.\n"
        return result


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
