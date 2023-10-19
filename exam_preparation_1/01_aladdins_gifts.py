from collections import deque


def check_sum(sum_gift, dict_gift):
    if sum_gift in range(100, 200):
        dict_gift["Gemstone"].append(sum_gift)
    elif sum_gift in range(200, 300):
        dict_gift["Porcelain Sculpture"].append(sum_gift)
    elif sum_gift in range(300, 400):
        dict_gift["Gold"].append(sum_gift)
    elif sum_gift in range(400, 500):
        dict_gift["Diamond Jewellery"].append(sum_gift)
    return dict_gift


materials = [int(x) for x in input().split()]
magik_level = deque(int(x) for x in input().split())

gift_dict = {"Gemstone": [], "Porcelain Sculpture": [], "Gold": [], "Diamond Jewellery": []}

is_found = False

while materials and magik_level:
    current_material = materials.pop()
    current_magik = magik_level.popleft()
    current_sum = current_material + current_magik
    gift_dict = check_sum(current_sum, gift_dict)
    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = current_material * 2 + current_magik * 3
            gift_dict = check_sum(current_sum, gift_dict)
        else:
            current_sum *= 2
            gift_dict = check_sum(current_sum, gift_dict)
    elif current_sum > 499:
        current_sum /= 2
        gift_dict = check_sum(round(current_sum), gift_dict)


if len(gift_dict["Gemstone"]) and len(gift_dict["Porcelain Sculpture"]):
    print(f"The wedding presents are made!")
elif len(gift_dict["Gold"]) and len(gift_dict["Diamond Jewellery"]):
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magik_level:
    print(f"Magic left: {', '.join(map(str, magik_level))}")

for k, v in sorted(gift_dict.items()):
    for i in v:
        if i:
            print(f"{k}: {len(v)}")
            break
