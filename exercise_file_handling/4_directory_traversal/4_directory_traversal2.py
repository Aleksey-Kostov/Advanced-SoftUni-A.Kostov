import os

files = {}

directory = os.path.abspath(input())


def get_file(folder, level):
    if level < 0:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = element.split('.')[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_file(f, level - 1)


get_file(directory, 1)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f'.{ext}\n')
        for f_name in sorted(f_names):
            output_file.write(f'- - - {f_name}\n')
