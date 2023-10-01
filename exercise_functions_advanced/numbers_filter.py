def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "odd":
            kwargs[key] = [x for x in value if x % 2 != 0]
        else:
            kwargs[key] = [x for x in value if x % 2 == 0]
    return dict(sorted(kwargs.items(), key=lambda x: (-len(x), x)))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

