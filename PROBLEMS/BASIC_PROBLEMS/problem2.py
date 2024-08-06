#program to do arithmetical operations

#using simple program
#Addition
num1 = input("enter a number: ")
num2 = input("enter a number: ")

sum = int(num1) + int(num2)
sub = int(num1) - int(num2)
mul = int(num1) * int(num2)
div = int(num1) / int(num2)



print("the sum of {} and {} is {}".format(num1,num2,sum))
print("the subtraction of {} and {} is {}".format(num1,num2,sub))
print("the multiplication of {} and {} is {}".format(num1,num2,mul))
print("the division of {} and {} is {}".format(num1,num2,div))
