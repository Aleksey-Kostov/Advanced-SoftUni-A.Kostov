from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

LIMIT_PER_DAY = 300

current_caffeine = 0

while caffeine and energy_drinks:
    caffeine_for_energy = caffeine.pop()
    current_energy = energy_drinks.popleft()
    current_caffeine += (current_energy * caffeine_for_energy)
    if current_caffeine > LIMIT_PER_DAY:
        energy_drinks.append(current_energy)
        current_caffeine -= (current_energy * caffeine_for_energy)
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0


if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
