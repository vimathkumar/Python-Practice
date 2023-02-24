#check if a number is prime or not
"""Prime numbers are postive numbers greater than 1 and divsible by 1 and itself."""
def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    return False 
num = int(input("Enter the number : "))
a = is_prime(num)
if a:
    print("Prime")
else:
    print("not prime")