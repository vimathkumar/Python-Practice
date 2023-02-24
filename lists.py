# list1 = [] #empty list method 1
# print(type(list1))

# list2 = list() #method 2
# print(type(list2))

# vimath = [1,3,2.23,"hello",True] #method 1
# print(vimath)

# vim = list([1,34,32424]) #method 2
# print(vim)
# print(len(vim))

#data accesssing
# vimath = [1,2.4,24,63,"vimath",23,242,[2,345,223,678,356],6]
# print(vimath[5])
# print(vimath[2])
# print(vimath[4][3])
# print(vimath[-1])
# print(vimath[-2])
# print(vimath[-2][2])
# # we can access nested list elements by indexing
# # print(vimath[20]) #out of range
# # print(vimath[-19]) #out of range
# vi = [1,2,23,432,543,67,"vik",8,9795]
# vi[1] = "hello list"
# print(vi)

#slicing in lists
#[start : stop : skip]
vimath = [2,34,5.53,2423,3533,"vimath",[234,242,24234,2424]]
print("length of list: ",len(vimath)) #len = 7
print(vimath[0:6]) #from 2 to "vimath"
print(vimath[0:6:3]) #skips 2 elements after each element
print(vimath[0:6:2]) #skips one elements
print(vimath[:]) #whole list
print(vimath[:6]) #0th index to exclude 6th index
print(vimath[2:]) #include 2nd index and remaing right elements
print(vimath[1:6:-2]) #gives empty
print(vimath[6::-2]) #reverse list with skip 1 element
print(vimath[-1:-8:-3]) #skips 2 elements in reverse
print(vimath[::-1]) #whole list reverse



#list methods
# balayya = [1,2,4,5,5,36,32,2,23,4,53,53,5]
#variable.method()
#Append
# balayya.append("balayya") #append takes single argument
# balayya.append(["balayya"])
# print(balayya) 
# print(type(balayya[-1]))
# print(type(balayya[-2]))
# #extend
# balayya.extend(["hi","jai",12,46,25,34])#takes bulk arguments in list format []
# print(balayya)
# #count
# print(balayya.count(5))#prints how many times the input value 5 repeats

#to print index of required input value
# balayya = [1,2,4,5,5,36,32,2,23,4,53,53,5]
# print(balayya.index(5))
# print(len(balayya)) #prints length of list...len() is built - in function
# #clear method
# balayya.clear()
# print(balayya)
# #copy method
# balayya = [1,2,4,5,5,36,32,2,23,4,53,53,5]
# b = balayya.copy()#creats a new list copy
# b.extend([12,34,324,2342,23])
# print(balayya)
# print(b)

#insert  method
# balayya = [1,2,4,5,5,36,32,2,23,4,53,53,5]
# balayya.insert(1,"balu")#take two input arguments, name.insert(index,value)
# print(balayya)
# #pop method
# balayya = [1,2,4,5,5,36,32,2,23,4,53,53,5]
# balayya.pop(1)#takes index value and remove that element,if no argument removes last element
# print(balayya)
# #remove method
# balayya = [1,2,4,5,5,36,32,2,23,4,53,53,5]
# balayya.remove(36)#take value as input ..and remove that value
# print(balayya)
# balayya.reverse()
# print(balayya)

#sort method
# balayya = [214,234,12,2,4512,42,42153,63,4124,26,56,24,14325]
# balayya.sort()
# print(balayya)

# #reverse sort
# balayya = [214,234,12,2,4512,42,42153,63,4124,26,56,24,14325]
# balayya.sort(reverse=True)
# print(balayya)

#list comprehension
# balayya = ["even" if i%2==0 else "odd" for i in range(10)]
# print(balayya)
# #method 1
# fruits = ["apple","banana","papaya","kiwi","pineapple","guava","cherry"]
# new_list = [x for x in fruits if "a" in  x ]
# print(new_list)
# #method 2
# fruits = ["apple","banana","papaya","kiwi","pineapple","guava","cherry"]
# new_list = []
# for x in fruits:
#     if "a" in x:
#         new_list.append(x)
# print(new_list)

#finding occurance of a single value in list
# s = [1,3,2,1,21,32,1,2,3,4,2,1,2,3,4,4,2,2,3,3,4]
# for i in range(len(s)):
#     #print(i)
#     if s[i] == 2:
#         print(i,end=" ")

# s = [1,3,2,1,21,32,1,2,3,4,2,1,2,3,4,4,2,2,3,3,4]
# n = []
# for i in range(len(s)):
#     if s[i]== 2:
#         pass
#     else:
#         n.append(s[i])
# print(s)
# print(n)