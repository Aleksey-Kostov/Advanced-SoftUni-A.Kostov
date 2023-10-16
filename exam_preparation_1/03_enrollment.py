def gather_credits(credit, *args):
    total_credit = 0
    courses_info = []
    for current_course, current_credit in args:
        if current_course in courses_info:
            continue
        if total_credit >= credit:
            break
        courses_info.append(current_course)
        total_credit += current_credit
    if total_credit >= credit:
        return (f"Enrollment finished! Maximum credits: {total_credit}.\n"
                f"Courses: {', '.join(sorted(courses_info))}")
    return f"You need to enroll in more courses! You have to gather {credit - total_credit} credits more."

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
