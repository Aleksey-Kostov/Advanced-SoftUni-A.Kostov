def stock_availability(*args):
    commands = args[1]
    cupcakes_boxes = args[0]
    index_commands = args.index(commands)
    next_item = args[index_commands + 1:]
    if commands == "delivery":
        for item in next_item:
            cupcakes_boxes.append(item)
    elif commands == "sell":
        if next_item:
            for current_item in next_item:
                if str(current_item).isdigit():
                    if len(cupcakes_boxes) >= current_item:
                        cupcakes_boxes = cupcakes_boxes[current_item:]
                else:
                    while current_item in cupcakes_boxes:
                        cupcakes_boxes.remove(current_item)
        else:
            if cupcakes_boxes:
                cupcakes_boxes.remove(cupcakes_boxes[0])
    return cupcakes_boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
