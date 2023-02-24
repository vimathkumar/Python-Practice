# file = open("demo.txt",mode="r")
# a = file.read()
# print(a)
# file.close()

# file = open("demo.txt",mode="r")
# a = file.readline()
# print(a)
# file.close()

# file = open("demo.txt",mode="r")
# a = file.readlines()
# print(a[1])
# print(a)
# file.close()

# file = open("demo.txt",mode="a")
# a = file.write(" this is my append mode")
# file.close()

# file = open("demo.txt",mode="w")
# a = file.write("this is my write functiom")
# file.close()

# #reading file in 'r+' mode
# with open("demo.txt",'r+') as file:
#     print(file.tell())
#     print(file.read())
#     print(file.tell())



# #reading file in 'w+' mode
# with open("demo.txt",'w+') as file:
#     print(file.tell())
#     print(file.read())
#     print(file.tell())
#     c = file.write("this is w+")
    
# #reading file in 'w+' mode
# with open("demo.txt",'w+') as file:
#     print(file.tell())
#     c = file.write("this is w+ function")
#     print(file.read())
#     print(file.tell())



# #write file in r+ mode 
# with open("demo.txt",'r+') as f:
#     f.write("this r+ ") #replace first words
    
# #write file in w+ mode
# with open("demo.txt",'w+') as w:
#     w.write("this is write")

# #with w+ opening new file
# with open("balayya.txt",'w+') as d:
#     pass

# #with r+ cannot open new file #error
# with open("chiranjeevi.txt",'r+') as d:
#     pass


# #opening file
# fp = open("demo.txt",'r')
# print(fp.tell())
# fp.read(6)
# print(fp.tell())
# fp.seek(3)
# print(fp.tell())
# fp.read()
# print(fp.tell())
# fp.close()



file = open("demo.txt",'r+')
content = file.read()
b = str(content)
print(b)
f = b.split()
print(f)
f.insert(2,"cheetah")
print(file.tell())
file.close()
file = open("demo.txt",'w')
print(f) 
for i in f: 
    file.writelines([i])