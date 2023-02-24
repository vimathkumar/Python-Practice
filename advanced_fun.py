# #lambda function #code reducing #single line anonymous function
# x = lambda a,b,c: (a+b+c)**2
# print(x(1,2,3))

# vim = lambda v,i:v+2+i
# print(vim(1,2))

# l1 = [1,2,3,3,4,43]
# l2 = []
# for i in l1:
#     # m = lambda i:i+1
#     # l2.append(m(i))
#     l2.append(i+1)
# print(l1)
# print(l2)




"""
filter() method filters the given sequence with the help of a function
that tests each element in the sequence to be true or not.
"""
"""
syntax :
filter (function,sequence)
function : function that tests each element whether true or not
sequence : which needs to be filtered,it can be sets,lists,
tuples, or containers of any iterators
"""
# a = [23,24,2,3,56,14,16,43]
# def check(x):
#     if x>18:
#         return True
#     else:
#         return False
# adults = filter(check,a)
# print(adults)
# print(list(adults))

"""
map functon
syntax:
map(function,iterable)
"""

def add(n):
    return n+n
number = [1,4,5,2,2,4,5,2]
mapping = map(add,number)
print(list(mapping))


# def mul(l):
#     return l*3
# l = [1,2,3,4,55]
# print(list(map(mul,l)))

# #reduce function
# from functools import reduce
# list = [1,3,4,4,2342,24,2,234]
# add = reduce(lambda a,b:a+b,list)
# print(add)


# # Generator function
# def simpleGeneratorFun(a,b,c):
#     yield a
#     yield c
#     yield b
# x = simpleGeneratorFun(12,15,13)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

nums = [11,22,33,44,55,66,77,88,99]
filter1 = filter(lambda x:x%2==0,nums)
print(list(filter1))
map1 = map(lambda x:x*2,nums)
print(list(map1))