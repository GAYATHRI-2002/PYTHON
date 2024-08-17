#2.Python Program to Find HCF
def hcf_calculate(x,y):
    if x < y:
        smallest = x
    else:
        smallest = y

    for i in range(1,smallest+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
print("The hcf of",num1,"and",num2,"is: ",hcf_calculate(num1,num2))
