#--------------------------- Open & read file --------------------------

# f = open("demo.txt", "r")

# data = f.read()

# print(data)
# print(type(data))

# f.close()


# f = open("demo.txt", "r")

# data = f.read(8)  # no of character specify 

# print(data)
# print(type(data))

# f.close()


# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


# f = open("demo.txt", "r")

# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


#--------------------------- Open & Write file --------------------------

# f = open("demo.txt","w")  # write

# f.write("This is a First newline!")

# f.close()


# f = open("demo.txt","a")   # append

# f.write("\nThis is a Second newline!")

# f.close()

# f = open("Sample.txt","w")
# f.close()

#----- Using r+

# f = open("demo.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

#----- Using w+

# f = open("demo.txt","w+")

# print(f.read())
# f.write("abc")

# f.close()

#----- Using a+

# f = open("demo.txt","a+")

# print(f.read())
# f.write("abc")

# f.close()


#----------------- With Syntax------------------------


# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("New Data!")
   

#------------------------- Deleting a File------------------------------

# import os

# os.remove("demo.txt")



#------------------------------------Let's Practice-----------------------

# f = open("Practice.txt","w")
# f.close()

#   qs # 1

# with open("Practice.txt","w") as f:
#     f.write("Hi Everyone")
#     f.write("\nWe are Learning File I/O")
#     f.write("\nUsing Java")
#     f.write("\nI Like Programming in Java")


#   qs # 2

with open("Practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)


# with open("Practice.txt","w") as f:
#     f.write(new_data)


# qs # 3 

# with open("Practice.txt","r") as f:
#     data = f.read()
    
#     word = "Learning"
    
#     if( data.find(word) != -1 ):
#         print("Found")
#     else:
#         print("Not Found")

# for function

# def check_for_word():
#     with open("Practice.txt","r") as f:
#        data = f.read()
    
#        word = "Learning"
    
#        if( data.find(word) != -1 ):
#           print("Found")
#        else:
#           print("Not Found")
            
# check_for_word()


# qs # 4 

# def check_for_line():
    
#     word = "Learning"
#     data = True
#     line_no = 1
    
#     with open("Practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if( word in data ):
#                 print(line_no)
#                 return
            
#             line_no += 1
    
#     return -1
            
# print(check_for_line())   
        
        
# qs # 5


with open("Practice.txt","w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10,11,12")  
    
with open("Practice.txt","r") as f:
    
    data = f.read()
    # print(data) 
# ---- 1st Method  
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ',' ):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

#----- 2nd Method
    count = 0
    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)
        
            
       

















