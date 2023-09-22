from collections import deque

string = deque(input().split())

main_color = ["red", "yellow", "blue"]
secondary_color = {"orange": ["red", "yellow"],
                   "purple": ["red", "blue"],
                   "green": ["yellow", "blue"]}
collections_color = []

while string:
    first_string = string.popleft()
    last_string = string.pop() if string else ""
    if first_string + last_string in main_color or first_string + last_string in secondary_color:
        collections_color.append(first_string + last_string)
    elif last_string + first_string in main_color or last_string + first_string in secondary_color:
        collections_color.append(last_string + first_string)
    else:
        if len(first_string) > 1:
            string.insert(len(string) // 2, first_string[:-1])
        if len(last_string) > 1:
            string.insert(len(string) // 2, last_string[:-1])

for color in collections_color:
    if color in secondary_color:
        for el in secondary_color[color]:
            if el not in collections_color:
                collections_color.remove(color)
                break

print(collections_color)
