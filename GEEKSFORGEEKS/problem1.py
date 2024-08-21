#1.Python program to interchange first and last elements in a list
def interchange(x):
    y = len(x)
    temp = x[0]
    x[0] = x[y - 1]
    x[y-1] = temp
    return x
x = [1,2,3]
print(interchange(x))
