#how to remove punctuation in string
str = input("Enter the string : ")
st = "''!@#$$%^&*()_+:;-{=<>.]}[?,"
result = ''
for i in str:
    if i not in st:
        result = result+i
print('result : ', result)