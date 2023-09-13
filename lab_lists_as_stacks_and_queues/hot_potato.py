from collections import deque

kids_name = deque(input().split())

n = int(input())
rotate_n = - n + 1

while len(kids_name) > 1:
    kids_name.rotate(rotate_n)
    removed_kid = kids_name.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {kids_name[0]}")
