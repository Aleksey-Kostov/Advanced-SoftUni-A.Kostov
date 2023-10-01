def even_odd(*args):
    command = args[-1]
    even_nums = list(filter(lambda x: x % 2 == 0, args[:-1]))
    odd_nums = list(filter(lambda x: x % 2 != 0, args[:-1]))
    if command == "even":
        return even_nums
    return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
