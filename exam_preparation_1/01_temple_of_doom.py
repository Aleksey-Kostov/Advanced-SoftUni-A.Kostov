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

if not check_result:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools_sequence:
    tools_sequence = [str(x) for x in tools_sequence]
    print(f"Tools: " + ', '.join(tools_sequence))
if substances_sequence:
    substances_sequence = [str(x) for x in substances_sequence]
    print(f"Substances: " + ", ".join(substances_sequence))
if check_result:
    check_result = [str(x) for x in check_result]
    print(f"Challenges: " + ", ".join(check_result))
