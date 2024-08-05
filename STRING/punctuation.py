#Python Program to Remove Punctuation from a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1 = input("enter a string: ")
no_punctuation = ""
for i in str1:
    if i not in punctuations:
        no_punctuation += i
print(no_punctuation)
