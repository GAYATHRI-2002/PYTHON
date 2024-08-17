#3. Python Program to Make a Simple Calculator
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y
def division(x,y):
    return x / y
def remainder(x,y):
    return x % y

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

print("THE OPTIONS TO CHOOSE")
print("OPTION A     : ADD")
print("OPTION B     : SUBTRACT")
print("OPTION C     : MULTIPLICATION")
print("OPTION D     : DIVISION")
print("OPTION E     : REMAINDER")

option= input("enter an option: ")
if option == 'a' or option == 'A':
    print("The result is : ",addition(num1,num2))
elif option == 'b' or option == 'B':
    print("The result is : ", subtraction(num1, num2))
elif option == 'c' or option == 'C':
    print("The result is : ", multiplication(num1, num2))
elif option == 'D' or option == 'd':
    print("The result is : ", division(num1, num2))
elif option == 'e' or option == 'E':
    print("The result is : ", remainder(num1, num2))
