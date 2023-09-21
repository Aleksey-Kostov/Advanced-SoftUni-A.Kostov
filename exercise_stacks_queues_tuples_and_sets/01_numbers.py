sequences_one = set(int(x) for x in input().split())
sequences_two = set(int(x) for x in input().split())

n = int(input())

for i in range(n):
    data = input().split()
    current_command = data[0] + " " + data[1]
    numbers_data = [int(x) for x in data[2:]]
    if current_command == "Add First":
        sequences_one.update(numbers_data)
    elif current_command == "Add Second":
        sequences_two.update(numbers_data)
    elif current_command == "Remove First":
        sequences_one.difference_update(numbers_data)
    elif current_command == "Remove Second":
        sequences_two.difference_update(numbers_data)
    elif current_command == "Check Subset":
        print(sequences_one.issubset(sequences_two) or sequences_two.issubset(sequences_one))

print(*sorted(sequences_one), sep=", ")
print(*sorted(sequences_two), sep=", ")
