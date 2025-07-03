"""
Problem: Create a function that calculates the grade based on average score.
Rules:
- Avg ≥ 90 → "A"
- Avg ≥ 75 → "B"
- Avg ≥ 60 → "C"
- Avg < 60 → "F"
Use *args to accept variable number of scores.

def grade_student(name, *scores):
    pass

Expected Outputs:
grade_student("Abhishek", 90, 85, 88)      → "Abhishek got grade B"
grade_student("Riya", 95, 92, 91, 98)      → "Riya got grade A"
grade_student("Tom", 50, 60)               → "Tom got grade F"


"""

def grade_student(name, *scores):
    
    res = sum(scores)/len(scores)
    grade = ""
    if res >= 90:
        grade = "A"
    elif res >= 75:
        grade = "B"
    elif res >= 60:
        grade = "C"
    else:
        grade = "F"


    return f"{name} got grade {grade}"

print(grade_student("Abhishek", 90, 85, 88))
print(grade_student("Riya", 95, 92, 91, 98))
print(grade_student("Tom", 50, 60))