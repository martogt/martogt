n_pairs = int(input())

students_grades = {}

for _ in range(n_pairs):
    name = input()
    grade = float(input())

    if name not in students_grades:
        students_grades[name] = grade
    else:
        students_grades[name] += grade
        students_grades[name] /= 2

for names, grades in students_grades.items():
    if grades >= 4.50:
        print(f"{names} -> {grades:.2f}")
