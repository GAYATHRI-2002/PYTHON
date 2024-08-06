#program to solve quadratic equation
#ax^2 + bx + c = 0
import cmath
a = int(input("enter the value 'a' : "))
b = int(input("enter the value 'b' : "))
c = int(input("enter the value 'c' : "))

d = (b**2)-(4*a*c)

solution = (-b) + cmath.sqrt(d)
solution1 = (-b) - cmath.sqrt(d)

print("the solutions are: ",solution)
print("the solutions are: ",solution1)

