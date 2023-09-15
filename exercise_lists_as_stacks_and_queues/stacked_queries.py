n = int(input())
numbers_stack = []

for _ in range(n):
    command = input().split()
    current_command = command[0]
    if current_command == "1":
        number = int(command[1])
        numbers_stack.append(number)
    elif numbers_stack:
        if current_command == "2":
            numbers_stack.pop()
        elif current_command == "3":
            print(max(numbers_stack))
        elif current_command == "4":
            print(min(numbers_stack))


while numbers_stack:
    print(numbers_stack.pop(), end="")
    if numbers_stack:
        print(", ", end="")
