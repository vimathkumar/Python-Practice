# set = set()
# print(type(set))
# set = {12,2,2,3,32,2}
# print(type(set))
# print(set)
# #print(set[1]) #error
# balayya = {1,54,4,2,1,76,3,21,6,7,3,414,6,72,2,5,67,2,611,435,2,5,2,2,34,5,4}
# print(balayya)
# balayya.add(23)
# print(balayya)
# balu = {1,2,3,5,3,63,75,2,5}
# balu.update({1,2,"python",32,556,34,64,63})
# print(balu)


# balayya = {2,5,4,3,2}
# balayya.remove(4) #delete the element given in remove method
# print(balayya)
# balayya = {2,5,4,3,2}
# balayya.pop() #deletes the random element  #doesnot take any input for pop
# print(balayya)
# balayya = {1,2,3,4,4,3}
# balayya.clear()
# print(balayya)
# vimath = balayya.copy()
# balayya.add(123)
# print(balayya)
# print(vimath)

#set operations
# balayya = {1,2,3,4,5}
# vimath = {4,5,6,7,8}
# print(balayya.union(vimath))
# print(balayya.intersection(vimath))
# print(balayya.difference(vimath))
# print(vimath.difference(balayya))
# print(balayya.symmetric_difference(vimath))
# print(balayya.isdisjoint(vimath))
# print(balayya.issubset(vimath))
# print(balayya.issuperset(vimath))

#Frozen set

# balayya = ["vimath",23,2.3,2342]
# print(type(balayya))

# vimath = frozenset(balayya)
# print(type(vimath))
# print(vimath)
# #print(vimath.append(123)) #returns error
# print(list(vimath))

# Create a frozenset
frozen_set = frozenset({1, 2, 3})

# Try to add an element to the frozenset (this will raise an error)
try:
    frozen_set.add(4)
except AttributeError as e:
    print(e)

# Try to remove an element from the frozenset (this will raise an error)
try:
    frozen_set.remove(2)
except AttributeError as e:
    print(e)

# You can still perform set operations on frozensets
print(frozen_set | {3, 4, 5})  # {1, 2, 3, 4, 5}
print(frozen_set & {3, 4, 5})  # {3}
print(frozen_set - {3, 4, 5})  # {1, 2}
