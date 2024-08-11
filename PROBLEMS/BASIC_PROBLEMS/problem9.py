#program to find if the given number is prime or not
num = int(input("enter a positive number: "))
for i in range(2,num):
    if num % i == 0:
        print("number",num,"is not a prime")
        break
        
else:
    print("number",num,"is prime")
    
    
