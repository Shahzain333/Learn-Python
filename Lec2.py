#--------------------String and length--------------

# str1 = "This is a String.\nWe are creating it in python"
# print(str1)

# str2 = "This is a String.\tWe are creating it in python"
# print(str2)

# str1 = "Apna"
# str2 = "College"
# str3=(str1+" "+str2)

# print(str3)
# print(len(str3))

#--------------Indexing string---------------

# ch = str1[3] #index which can show the alphabet of str1 jis index mai hoga wah show kry ga

# print(ch)


#---------------Slicing-------------------------


# str = "Apna College"

# #-------for positive index 

# print(str[0:4])
# print(str[5:12])
# print(str[5:len(str)])
# print(str[5:]) #[5:len(str)]
# print(str[:4]) #[0:4]

# #-------for Negative index 

# print(str[-3:-1])
# print(str[-12:-8])
# print(str[-7:-1])

#---------------String Function-------------------------


# str = "i am Studying Python from apna college"

# print(str.endswith("ege"))
# print(str.endswith("app"))

# print(str.capitalize())
# print(str.replace("Python","Java"))
# print(str.replace("o","a"))

# print(str.find("Python"))
# print(str.count("Python"))


#---------------Let's Practice ---------------------------------------

# name = input("Enter Your Name :")
# print("Your Name legth is :",len(name))


# str = input("Enter The String :")
# print("Your String Count is :",str.count("$"))


#------------------------------------------Conditional Statement----------------------------------

# age = input("Enter Your Age :")

# if( age >= "18"):
#   print("You wil be able to give the vote!")
# elif( age <= "18"):
#   print("You will not be able to give the vote!")


# light = "green"

# if( light == "red"):
#     print("Stop")
    
# elif( light == "green"):
#     print("go")

# elif( light == "yellow"):
#     print("Look")


# light = "black"

# if( light == "red"):
#     print("Stop")
    
# elif( light == "green"):
#     print("go")

# elif( light == "yellow"):
#     print("Look")

# else:
#     print("Light is broken")



#-----Conditional Statement for grade---

# marks = int(input("Enter Your MArks :"))

# if( marks >= 90 ):
#     print("Your Grade is : 'A' ")
# elif( marks > 80 and marks < 90 ):
#     print("Your Grade is : 'B' ")
# elif( marks > 70 and marks < 80):
#     print("Your Grade is : 'C' ")
# else:
#     print("Your Grade is : 'D' ")
    
#----Nested conditional Statement-------

# age = 34

# if( age >= 18):
#     if( age >= 80):
#         print("Can't Drive")
#     else:
#         print("Drive")
# else:
#     print("Can't Drive")

# age = 95

# if( age >= 18):
#     if( age >= 80):
#         print("Can't Drive")
#     else:
#         print("Drive")
# else:
#     print("Can't Drive")


#-----------------------------let's Practice--------------------
#-----print even and odd no

# num = int(input("Enter The No :"))

# rem = num % 2

# if( rem == 0):
#     print("Even")
# else:
#     print("Odd")

#-----print the greatest of 3 number enetered by the user

# num1 = int(input("Enter The 1st No :"))
# num2 = int(input("Enter The 2nd No :"))
# num3 = int(input("Enter The 3rd No :"))

# if( num1 >= num2 and num1 >= num3):
#     print("First Num is Largest :",num1)
# elif( num2 >= num3):
#     print("Second Num is Largest :",num2)
# else:
#     print("Third Num is Largest :",num3)


#---------check no is multiple of 7 or not ------

num = int(input("Enter The No :"))

if( num % 7 == 0):
    print("The NO is Multiple of 7")
else:
    print("The No is not multiple of 7")























