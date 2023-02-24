# #checking whether the given number is positive or negative or 0
# a = float(input("enter the number : "))
# if a>0:
#     print("Positive number")
# elif a<0:
#     print("Negative number")
# else:
#     print("Zero")



# check whether the given number is even or odd
#if the number is divsible by 2 it is even or if the remainder is 1,it is odd
num = int(input("enter the number : "))
if num%2==0 and num>0:
    print("{} is Even numer".format(num))
else:
    print("{} is Odd number".format(num))




# #python program to check whether the given year is leap year or not
# def checkleap(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#         return "{} is leap year.".format(year)
#     else:
#         return "{} is not a leap year.".format(year)
# year = int(input("Enter the year : "))
# print(checkleap(year)) 



# #find the largest number among 3 inputs
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# c = int(input("Enter the third number : "))
# if a>=b and a>=c:
#     large = a
# elif b>=a and b>=c:
#     large  = b
# else :
#     large = c
# print("Largest number : ",large)



# l = [1,2,312,1231,232]
# # print(max(l))
# max = l[0]
# for i in l:
#     if max<i:
#         max = i
# print(max)


# #python program to compute all permutation of the string
# def perm(string, i=0):
#     if i==len(string):
#         print("".join(string))
#     for j in range(i,len(string)):
#         words = [c for c in string]
#         words[i],words[j]=words[j],words[i]
#         perm(words,i+1)
# a = input("Enter the string : ")
# perm(a)