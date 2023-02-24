##palindrome check
s = input("Enter the string : ")
rev = s[::-1]
if rev ==s:
    print("palindrome")
else:
    print("Not a Palindrome")