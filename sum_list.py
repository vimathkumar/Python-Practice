#writing a function for sum of list items
# l = [1,2,3,4,5,23]
# s = 0
# for i in l:
#     s = s+i
# print(s)

def sum_list(num):
    total = 0
    for i in num:
        total+=i
    return total
num = [1,2,3,4,2,4,2,42,3,2,3]
print(sum_list(num))