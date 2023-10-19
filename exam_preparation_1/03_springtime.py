def start_spring(**kwargs):
    result = ""
    object_items = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for k, v in object_items:
        result = f"{k}:\n-{sorted(v)}\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
