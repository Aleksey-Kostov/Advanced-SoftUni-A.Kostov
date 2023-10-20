from collections import deque


def check_sum(total_sum, current_dict):
    fireworks_dict = current_dict
    is_found = False
    is_perfect = False
    if total_sum % 3 == 0 and total_sum % 5 != 0:
        fireworks_dict["Palm Fireworks"] += 1
        is_found = True
    elif total_sum % 3 != 0 and total_sum % 5 == 0:
        fireworks_dict["Willow Fireworks"] += 1
        is_found = True
    elif total_sum % 3 == 0 and total_sum % 5 == 0:
        fireworks_dict["Crossette Fireworks"] += 1
        is_found = True
    if (fireworks_dict["Palm Fireworks"] >= 3 and
            fireworks_dict["Willow Fireworks"] >= 3 and
            fireworks_dict["Crossette Fireworks"] >= 3):
        is_perfect = True
    return fireworks_dict, is_found, is_perfect


dict_fireworks = {"Palm Fireworks": 0, "Willow Fireworks": 0, "Crossette Fireworks": 0}
found = False
perfect = False
counter = 0

firework_effects = deque(int(x) for x in input().split(", "))
last_explosive_power = [int(x) for x in input().split(", ")]

while firework_effects and last_explosive_power:
    current_effect = firework_effects.popleft()
    current_explosive = last_explosive_power.pop()
    current_sum = current_effect + current_explosive
    if current_explosive <= 0:
        firework_effects.appendleft(current_effect)
        continue
    elif current_effect <= 0:
        last_explosive_power.append(current_explosive)
        continue
    dict_fireworks, found, perfect = check_sum(current_sum, dict_fireworks)
    if perfect:
        break
    if not found:
        current_effect -= 1
        firework_effects.append(current_effect)
        last_explosive_power.append(current_explosive)


if perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if last_explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, last_explosive_power))}")

for k, v in dict_fireworks.items():
    print(f"{k}: {v}")
