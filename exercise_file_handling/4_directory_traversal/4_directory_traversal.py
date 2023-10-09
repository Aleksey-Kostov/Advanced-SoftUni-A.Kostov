import os

file = {}

directory = input()

for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = element.split('.')[-1]
        if ext not in file:
            file[ext] = []
        file[ext].append(element)
    else:
        for el in os.path.join(f):
            filename = os.path.join(f)
            if os.path.isfile(filename):
                ext = element.split('')[-1]
                if ext not in file:
                    file[ext] = []
                file[ext].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(file.items()):
        output_file.write(f'.{ext}\n')
        for f_name in sorted(f_names):
            output_file.write(f'- - - {f_name}\n')
