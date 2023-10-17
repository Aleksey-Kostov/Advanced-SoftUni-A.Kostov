def forecast(*args):
    sorted_location = sorted(args, key=lambda x: (-(x[1] == "Sunny"), -(x[1] == "Cloudy"), -(x[1] == "Rainy"), x[0]))
    result = ""
    for location, weather in sorted_location:
        result += f"{location} - {weather}\n"
    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
