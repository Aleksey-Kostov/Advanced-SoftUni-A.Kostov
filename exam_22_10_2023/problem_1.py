from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

not_corresponding = False
counter = 0
reached_altitudes = []

for i in range(1, 5):
    current_fuel = initial_fuel.pop()
    current_consumption = consumption.popleft()
    check_fuel = fuel_needed.popleft()
    subtract = current_fuel - current_consumption
    if subtract < check_fuel:
        print(f"John did not reach: Altitude {i}")
        not_corresponding = True
        break
    else:
        counter += 1
        reached_altitudes.append(f"Altitude {i}")
        print(f"John has reached: Altitude {i}")

if counter < 4 and counter != 0:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitudes)}")
elif counter == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif counter == 4:
    print("John has reached all the altitudes and managed to reach the top!")
