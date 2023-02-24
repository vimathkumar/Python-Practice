#simple Intrest
#we know the formula for simple intrest S.I = P * T * R /100
principal_amount = int(input("enter the principal amount : "))
time = int(input("enter the years : "))
rate = int(input("enter the intrest rate per year :"))
simple_intrest = (principal_amount*time*rate)/100
print("SIMPLE INTREST : ",simple_intrest)

#compound intrest
#FORMULA : CI = P *(1+R/100)**T-P
compund_intrest = principal_amount*(1+rate/100)**time-principal_amount
print("COMPOUND INTREST : ",round(compund_intrest,2))