number_of_car = int(input())
registration_set = set()

for _ in range(number_of_car):
    registration_number = input().split(", ")
    if registration_number[0] == "IN":
        registration_set.add(registration_number[1])
    elif registration_number[0] == "OUT":
        registration_set.remove(registration_number[1])

if registration_set:
    for number in registration_set:
        print(number)
else:
    print("Parking Lot is Empty")


