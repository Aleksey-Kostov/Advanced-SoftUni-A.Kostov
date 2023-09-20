from collections import deque

sequences_one = deque(set(int(x) for x in input().split()))
sequences_two = deque(set(int(x) for x in input().split()))

n = int(input())

for i in range(n):
    data = input().split()
    current_command = data[0] + " " + data[1]
    numbers_data = data[2:]
    if current_command == "Add First":
        pass
    elif current_command == "Add Second ":
        pass
    elif current_command == "Remove First":
        pass
    elif current_command == "Remove Second":
        pass
    elif current_command == "Check Subset":
        pass
