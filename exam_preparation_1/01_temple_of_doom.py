from collections import deque

tools_sequence = deque(int(x) for x in input().split())
substances_sequence = [int(x) for x in input().split()]

check_result = [int(x) for x in input().split()]

while substances_sequence and check_result:
    tools_number = tools_sequence.popleft()
    substances_number = substances_sequence.pop()
    current_result = tools_number * substances_number
    if current_result in check_result:
        check_result.remove(current_result)
    else:
        tools_number += 1
        tools_sequence.append(tools_number)
        substances_number -= 1
        if substances_number != 0:
            substances_sequence.append(substances_number)

print(tools_sequence)
print(check_result)

