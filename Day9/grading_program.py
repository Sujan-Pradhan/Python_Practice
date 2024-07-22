student_scores = {
    "Sujan": 99,
    "Harry": 82,
    "John":78,
    "Draco":74,
    "Nevile":62
}

 
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score>90 and score<=100:
        student_grades[student] = "Outstanding"
    elif score>80:
        student_grades[student] = "Exceeds Expectation"
    elif score >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)