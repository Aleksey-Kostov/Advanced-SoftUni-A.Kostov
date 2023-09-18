numbers = [int(x) for x in input().split()]

result = int(input())
target_number = set()
number_dict = {}

for number in numbers:
    current_number = result - number
    if current_number in numbers and current_number != number:
        target_number.add(current_number)
        numbers.remove(current_number)
        number_dict[number] = current_number

for key, value in number_dict.items():
    target = key + value
    print(f"{key} + {value} = {target}")
