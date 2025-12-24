attendance = [(101, ['P', 'A', 'P', 'P', 'P']),
              (102, ['A', 'A', 'P', 'P', 'A']),
              (103, ['P', 'P', 'P', 'A', 'P'])
]

def attendance_percentage(data):
    percentages = []
    for record in data:
        id = record[0]
        attendance = record[1]
        total = 0
        present = 0
        for day in attendance:
            total = total + 1
            if day == 'P':
                present += 1

        percentage = (present * 100) / total
        percentages.append((id, percentage))
    return percentages

def low_attendance_students(data, minAttendence):
    low = []
    percentages = attendance_percentage(data)
    for record in percentages:
        if record[1] < minAttendence:
            low.append(record[0])
    return low

def daily_absences(data):
    absences = []
    days = 0
    while days < 5:
        count = 0
        for record in data:
            if record[1][days] == 'A':
                count = count + 1
        absences.append(count)
        days = days + 1
    return absences

percentages = attendance_percentage(attendance)
print("Student Attendance Percentages:")
for record in percentages:
    print("Student ID:", record[0], "Percentage:", record[1], "%")

minAttendence = 75
low_list = low_attendance_students(attendance,minAttendence)
print("Students below", minAttendence, "% attendan ce:", low_list)

absences_per_day = daily_absences(attendance)
print("Total absences per day:", absences_per_day)
