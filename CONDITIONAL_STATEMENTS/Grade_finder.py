english = float(input("enter the marks of english:"))
physics = float(input("enter the marks of physics:"))
maths = float(input("enter the marks of maths:"))
science = float(input("enter the marks of science:"))
social = float(input("enter the marks of social:"))

total_marks = english+physics+maths+science+social

average = (total_marks / 500) * 100

if average >= 90:
    print("A grade")
elif average <= 89 and average >= 80:
    print("B grade")
elif average <= 79 and average >= 70:
    print("C grade")
elif average <= 69 and average >= 60:
    print("D grade")
elif average <= 59 and average >= 50:
    print("pass grade")
else:
    print("Failed")
