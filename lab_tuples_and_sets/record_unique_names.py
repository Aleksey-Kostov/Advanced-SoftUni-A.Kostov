number_of_names = int(input())
names_set = set()

for name in range(number_of_names):
    current_name = input()
    names_set.add(current_name)

for set_name in names_set:
    print(set_name)
