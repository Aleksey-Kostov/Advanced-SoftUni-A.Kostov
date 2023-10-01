def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for key, value in sorted_dict:
        result += f"{key}\n"
        sorted_values = sorted(value, reverse=True)
        result += "\n".join([str(x) for x in sorted_values])
        result += "\n"
    return result



