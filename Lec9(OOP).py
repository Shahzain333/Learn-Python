#------------------------------------ OOP------------------------------------------

# class student:
#     Name = "Shahzain khan"

# s1 = student()
# # print(s1)
# print(s1.Name)

# s2 = student()
# print(s2.Name)


# class car:
#     Color = "Blue"
#     Brand = "mercedes"

# car1 = car()
# print(car1.Color)
# print(car1.Brand)



# ---------- __init__ Function / Constructor ----------

# class student:
#     name = "Khan"
#     def __init__(self):
#         # print(self)
#         print("Adding New Srudent in Datbase!")
    
# s1 = student()
# # print(s1)
# # print(s1.name)

# class student:
#     def __init__(self,fullname):
#         self.name = fullname
#         print("Adding New Srudent in Datbase!")
    
# s1 = student("Shahzain")
# print(s1.name)

# s2 = student("Khan")
# print(s2.name)

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding New Srudent in Datbase!")
    
# s1 = student("Shahzain",90)
# print(s1.name)
# print(s1.marks)

# s2 = student("Khan",34)
# print(s2.name,s2.marks)


# class student:
    
#     #----------- Default Constructor----
#     def __init__(self):
#         pass
     
#     #--------- Parameterized Constructor ----   
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding New Srudent in Datbase!")
    
# s1 = student("Shahzain",90)
# print(s1.name)
# print(s1.marks)

# s2 = student("Khan",34)
# print(s2.name,s2.marks)


# class student:
    
#     college_name = "ABC College"   
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding New Srudent in Datbase!")
    
# s1 = student("Shahzain",90)
# print(s1.name)
# print(s1.marks)

# # print(s1.college_name)
# print(student.college_name)


# class student:
    
#     college_name = "ABC College"  
#     name = "Anonuymous"   # --- class attr
    
#     def __init__(self,name,marks):
#         self.name = name     # --- Object attr > class attr
#         self.marks = marks
#         print("Adding New Srudent in Datbase!")
    
# s1 = student("Shahzain",90)
# print(s1.name)
# print(s1.marks)

#---------------- methods -------------

# class student:
    
#     def __init__(self,name):
#         self.name = name  
    
#     def welcome(self):
#         print("Welcome Students!")  
    
# s1 = student("Shahzain")
# s1.welcome()

# class student:
    
#     def __init__(self,name):
#         self.name = name  
    
#     def welcome(self):
#         print("Welcome Students!",self.name)  
    
# s1 = student("Shahzain")
# s1.welcome()

# class student:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks  
    
#     def welcome(self):
#         print("Welcome Students!",self.name)  
    
#     def get_marks(self):
#         return self.marks
    
# s1 = student("Shahzain",90)

# s1.welcome()
# print(s1.get_marks())


# ---------------------  Let's Practice ----------------------------------

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum += val
#         print("Hi",self.name,"Your Avg Score is : ", sum/3)

# s1 = student( "Shahzain Khan" , [ 98 , 56 , 90 ] )
# s1.get_avg()


# ----------------------- Static Method ---------------------

# class student:
    
#     @staticmethod
#     def college():
#         print("ABC College")

# c1 = student ()
# c1.college()


# ------------------------------- OOP ( Abstraction ) ------------------

# class cars:
    
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started!.....")
        
# car1 = cars()
# car1.start()

#---------------------------------Let's Practice --------------------

class Account :
    
    def __init__(self , bal , acc_no):
        self.bal = bal
        self.acc_no = acc_no
    
    # debit method
    
    def debit(self , amount):
        self.bal -= amount
        print("Rs." , amount , "was Debited!")
        print("Total Balance = ", self.get_balance())
    
    def credit(self , amount):
        self.bal += amount
        print("Rs." , amount , "was Cedited!")
        print("Total Balance = ", self.get_balance())
    
    def get_balance(self):
        return self.bal
    
        
# acc1 = Account(10000 , 1234)
# print(acc1.bal)
# print(acc1.acc_no)

acc1 = Account(10000 , 1234)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)





































































