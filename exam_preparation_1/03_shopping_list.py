def shopping_list(budget, **kwargs):
    while True:
        if len(kwargs) >= 5:
            for i in range(5):
                for item in kwargs.items():
                    amount = float(item[0]) * int(item[1])
        else:
            pass


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
