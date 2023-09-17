courses = {}

while True:
    line_input = input()
    if line_input == "end":
        break

    course_name, student_name = line_input.split(" : ")

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student_name in courses[course]:
        print(f"-- {student_name}")
