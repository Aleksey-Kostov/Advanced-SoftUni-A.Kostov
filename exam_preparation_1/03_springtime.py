def start_spring(**kwargs):
    item_dict = {}
    for v, k in kwargs.items():
        if k not in item_dict:
            item_dict[k] = []
        item_dict[k].append(v)
    result = ""
    item_dict = sorted(item_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for k, v in item_dict:
        result += f"{k}:\n"
        for i in sorted(v):
            result += f"-{i}\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


