string = input()
stack_string = list(string)

while stack_string:
    last_char = stack_string.pop()
    print(last_char, end="")
