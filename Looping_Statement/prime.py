#Program to check the given number is prime/not
num = int(input("enter a number: "))
for i in range(2,num):
    if num % i == 0:
        print("the number is not prime")
        break
    else:
        print("the number is prime")
        break
