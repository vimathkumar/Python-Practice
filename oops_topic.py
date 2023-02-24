# OOPs concept

# class balayya:
#     def fun(self):
#         print("this is balayya class")
# vimath = balayya()
# vimath.fun()

# # class vimath():
# #     a = 10 #attribute
# #     def show(self):   #method
# #         print("this is vimath class")
# # vim = vimath()
# # print(vim.a)
# # vim.show()


# class vimath():
#     a = 10 #attribute
#     def show(self):   #method
#         print("this is class")
# vim = vimath()
# vim1 = vimath()
# print(vim1.a)
# vim1.show()

# class vimath():
#     a = 10 #attribute
#     def show(self):   #method(self)
#         print(self.a)
# vim = vimath()
# vim.show()



# class balayya():
#     a = "hi"
#     def fun(self):
#         print(self.a)
# chiru = balayya()   #1 object
# pawan = balayya() #2 objects
# chiru.fun()
# pawan.fun()


# class govinda():
#     def __init__(self,a,b,c): #acts as method and constructor
#         self.one = a
#         self.two = c
#         self.three = b
#         print(a+b)
#     def output(self):
#         print(self.one,self.two,self.three)
# vimath  = govinda(23,45,32)
# vimath.output()



# class mobile():
#     def __init__(self,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         self.name = mobile_name
#         self.ram = mobile_ram
#         self.battery = mobile_battery
#         self.price = mobile_price
#     def data(self):
#         print("MOBILE NAME : ",self.name)
#         print("MOBILE RAM : ",self.ram)
#         print("MOBILE BATTERY : ",self.battery)
#         print("MOBILE PRICE : ",self.price)
# mob = mobile("iqoo","6","5000mah","15000")
# mob.data()




# class mobile():
#     def __init__(self,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         self.name = mobile_name
#         self.ram = mobile_ram
#         self.battery = mobile_battery
#         self.price = mobile_price
#     def data(self):
#         print("\nMOBILE NAME : ",self.name)
#         print("MOBILE RAM : ",self.ram)
#         print("MOBILE BATTERY : ",self.battery)
#         print("MOBILE PRICE : ",self.price)
# a = input("Enter the mobile name : ")
# b = input("Enter the mobile ram : ")
# c = input("Enter the mobile battery : ")
# d = float(input("Enter the mobile price : "))
# mob = mobile(a,b,c,d)
# mob.data()




# class Bike():
#     def __init__(self,bike_model,milage,capacity,price):
#         self.model = bike_model
#         self.speed = milage
#         self.capacity = capacity
#         self.price = price
#         print("\nBike details : ")
#     def Bike_Data(self):
#         print("Bike model : ",self.model)
#         print("Bike milage : ",self.speed)
#         print("Bike fuel capacity : ",self.capacity)
#         print("Bike price : ",self.price)
# model = input("Enter the Bike and model : ")
# speed = input("Enter the milage of bike : ")
# capacity = input("Enter the fuel capacity of the bike : ")
# price = float(input("Enter the total cost of bike : "))
# bike1 = Bike(model,speed,capacity,price)
# bike1.Bike_Data()














# day 2




# #Single Inheritance
# class parent():
#     def output(self):
#         print("this is parent class")
# class child(parent):
#     def input(self):
#         print("THIS IS CHILD CLASS")
# balayya = child()
# balayya.output()
# balayya.input()



#  #mutiple inheritance
# class Father():
#     def outputF(self):
#         print("this is father class")
# class Mother():
#     def outputM(self):
#         print("this is Mother class")
# class son(Father,Mother):
#     def outputS(self):
#         print("this is Child class")
# child = son()
# child.outputF()
# child.outputM()
# child.outputS()



# #multiLevel inheritance
# class GrandFather():
#     def outputGF(self):
#         print("this is grand father class")
# class Father(GrandFather):
#     def outputF(self):
#         print("this is father class")
# class son(Father):
#     def outputS(self):
#         print("this is child class")
# child = son()
# child.outputGF()
# child.outputF()
# child.outputS()


# #Hierarchial Inheritance
# class Parent():
#     def outputP(self):
#         print("this is parent class")
# class child1(Parent):
#     def outputS1(self):
#         print("this is child 1 class")
# class child2(Parent):
#     def outputS2(self):
#         print("this is child 2 class")
# balayya = child1() #child 1 class
# balayya.outputP()
# balayya.outputS1()
# chiranjeevi = child2() #child 2 class
# chiranjeevi.outputP()
# chiranjeevi.outputS2()


# #poly morphism
# #method overloading
# class methodoverload():
#     def something(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj = methodoverload()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)
# obj.something()




# #Polymorphism
# #method overriding
# class Parent:
#     def display(self):
#         print("this is parent class")
# class Child(Parent):
#     def display(self):
#         super().display()
#         print("this is child class")
# balu = Child()
# balu.display()



# encapsulation
# binding of class (methods and variables(attributes))
# public
# private __
# # protected _

# #protected 
# class GrandF():
#     def __init__(self,a):
#         self._y = a
#         print(self._y)
# class Father(GrandF):
#     def outputF(self):
#         print(self._y)
# class Son(Father):
#     def outputS(self):
#         print("child class ",self._y)
# son = Son(12)
# son.outputS()
# son.outputF()


# #private
# class GrandF():
#     def __init__(self,a):
#         self.__y = a
#         print(self.__y)
# class Father(GrandF):
#     def outputF(self):
#         print(self.__y)
# class Son(Father):
#     def outputS(self):
#         print("child class ",self.__y)
# son = Son(12)
# son.outputS()
# son.outputF()


# a = 10 #global variable
# def fun():
#     b = 20 #local variable
#     print("hi",a,b)
# fun()
# #print(b) #error



# from abc import ABC, abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass
# class Tesla(Car):
#     def mileage(self):
#         print("the mileage is 30kmph")
# class Suzuki(Car):
#     def mileage(self):
#         print("the mileage is 20kmph")
# class Tata(Car):
#     def mileage(self):
#         print("the mileage is 50kmph")
# t = Tesla()
# t.mileage()
# s = Suzuki()
# s.mileage()
# tata = Tata()
# tata.mileage()









##practice
# def prime(num):
#     c = 0
#     for i in range(1,num):
#         if num>1 and num%i==0:
#             c+=1
#     return c
# number = int(input("Enter the number : "))
# c = prime(number)
# if c==1:
#     print("{} is prime.".format(number))
# else:
#     print("{} is not prime".format(number))


# #practice
# str = input("enter the string : ")
# print("Palindrome") if str==str[::-1] else print("Not a Palindrome")