#1. Write a Python program to append a new item to the end of the array.

arr1 = []
arr2 = int(input("enter the number of items in array: "))
for i in range(arr2):
    item = int(input("enter the items: "))
    arr1.append(item)
print(arr1)

arr3 = int(input("enter the item to be entered to the last of array:"))
arr1.append(arr3)
print(arr1)
