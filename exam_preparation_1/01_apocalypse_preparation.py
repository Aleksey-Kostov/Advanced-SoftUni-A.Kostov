from collections import deque

textiles = deque(int(x) for x in input().split())
medicament = [int(x) for x in input().split()]

needed_kit = {"Patch": 30, "Bandage": 40, "MedKit": 100}
healing_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicament:
    first_textiles = textiles.popleft()
    last_medicament = medicament.pop()
    current_sum = first_textiles + last_medicament
    if current_sum >= needed_kit["MedKit"]:
        if current_sum == needed_kit["MedKit"]:
            healing_items["MedKit"] += 1
        else:
            diff = current_sum - needed_kit["MedKit"]
            medicament[-1] += diff
            healing_items["MedKit"] += 1
    elif current_sum == needed_kit["Bandage"]:
        healing_items["Bandage"] += 1
    elif current_sum == needed_kit["Patch"]:
        healing_items["Patch"] += 1
    else:
        medicament.append(last_medicament + 10)


if not medicament and not textiles:
    print("Textiles and medicaments are both empty.")
else:
    if not medicament:
        print(f"Medicaments are empty.")
    if not textiles:
        print(f"Textiles are empty.")
for k, v in sorted(healing_items.items(), key=lambda x: (-x[1], x[0])):
    if v > 0:
        print(f"{k} - {v}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
if medicament:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicament))}")
