n = int(input())
students = {}

for _ in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student_name, students_grades in students.items():
    formated_grades = ' '.join([f"{grades:.2f}" for grades in students_grades])
    print(f"{student_name} -> {formated_grades} (avg: {sum(students_grades) / len(students_grades):.2f})")
