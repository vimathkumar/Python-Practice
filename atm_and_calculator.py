# #calculator program with functions
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def sq(a):
#     return a**2
# def cube(a):
#     return a**3

# def inp():
#     a = float(input("enter the first number : "))
#     b = float(input("enter the second number : "))
#     return a,b

# s = """
# ----------------
#    OPERATIONS
# ----------------
# 1.ADDITION
# 2.SUBSTRACTION
# 3.DIVISON
# 4.MULTIPLICATION
# 5.SQUARE
# 6.CUBE
# """
# while True:
#     print(s)
#     op = int(input("Enter your option : "))
#     if op==1:
#         c = inp()
#         print("addition : ", add(c[0],c[1]))
#     elif op==2:
#         c = inp()
#         print("substraction : ",sub(c[0],c[1]))
#     elif op==3:
#         c = inp()
#         print("divison :",div(c[0],c[1]))
#     elif op==4:
#         c = inp()
#         print("multiplication : ",mul(c[0],c[1]))
#     elif op==5:
#         a = int(input("enter you number :"))
#         print("sqare : ",sq(a))
        
#     elif op==6:
#         a = int(input("enter your number : "))
#         print("cube : ",cube(a))
#     else :
#         print("INVALID OPTION")
#     op1 = input("Do you want to do another operation ,yes/no : ")
#     if op1=='yes':
#         pass
#     else:
#         break








































































































#using functions in ATM basics
def credit():
    print("Credit : ")
    credit1 = float(input("enter the credit amount : "))
    print("total amount : ",amount+credit1)

def debit1():
    print("Debit :")
    debit = float(input("enter the amount : "))
    if debit>amount:
        print("####Insufficient balance####")
    else :
        print("Take {} cash".format(debit))
        print("remaining amount : ",amount-debit)

def ministatement():
    print("======MINISTATEMENT======")
    print("Balance :",amount)

#ATM with basics in python
user_names ={"vimath" : 1234, "balayya": 2345,"chiru":4567}
while True:
    user = input("enter the user name : ")
    pin1 = int(input("enter the pin : "))
    amount = 1000 #random
    atm = '''
            1. Credit
            2. Debit
            3. Mini Statement
            4. Exit
            '''
    if user in user_names:
        if pin1==user_names[user]:
            print(atm)
            option = int(input("enter the option : "))
            if option==1:
                credit()
            elif option==2:
                debit1()
            elif option ==3:
                ministatement()
            elif option == 4:
                print("Thank you...")
                break
            else :
                print("Invalid option")
        else:
            print("Enter Valid pin...")
    else :
        print("INVALID USER NAME...")
    print()