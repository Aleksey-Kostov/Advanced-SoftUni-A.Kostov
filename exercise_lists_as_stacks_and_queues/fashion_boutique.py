clothes = [int(x) for x in input().split()]
capacity_rack = int(input())

rack_counter = 0

while clothes:
    current_capacity = capacity_rack
    rack_counter += 1
    while clothes and clothes[-1] <= current_capacity:
        current_clothes = clothes.pop()
        current_capacity -= current_clothes

print(rack_counter)
