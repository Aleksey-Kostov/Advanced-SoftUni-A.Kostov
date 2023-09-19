number_of_username = int(input())

username_set = set()

for name in range(number_of_username):
    current_name = input()
    username_set.add(current_name)

print(*username_set, sep='\n')
