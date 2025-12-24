n = int(input("Enter number of students: "))
marks_list = []
i = 0
while i < n:
    mark = int(input("Enter marks of student " + str(i + 1) + ": "))
    marks_list.append(mark)
    i = i + 1

def average(marks_list):
    total = 0
    count = 0
    for mark in marks_list:
        total = total + mark
        count = count + 1
    avg = total / count
    return avg

def highest(marks_list):
    high = marks_list[0]
    for mark in marks_list:
        if mark > high:
            high = mark
    return high

def grades(marks_list):
    grade_list = []
    for mark in marks_list:
        if mark >= 90:
            grade_list.append('A')
        elif mark >= 75:
            grade_list.append('B')
        elif mark >= 60:
            grade_list.append('C')
        else:
            grade_list.append('F')
    return grade_list

print("Average Marks:", average(marks_list))
print("Highest Marks:", highest(marks_list))
print("Grades of all students:", grades(marks_list))
