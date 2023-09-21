from collections import deque

bees = deque([int(num) for num in input().split()])
nectar = deque([int(num) for num in input().split()])
actions = deque(input().split())
result = 0

commands = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue
    if current_nectar > 0:
        command = actions.popleft()
        result += abs(commands[command](current_bee, current_nectar))

print(f"Total honey made: {result}")
if bees:
    print(f"Bees left: {', '.join(str(num) for num in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(num) for num in nectar)}")