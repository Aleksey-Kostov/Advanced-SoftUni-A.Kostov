def team_lineup(*args):
    data_dict = {}
    sorted_result = ""
    for name, country in args:
        if country not in data_dict:
            data_dict[country] = []
        data_dict[country].append(name)
    data_dict = dict(sorted(data_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for country, names in data_dict.items():
        sorted_result += f"{country}:\n"
        for name in names:
            sorted_result += f"  -{name}\n"
    return sorted_result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))



