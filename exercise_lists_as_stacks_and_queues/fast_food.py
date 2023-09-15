from collections import deque

quantity_of_food = int(input())
order_deq = deque([int(x) for x in input().split()])

print(max(order_deq))


while order_deq and quantity_of_food >= order_deq[0]:
    current_order = order_deq.popleft()
    quantity_of_food -= current_order


if order_deq:
    print(f"Orders left: ", end="")
    while order_deq:
        print(order_deq.popleft(), end="")
        if order_deq:
            print(" ", end="")
else:
    print("Orders complete")
