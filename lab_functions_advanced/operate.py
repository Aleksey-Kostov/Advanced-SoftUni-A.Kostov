from functools import reduce


def operate(sing, *args):
    def add():
        return reduce(lambda a, b: a + b, args)

    def subtract():
        return reduce(lambda a, b: a - b, args)

    def multiply():
        return reduce(lambda a, b: a * b, args)

    def divide():
        return reduce(lambda a, b: a / b, args)

    if sing == "+":
        return add()
    if sing == "-":
        return subtract()
    if sing == "*":
        return multiply()
    if sing == "/":
        return divide()

print(operate("*", 3, 4))