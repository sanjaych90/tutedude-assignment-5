student_details = {"Rohan": 92.5, "Ravi": 88, "Sanjay": 35, "Roshni": 55}
student_name= input("Enter student name: ").capitalize()
try:
    student_marks = student_details[student_name]
    print(f"The average marks of {student_name} is {student_marks}")
except KeyError:
    print(f"The student named {student_name} could not be found")