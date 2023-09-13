from collections import deque

quantity_of_water = int(input())
name_of_people = input()
name_of_people_deq = deque()

while name_of_people != "Start":
    name_of_people_deq.append(name_of_people)
    name_of_people = input()

get_water = input().split()

while get_water[0] != "End":
    if len(get_water) != 1:
        quantity_of_water += int(get_water[1])
    else:
        if int(get_water[0]) <= quantity_of_water:
            quantity_of_water -= int(get_water[0])
            people_get_water = name_of_people_deq.popleft()
            print(f"{people_get_water} got water")
        else:
            people_get_water = name_of_people_deq.popleft()
            print(f"{people_get_water} must wait")
    get_water = input().split()

print(f"{quantity_of_water} liters left")
