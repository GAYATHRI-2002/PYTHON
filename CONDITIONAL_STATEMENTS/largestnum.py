num1 = int(input("enter a number:"))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))

if num1 > num2 and num1 > num3:
    print("number", num1, "is greater than others")
elif num2 > num1 and num2 > num3:
    print("number", num2, "is greater than others")
elif num3 > num1 and num3 > num2:
    print("number", num3, "is greater than others")
else:
    print("error occured")
