number = int(input())

longest_intersection = set()

for _ in range(number):
    range_one, range_two = input().split("-")
    first_start, first_end = [int(x) for x in range_one.split(",")]
    second_start, second_end = [int(x) for x in range_two.split(",")]

    range_a = set(range(first_start, first_end + 1))
    range_b = set(range(second_start, second_end + 1))

    intersection = range_a.intersection(range_b)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
