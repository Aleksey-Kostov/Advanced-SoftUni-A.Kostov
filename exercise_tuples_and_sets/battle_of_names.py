numbers_n = int(input())

odd_set = set()
even_set = set()

for i in range(1, numbers_n + 1):
    sum_name = sum([ord(x) for x in input()]) // i
    if sum_name % 2 == 0:
        even_set.add(sum_name)
    elif sum_name % 2 != 0:
        odd_set.add(sum_name)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')
