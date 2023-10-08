def get_integer_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("The variable number must be an integer")


def search_key(numbers_dictionary):
    search_key = input("Enter a key to search for: ")
    if search_key in numbers_dictionary:
        print(numbers_dictionary[search_key])
    else:
        print("Number does not exist in dictionary")


def remove_key(numbers_dictionary):
    remove_key = input("Enter a key to remove: ")
    if remove_key in numbers_dictionary:
        del numbers_dictionary[remove_key]
    else:
        print("Number does not exist in dictionary")


def main():
    numbers_dictionary = {}
    while True:
        line = input("Enter a key or command: ")

        if line == "Search":
            search_key(numbers_dictionary)

        elif line == "Remove":
            remove_key(numbers_dictionary)

        elif line == "End":
            break  # Exit the loop

        else:
            try:
                number = get_integer_input("Enter an integer value: ")
                numbers_dictionary[line] = number
            except ValueError:
                continue  # Skip adding the value if it's not an integer

    print(f"Key-Value pairs in the dictionary: {numbers_dictionary}")

main()
