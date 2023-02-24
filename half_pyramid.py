#program to print half pyramid using *
row = int(input("Enter the rows : "))
for i in range(row):
    for j in range(i+1):
        print("*",end=" ")
    print()
