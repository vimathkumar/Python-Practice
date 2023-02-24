#check whether the given numer is armstrong or not
#without power function
n = int(input("enter the number : "))
l = len(str(n))
s = n
sum1 = 0
while n!=0:
    r = n%10
    sum1+=(r**l)
    n//=10
if sum1==s:
    print("Armstrong")
else :
    print("Not an Armstrong")