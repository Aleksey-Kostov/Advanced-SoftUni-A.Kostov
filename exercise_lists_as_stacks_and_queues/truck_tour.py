from collections import deque

petrol_pump_numbers = int(input())
petrol_pumps_deq = deque()
start_position = 0
stops = 0

for pump in range(petrol_pump_numbers):
    petrol, distance = input().split()
    petrol_pumps_deq.append([int(petrol), int(distance)])

while stops < petrol_pump_numbers:
    fuel = 0
    for i in range(petrol_pump_numbers):
        fuel += petrol_pumps_deq[i][0]
        destination = petrol_pumps_deq[i][1]
        if fuel < destination:
            petrol_pumps_deq.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_position)
