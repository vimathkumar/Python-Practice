# vimath = 'python'
# balayya = "python's"
# jai = """python is programming language
# strings in python
# hellloo world
# """
# print(type(vimath),type(balayya),type(jai))
# msg1 = "Hello World!"
# msg2 = "Welcome Vimath Kumar"
# print(msg1+msg2) #+ operatoxr
# print(msg1*3)# * operator
# print(msg1[7]) # [] operator
# print(msg2[3:9]) #[:] slicing operator
# str = "Hello"
# if str in msg1: #   in operator
#     print("It is present!")
# if str not in msg2:
#     print("It is not present!")



#string methods
# balayya = "Jai Balayya"
# print(len(balayya))
# #change upper case and lower case methods
# balayya = "Jai Balayya"
# print(balayya.upper()) # prints the whole string in upper case

# print(balayya.lower()) # prints the whole string in lower case

# print(balayya.capitalize()) # prints the first letter in captial case

# print(balayya.title()) # prints the first letter of each word in capital case

# print(balayya.swapcase()) # swaps the case of each letter in string upper to lower or vice versa

# # count , index and find methods in strings
# balu = "my favourite hero hero is balayya balayya babu"
# print(balu.count("balayya"))
# print(balu.index("hero")) #gives the first index of the input value match and if not found returns error
# print(balu.find("hero")) # gives the first index of the input value match
# print(balu.find("hi")) # if not found return -1
# # starts with and endswith methods in strings
# print(balu.startswith("my"))
# print(balu.endswith("babu"))
# print(balu.startswith("ji"))
# #real time example
# websites = ["hi.org","bye.in","balayya.com","babu.in","gk.in","golu.com" ] #database
# in_websites =[]
# for site in websites:
#     if site.endswith("in"):
#         in_websites.append(site)
# print(in_websites)


# # format method in strings
# vimath = "hi {} garu thinnava?".format("balayya")
# print(vimath)
# #real time example 
# #zomato example
# names = ["balu","balayaya","chandrababu","ysjagan","pawan"]
# for name in names:
#     print("hi {} garu thinnara? {}".format(name,"coffe tagara?"))

# #is alphanumeric or alpha or numerica methods in strings
# balayya = "kiran1223"
# print(balayya.isalnum()) #alphabets and numerics accepted
# print(balayya.isalpha()) # only alphabet are acepted return false if any numeric values
# print(balayya.isnumeric()) # only numerics are accepted reutrn false if any alphabet values
# vimath = "23424.32424"
# print(vimath.isalnum())


# #strip methods in strings 
# balayya = " hi balayya garu, oka selfie please...   "
# print(len(balayya))
# a = balayya.strip()
# b =balayya.lstrip()
# c = balayya.rstrip()
# print(len(a)) #strip removes both side spaces
# print(len(b)) # lstrip removes left side whitespaces
# print(len(c)) # rstrip removes right side whitespaces
# #replace method in string
# balayya = " hi balayya garu, oka selfie please please please...   "
# chiranjeevi = balayya.replace("balayya","chiranjeevi")
# print(chiranjeevi)
# chiranjeevi = balayya.replace("hi","hello").replace("balayya","chiranjeevi")
# chiranjeevi = balayya.replace("please","ivvandi",2) # you can give occurance
# print(chiranjeevi)

#split method in strings
# balayya = "jai balayya... oka selfie ayyya"
# l = balayya.split() #split the each word with whitespace in default and makes a list
# print(l)
# print(type(l))
# s = []
# for i in l:
#     if i=="balayya...":
#         i = "chiranjeevi"
#         s.append(i)
#     else :
#         s.append(i)
# print(s)
# #join method in strings
# print(' '.join(s)) #join the items in list with the characteres in quotes''
# print('%'.join(s)) 
# print(' '.join(balayya))

# hi = "di fsa fisf sfsefr fsfs ew sd ses f sfsdf dsfdsd fds"
# print(hi.split('f'))