# list of three students named Jon, Kim and Lee
students = ["Jon", "Kim", "Lee"]
students.append("Sara")
students.append("Miko")

# function to print 'Hi name' for each student in the list
def greet_students(student_list):
    for student in student_list:
        print(f"Hi {student}")
    print(f"Total number of students: {len(student_list)}")

# call the function
greet_students(students)

# change Jon to John
students[0] = 'John'
greet_students(students)