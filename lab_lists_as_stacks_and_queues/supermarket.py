from collections import deque

name_clients = input()
name_clients_deq = deque()

while name_clients != "End":
    if name_clients == "Paid":
        while name_clients_deq:
            print(name_clients_deq.popleft())
    elif name_clients != "Paid":
        name_clients_deq.append(name_clients)
    name_clients = input()

print(f"{len(name_clients_deq)} people remaining.")
