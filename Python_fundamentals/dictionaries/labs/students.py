line_input = input()

course_info = {}

while ":" in line_input:
    name, student_id, course = line_input.split(":")
    if course not in course_info:
        course_info[course] = {name: student_id}
    else:
        course_info[course][name] = student_id
    line_input = input()

line_input = line_input.replace("_", " ")

students = course_info[line_input]

for name, student_id in students.items():
    print(f'{name} - {student_id}')
