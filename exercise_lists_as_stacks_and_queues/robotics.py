from collections import deque

type_of_robots = input().split(";")
robots_deq = deque()
product_list = []
all_robots_deque = deque()
current_seconds = 0

for robot in type_of_robots:
    if robot not in robots_deq:
        robots_deq.append(robot)


hours, minutes, seconds = input().split(":")

product = input()
while product != "End":
    product_list.append(product)
    product = input()

for prod in range(len(product_list)):
    if robots_deq:
        robot_name = robots_deq.popleft().split(", ")
        name_robot, time_robot = robot_name[0].split("-")
        if name_robot not in all_robots_deque:
            all_robots_deque.append([name_robot, time_robot])
    else:
        robot_name = all_robots_deque[-1][0]
        robot_time = all_robots_deque[-1][1]
        current_seconds = int(robot_time) + int(robot_time)
        all_robots_deque.append([robot_name, current_seconds])

for detail in product_list:
    current_robot = all_robots_deque.popleft()[0]
    seconds = (int(seconds) + 1)
    print(f"{current_robot} - {detail} [{int(hours):02d}:{int(minutes):02d}:{seconds:02d}]")
