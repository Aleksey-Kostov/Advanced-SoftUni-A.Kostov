from collections import deque
cups = deque(int(item) for item in input().split())
bottles = deque(int(item) for item in input().split())

wasted_water = 0

while cups and bottles:
    if bottles[-1] > cups[0]:
        wasted_water += bottles[-1] - cups[0]
        cups.popleft()
        bottles.pop()
    elif bottles[-1] == cups[0]:
        cups.popleft()
        bottles.pop()
    elif bottles[-1] < cups[0]:
        cups[0] -= bottles.pop()

if cups:
    cups = [str(item) for item in cups]
    print("Cups: " + " ".join(cups))
elif bottles:
    bottles = [str(item) for item in bottles]
    print("Bottles: " + " ".join(bottles))

print(f"Wasted litters of water: {wasted_water}")
