num_of_students = int(input())
student_dict = {}

for student in range(num_of_students):
    name, grade = input().split()
    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(float(grade))

for key, value in student_dict.items():
    print(f"{key} -> {*value, }")
    