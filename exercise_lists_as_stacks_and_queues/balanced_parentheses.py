from collections import deque

parentheses_deque = deque(input())
opening_parentheses = "([{"
closing_parentheses = ")]}"
counter = 0

while parentheses_deque and counter < len(parentheses_deque):
    if parentheses_deque[0] not in opening_parentheses:
        break
    index = opening_parentheses.index(parentheses_deque[0])
    if parentheses_deque[1] == closing_parentheses[index]:
        parentheses_deque.popleft()
        parentheses_deque.popleft()
        parentheses_deque.rotate(counter)
        counter = 0
    else:
        parentheses_deque.rotate(-1)
        counter += 1

if parentheses_deque:
    print("NO")
else:
    print("YES")
