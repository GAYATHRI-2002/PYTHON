#Python Program to Find Armstrong Number in an Interval
start = int(input("enter a number: "))
end = int(input("enter a number: "))
print("the armstrong numbers are:")

for number in range(start,end+1):
    sum = 0
    temp = number
    while temp>1:
        rem = temp%10
        sum = sum + rem ** 3
        temp = temp//10

        if sum == number:
            print(number)
        



        
