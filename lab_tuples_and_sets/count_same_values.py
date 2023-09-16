numbers = tuple(float(num) for num in input().split())
# num_list = []
#
# for num in numbers:
#     if num not in num_list:
#         num_list.append(num)
#         current_num = numbers.count(num)
#         print(f"{num} - {current_num} times")

num_list = {}
for num in numbers:
    if num not in num_list:
        num_list[num] = numbers.count(num)

for key, value in num_list.items():
    print(f"{key} - {value} times")
