from collections import deque

eggs_size = deque(int(x) for x in input().split(", "))
piece_of_paper = [int(x) for x in input().split(", ")]

BOX_SIZE = 50
luck_eggs = 13
create_box = []

while eggs_size and piece_of_paper:
    first_eggs = eggs_size.popleft()
    last_piper = piece_of_paper.pop()
    current_sum = first_eggs + last_piper
    if first_eggs <= 0:
        piece_of_paper.append(last_piper)
        continue
    if first_eggs == luck_eggs:
        piece_of_paper.append(last_piper)
        piece_of_paper[-1], piece_of_paper[0] = piece_of_paper[0], piece_of_paper[-1]
    elif current_sum <= BOX_SIZE:
        create_box.append(current_sum)
    elif current_sum > BOX_SIZE:
        continue

if create_box:
    print(f"Great! You filled {len(create_box)} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join(map(str, eggs_size))}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join(map(str, piece_of_paper))}")
