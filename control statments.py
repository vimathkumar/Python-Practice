#conditional statements
# if 'a'>'b':
#     print("this is if")
# elif 34<23:
#     print("this is elif")
# else:
#     print("this is else")


#if within if is called nested if...
# if 3>2:
#     print("this is outer if")
#     if 2>0:
#         print("this is inner if")
#     else:
#         print("this is innner else")
# else:
#     print("this is outer else")

#short hand ifx

# if 3>2:print("this is if")

#short hand if - else

# a = 1
# b = 2

# print("this is if") if a>b else print("this is else")

""" 
while condition:
    statements
"""

# while False:
#     print("this is loop")
# else:
#     print("else")

# i= 20
# while i<=40:
#     print("this is while",i)
#     i+=1
    
"""
for i in iterators:
    statements

"""

# for i in "kiran":
#     print(i,end=" ")

# for j in range(2,22,2):
#     print(j)

# for i in "hello world":
#     if i== " ":
#         continue
#     print(i,end="")

# for i in "hello world":
#     if i== " ":
#         break
#     print(i,end="")


# if True :
#     pass

#printing 100 tables
for i in range(1,101):
    for j in range(1,11):
        print(i," * ",j," = ",i*j)
        print()
    print()

#user validation program

user = "vimath"
password = "vimath@python"
user_name = input("enter the user name : ")
pass_word = input("enter the password : ")
if user==user_name and password == pass_word :
    print("validation succuess")   
else:
    print("Try agian")