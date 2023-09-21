from collections import deque

string = input().split()

numbers = deque()

for char in string:
    if char not in "-/+*":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            if char == "+":
                result = first_number + second_number
                numbers.appendleft(result)
            elif char == "-":
                result = first_number - second_number
                numbers.appendleft(result)
            elif char == "*":
                result = first_number * second_number
                numbers.appendleft(result)
            elif char == "/":
                result = first_number // second_number
                numbers.appendleft(result)

print(numbers[0])
