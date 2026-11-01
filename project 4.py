students = {
    "S101": {"name": "ashish", "marks": [78, 65, 88]},
    "S102": {"name": "gupta", "marks": [35, 72, 61]},
    "S103": {"name": "gupta ji", "marks": [50, 72, 61]},
    "S104": {"name": "none", "marks": [21, 21, 21]},

}

def total(marks):
    return sum(marks)

def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "First Division"
    elif avg >= 40:
        return "Pass"
    else:
        return "Fail"

def report(student):
    marks = student["marks"]
    avg = average(marks)
    print(student["name"], marks, total(marks),round(avg, 2), grade(avg))

def class_average(*marks):
    return sum(marks) / len(marks)

def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print("STUDENT REPORT")

for sid, student in students.items():
    print(sid, end=" | ")
    report(student)

top_students = list(filter(
    lambda s: average(s["marks"]) >= 75,
    students.values()
))

names = list(map(lambda s: s["name"], top_students))
print("High performers:", names)

print("Class average:",
      class_average(77, 56))

print("Recursive sum:", recursive_sum(5))
