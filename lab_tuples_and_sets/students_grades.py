num_of_students = int(input())
student_dict = {}

for student in range(num_of_students):
    name, grade = input().split()
    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(float(grade))

for key, value in student_dict.items():
    formatted_grades = ' '.join([f"{x:.2f}" for x in value])
    average_grade = sum(value) / len(value)
    print(f"{key} -> {formatted_grades} (avg: {average_grade:.2f})")
