count_n = int(input())
unique_element = set()

for _ in range(count_n):
    unique_element.update({x for x in input().split()})

print(*unique_element, sep="\n")
