# 1. Python Program to Find LCM
def calculate_lcm(a,b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
print("The lcm of",num1,"and",num2,"is: ",calculate_lcm(num1,num2))
