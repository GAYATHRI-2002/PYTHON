#Python Program to Generate a Random Number

import random

n = random.randint(3,6)
print("Random number between a range using randint(): ",n)

#Creating a list of random integers using for loop
rand_list = []
for i in range(0,10):
    k = random.randint(2,22)
    rand_list.append(k)
print("using for loop: ",rand_list)
