
# ---------------------------------- del Keyword ------------------------------

# class student:
#     def __init__(self,name):
#         self.name = name
        
# s1 = student("Shahzain") 
# print(s1.name)
# del s1.name
# print(s1.name)


# ------------------ Pivate (like) Attribute & Method ----------------

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
# acc1 = Account("1234","abcde")
# print(acc1.acc_no)
# print(acc1.__acc_pass)


# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)
        
# acc1 = Account("1234","abcde")
# print(acc1.acc_no)
# # print(acc1.__acc_pass)
# print(acc1.reset_pass())


# class person:
#     __name = "anonymous"
    
#     def __hello(self):
#         print("Hello Person!")
        
#     def welcome(self):
#         self.__hello()
    
# p1 = person()

# # print(p1.__name)
# # print(p1.__hello())
# print(p1.welcome())


# ----------------------------- Inheritance ---------------------------

# ---------Single Inheritance------

# class Car:
    
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car Started!")
    
#     @staticmethod
#     def stop():
#         print("Car Stoped!")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name
        
# Car1 = ToyotaCar("Fortuner")
# Car2 = ToyotaCar("Prius")
        

# print(Car1.name) 
# print(Car1.start()) 
# print(Car1.stop())
# print(Car1.color)


# ---------Multi-level Inheritance------

# class Car:
#     @staticmethod
#     def start():
#         print("Car Started!") 
#     @staticmethod
#     def stop():
#         print("Car Stoped!")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand
        
# class Fortuner(ToyotaCar): 
#     def __init__(self, type):
#         self.type = type


# Car1 = Fortuner("diesel")
# Car1.start()

# --------------- Multiple Inheritance ---------

# class A:
#     varA = "Welcome To Class A"

# class B:
#     varB = "Welcome To Class B"

# class C(A, B):
#     varC = "Welcome To Class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# ---------------------- Super Method -----------------

# class Car:
    
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("Car Started!") 
#     @staticmethod
#     def stop():
#         print("Car Stoped!")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()
        
# Car1 = ToyotaCar("Prius","electric")
# print(Car1.type)


# ------------------- Class Method ------------------

class Person:
    
    name = "Anonymous"
    
    def ChangeName(self,name):
        self.name = name
        
p1 = Person()
p1.ChangeName("Shahzain khan")
print(p1.name)
print(Person.name)

#-- 1st method

# class Person:
    
#     name = "Anonymous"
    
#     def ChangeName(self,name):
#         Person.name = name
        
# p1 = Person()
# p1.ChangeName("Shahzain khan")
# print(p1.name)
# print(Person.name)

#-- 2nd method

# class Person:
    
#     name = "Anonymous"
    
#     def ChangeName(self,name):
#         self.__class__.name = name
        
# p1 = Person()
# p1.ChangeName("Shahzain khan")
# print(p1.name)
# print(Person.name)



# class Person:
    
#     name = "Anonymous"
    
#     @classmethod
#     def ChangeName(cls,name):
#         cls.name = name
        
# p1 = Person()
# p1.ChangeName("Shahzain khan")
# print(p1.name)
# print(Person.name)


#----------------------- Property Method -------------------------


# class Student:
    
#     def __init__(self,phy,math,chm):
#         self.phy = phy
#         self.chm = chm
#         self.math = math
#         # percentage
#         self.percentage = str( (self.phy + self.chm + self.math) / 3 ) + "%"
        
#     def CalculatePercentage(self):
#         self.percentage = str( (self.phy + self.chm + self.math) / 3 ) + "%"
    
# std1 = Student(98,99,97)
# print(std1.percentage)      

# std1.phy = 86
# print(std1.phy)
# print(std1.percentage) 

# class Student:
    
#     def __init__(self,phy,math,chm):
#         self.phy = phy
#         self.chm = chm
#         self.math = math
        
#     # def CalculatePercentage(self):
#     #     self.percentage = str( (self.phy + self.chm + self.math) / 3 ) + "%"
    
#     @property
    
#     def Percentage(self):
#         return str( (self.phy + self.chm + self.math) / 3 ) + "%"
    
# std1 = Student(98,99,97)
# print(std1.Percentage)      

# std1.phy = 86
# print(std1.phy)
# print(std1.Percentage) 


# -------------------------------------- Polymorphism ------------------------------------------

#---This is the implicit overloading (its mean already def in python class )
# print ( 1 + 2 ) # 3
# print( "shah" + "zain" ) # concatenate
# print( [1,2,3] + [4,5,6] ) # merge


# class complex:
    
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img 
        
#     def showNum(self):
#         print( self.real, "i +" , self.img, "j" )
        
#     def add(self , num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return complex(newReal , newImg)

# num1 = complex(1,3)
# num1.showNum()

# num2 = complex(4,6)
# num2.showNum()

# num3 = num1.add(num2)
# num3.showNum()


# class complex:
    
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img 
        
#     def showNum(self):
#         print( self.real, "i +" , self.img, "j" )
    
#     # For add dunder funcion  
#     def __add__(self , num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return complex(newReal , newImg)
#     # For sub dunder funcion
#     def __sub__(self , num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return complex(newReal , newImg)

# num1 = complex(1,3)
# num1.showNum()

# num2 = complex(4,6)
# num2.showNum()

# num3 = num1 + num2
# num3.showNum()

# num3 = num1 - num2
# num3.showNum()


# -------------------------- Let's Practice -----------------------------------------

# qs # 1

# class Circle:
    
#     def __init__(self,radius):
#         self.radius = radius
        
#     # def area(self):
#     #     return 3.14 * self.radius ** 2 
    
#     # def perimeter(self):
#     #     return 2 * 3.14 * self.radius
    
#     def area(self):
#         return (22/7) * self.radius ** 2 
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)

# print(c1.area())
# print(c1.perimeter())

# qs # 2

# class Employee:
    
#     def __init__(self , role , dept , salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary        
    
#     def show_detail(self):
#         print("Role =",self.role)
#         print("Dept =",self.dept)
#         print("Salary =",self.salary)

# class Engineer(Employee):
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer" , "IT" , 50000)
        
    
# # e1 = Employee("Accountant" , "Finance" , 60000)
# # e1.show_detail()

# eng1 = Engineer("Shahzain", 23)
# eng1.show_detail()


# qs # 3

class Order:
    def __init__(self , item , price):
        self.item = item
        self.price = price
    
    def __gt__(self , odr2):
        return self.price > odr2.price
        
        

odr1 = Order("Chips" , 50)
odr2 = Order("ketchup" , 40)

print(odr1 > odr2)





































































