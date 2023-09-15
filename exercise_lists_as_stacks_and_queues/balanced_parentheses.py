from collections import deque

parentheses_deque = deque([x for x in input()])
range_parentheses = len(parentheses_deque) // 2
parentheses = ["()", "[]", "{}"]

for i in range(len(parentheses_deque)):
    a = parentheses_deque[i]
    b = parentheses_deque[i + 1]
    if parentheses_deque[i] + parentheses_deque[i + 1] not in parentheses:
        parentheses_deque.rotate(-1)
    else:
        parentheses_deque.popleft()
        parentheses_deque.popleft()
        parentheses_deque.rotate(1)

if parentheses_deque:
    print("YES")
else:
    print("NO")
