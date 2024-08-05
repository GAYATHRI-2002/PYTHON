#program to check whether a nunmber is armstrong or not
num = int(input("enter a three digit positive number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10
if temp == sum:
    print("the number",temp , "is armstrong")
else:
    print("thr number", temp , "is not an armstrong number")
