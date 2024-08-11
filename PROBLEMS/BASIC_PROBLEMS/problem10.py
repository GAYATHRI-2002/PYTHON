# program to check if the given number is palindrome or not.
num = int(input("enter a number: "))

temp = num
rev = 0

while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10

if rev == num:
    print("the number is palindrome")
else:
    print("not a palindrome")
