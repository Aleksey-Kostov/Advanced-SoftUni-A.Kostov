from collections import deque

type_of_robots = input().split(";")
robots_deq = deque()
product_list = []
all_robots_deque = deque()

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
        all_robots_deque.append([robot_name, robot_time])

for detail in product_list:
    current_robot = all_robots_deque.popleft()[0]
    current_seconds = f"{(int(seconds) + 1):.0f}"
    print(f"{current_robot} - {detail} {hours}:{minutes}:{current_seconds}")
