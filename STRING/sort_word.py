#Python Program to Sort Words in Alphabetic Order
str1 = input("enter a string: ")
word = str1.split()
word.sort()
for i in word:
    print(i)
