text = tuple(input())

text_set = sorted(set(text))

for char in text_set:
    print(f"{char}: {text.count(char)} time/s")
