#4. Python Program to Find Factorial of Number Using Recursion

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

num1 = int(input("enter a number: "))
print("the result is : ",factorial(num1))

