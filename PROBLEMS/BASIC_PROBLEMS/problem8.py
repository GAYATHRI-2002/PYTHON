# program to print the given number is odd or even.

num1 = int(input("enter a number: "))

if num1 > 0:
    if num1%2 == 0:
        print("the number",num1,"is even")
    else:
        print("the number",num1,"is odd")
else:
    print("invalid")
