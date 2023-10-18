from collections import deque


def check_word(first_char, last_char, current_flowers):
    for i in range(len(current_flowers)):
        if first_char in current_flowers[i]:
            current_flowers[i] = current_flowers[i].replace(first_char, "")
        if last_char in current_flowers[i]:
            current_flowers[i] = current_flowers[i].replace(last_char, "")


vowels = deque(input().split())
consonants = input().split()

found = False

flowers = ["rose", "tulip", "lotus", "daffodil"]

while vowels and consonants:
    first_vowels = vowels.popleft()
    last_consonants = consonants.pop()
    check_word(first_vowels, last_consonants, flowers)
    for index in range(len(flowers)):
        if flowers[index] == "":
            found = True
        if found:
            if index == 0:
                print("Word found: rose")
                break
            elif index == 1:
                print("Word found: tulip")
                break
            elif index == 2:
                print("Word found: lotus")
                break
            elif index == 3:
                print("Word found: daffodil")
                break
    if found:
        break

if not found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
