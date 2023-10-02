def concatenate(*args, **kwargs):
    strings = ""
    for word in args:
        strings += word
    for key, value in kwargs.items():
        if key in strings:
            strings = strings.replace(key, value)
    return strings


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))