#Tuple
# golu = (1234,242,234,535.3453)
# print(type(golu))
# print(golu)
# print(golu[2])
# #buili - in functions not tuple methods
# print(max(golu))
# print(min(golu))
# print(sum(golu))
# print(len(golu))
# print(sorted(golu)) #sorting
# print(list(golu))


# tup = ("hi",)
# print(tup)
# print(type(tup))
# hi = (1,2,3,4,5)
# bye = (23,45,2,35,23)
# print(hi+bye)
# s = zip(hi,bye)
# print(tuple(s))
# new =[]
# for i,j in zip(hi,bye): #adding numbers of two tuples
#     new.append(i+j)
# print(tuple(new))
# d = (1,3,4,2)
# print(d*3)
# print(3 in d) #membership operator
# print(4 not in d)
# print(hi is bye)
# print(hi is not bye)



# balu = (1,34,5,64,56,457,5,43,532,532,23,5,346)  #using for loop
# for i in balu:
#     print(i)




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
                print("Credit : ")
                credit = float(input("enter the credit amount : "))
                print("total amount : ",amount+credit)
            elif option==2:
                print("Debit :")
                debit = float(input("enter the amount : "))
                if debit>amount:
                    print("####Insufficient balance####")
                else :
                    print("Take {} cash".format(debit))
                    print("remaining amount : ",amount-debit)
            elif option ==3:
                print("======MINISTATEMENT======")
                print("Balance :",amount)
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