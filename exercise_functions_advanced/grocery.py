def grocery_store(**kwargs):
    sorted_items = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = []
    for k, v in sorted_items.items():
        result.append(f"{k}: {v}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
