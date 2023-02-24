# def login_required(f1):
#     def innner(name,is_login):
#         if is_login==False:
#             print("Login required!")
#             return
#         return f1(name,is_login)
#     return innner

# @login_required
# def home(name,is_login):
#     print("Welcome to home page")

# @login_required
# def orders(name,is_login):
#     print("Welcome to orders page")

# def about():
#     print("Welcome to about page")
    
# home('user',True)
# orders('user',False)
# about()

# def ZeroDivisionError(f1):
#     def inner(a,b):
#         if b==0:
#             print("Cannot divide by zero")
#             return
#         return f1(a,b)
#     return inner

# @ZeroDivisionError
# def div(a,b):
#     print(a/b)
    
# div(5,0)

# a= 6
# b = 7
# print(a|b)


# a = 5
# for i in range(1,11):
#     print(a," X ",i," = ",(a*i))


# num = int(input()) 
# while(num>0):
#     for i in range(1,num+1):
#         print(i,end=' ')
#     num-=1 
#     print()



# #sum of elements
# num = int(input())
# array = input()
# l = array.split()
# sum = 0
# for i in l:
#     sum += int(i)
# print(sum)

# #recursion function
# def fun(n):
#     if n==0:
#         return 1
#     else:
#         return (1/(2**n)) + fun(n-1)
# n = int(input())
# s = fun(n)
# print(s)


# 5
# 1 3 5
#9
# 1 3 5 7 9

# #sabitha - the developer
# num = int(input())
# for i in range(1,num+1,2):
#     print(i, end=' ')
    
# #vimath - the junior developer
# sabitha = int(input())
# for i in range(1,sabitha+1):
#     if i%2==1:
#         print(i,end=' ')

    