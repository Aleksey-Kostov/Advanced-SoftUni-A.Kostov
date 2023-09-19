number_of_username = int(input())

username_set = set()

for _ in range(number_of_username):
    username_set.add(input())

print(*username_set, sep='\n')
