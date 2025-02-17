#A student will not be allowed to sit in exam if his/her attendance is less then 75%
# Take the following inputs from the user: 
# Number of classes attended.
# Number of classes held.
# Print the percentage of classes attended 
# and determined if the student is allowed to take the exam

classes_held = int(input("Enter classes: "))
classes_attended = int(input("Enter attendace: "))
is_allowed = int(classes_attended / classes_held * 100)

if is_allowed >= 75:
    print(f'Classes: {classes_held}, Attendance {is_allowed}%, - allowed to take the exam!')
else:
    print(f'Classes: {classes_held}, Attendance {is_allowed}%, - not allowed to take the exam!')

