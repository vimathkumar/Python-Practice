#Adding two lists using map and lambda functions
l1 = [1,2,3,4]
l2 = [45,3,2,23]
sum = map(lambda a,b:a+b,l1,l2)
print(list(sum))