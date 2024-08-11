#program to check if the given number is Armstrong or not.
num = int(input("enter a three digit number: "))

temp =  num
digit = 0

while temp > 0:
    rem = temp % 10
    digit = digit + rem ** 3
    temp = temp // 10

if digit == num:
    print("it is armstrong")
else:
    print("not armstrong")
