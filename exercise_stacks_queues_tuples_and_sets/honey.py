from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]

symbols = deque(input().split())

total_honey = 0

while nectar and bees:
    if bees[0] <= nectar[-1]:
        current_nectar = nectar.pop()
        current_bee = bees.popleft()
        symbol = symbols.popleft()
        if symbol == "+":
            current_honey = current_nectar + current_bee
            total_honey += abs(current_honey)
        elif symbol == "-":
            current_honey = current_nectar - current_bee
            total_honey += abs(current_honey)
        elif symbol == "*":
            current_honey = current_nectar * current_bee
            total_honey += abs(current_honey)
        elif symbol == "/":
            if current_nectar == 0:
                continue
            current_honey = current_nectar / current_bee
            total_honey += abs(current_honey)
    elif bees[0] > nectar[-1]:
        nectar.pop()


print(f"Total honey made: {total_honey:.0f}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

