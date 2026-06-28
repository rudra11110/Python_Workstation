#list 
marks_of_student = []

while True:
    marks = input("Enter the marks (to stop, enter 'finish'): ")

    if marks.lower() == "finish":
        break

    marks_of_student.append(marks)

marks_of_student.sort()

print(marks_of_student)
