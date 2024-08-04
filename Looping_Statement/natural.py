#Program to find the sum of n natural numbers to a limi
num = int(input("enter the natural number to find the sum to a limit:"))

sum = 0
if num < 0:
    print("enter a natural number")
elif num > 0:
    for i in range(1,num+1):
        sum = sum + i
    print("the sum of n natural numbers to a limit: ",sum)
