grades = {"Ali": 85, "Sara": 92, "Omar": 78, "Huda": 90}

total = 0
best_name = None
best_grade = -1

for name, grade in grades.items():
    print(f"{name}: {grade}")
    total += grade
    if grade > best_grade:
        best_grade = grade
        best_name = name

average = total / len(grades)
print(f"Average: {average:.2f}")
print(f"Best: {best_name} ({best_grade})")
