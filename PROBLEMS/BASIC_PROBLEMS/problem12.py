#Python Program to Print all Prime Numbers in an Interval
start = int(input("enter a number: "))
end = int(input("enter a number: "))
print("the prime numbers are:")

for number in range(start,end+1):
    if number>1:
        for i in range(2,number):
            if number%i == 0:
                #print("not prime")
                break
        else:
            print(number)
