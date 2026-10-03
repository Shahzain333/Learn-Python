#------------------------------------------Loop---------------------------------------

#-------While Condition--

# count = 1
# while count <= 5 :
#     print("Hello")
#     count += 1

# print(count)

# i = 1
# while i <= 30 :
#     print("Hello",i)
#     i += 1

# print number from 1 to 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# print("Loop Ended")

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# print("Loop Ended")

#------------------Let's Practice----------
#qs # 1

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# print("Loop Ended")

#qs # 2

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# print("Loop Ended")

#qs # 3

# a = int(input("Enter The Number :"))
# i = 1
# while i <= 10 : 
#     print(a, "*", i, "=",a * i)
#     i += 1

#qs # 4

# nums = [1,4,9,16,25,36,79,64,81,100]
# i = 0
# while i <= (len(nums)-1):
#     print(nums[i])
#     i += 1

# nums = [1,4,9,16,25,36,79,64,81,100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1

#qs # 4

# x = int(input("Enter The Number B/W Tuples :"))

# nums = (1,4,9,16,25,36,49,64,81,100)

# i = 0
# while i < len(nums):
    
#     if(nums[i] == x):
#         print("Found at idx",i)
#         break
#     else:
#         print("Finding...")
        
#     i += 1


#-------------------Break $ continue------

# i = 1
# while i <= 5:
#     print(i)  
#     if(i == 3):
#         break
#     i += 1
#     print("end of loop")


# i = 0
# while i <= 5:
#     if( i == 3):
#         i += 1
#         continue    # skip
#     print(i)
#     i += 1

# i = 0
# while i <= 10:
#     if( i % 2 == 0):
#         i += 1
#         continue    # skip
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     if( i % 2 != 0):
#         i += 1
#         continue    # skip
#     print(i)
#     i += 1



#--------------------------------- For Loop --------------------------------


# nums = [1,2,3,4]

# for val in nums:
#     print(val)

# nums = ['a','b','c','d']

# for val in nums:
#     print(val)

# nums = ('a','b','c','d')

# for val in nums:
#     print(val)

# str = "shahzain khan"

# for char in str:
#     print(char)

# nums = ('a','b','c','d')

# for val in nums:
#     if( val == 'c'):
#         print("found",val)
#         break    
#     print(val)
# else:
#     print("End")


#------------------------let's Practice--------------

#qs # 1

# nums = [1,4,9,16,25,36,79,64,81,100]

# for el in nums:
#     print(el)


#qs # 2

# x = int(input("Enter The Number B/W Tuples :"))

# nums = [1,4,9,16,25,36,79,64,81,100]

# idx = 0

# for el in nums:
#     if( el == x):
#         print("Element Found at idx",idx)
#         break
#     idx += 1


#----------------------- Range Function-----

# print(range(5))

# seq = range(5)

# for i in seq:
#     print(i)


# for i in range(5):   # range(stop)
#     print(i)

# for i in range(2,10):  # range(start,stop)
#     print(i)
    
# for i in range(2,10,2):    # range(start,stop,step)
#     print(i)

# for i in range(1,100,2):    # range(start,stop,step)
#     print(i)
    
# for i in range(1,101,2):    # range(start,stop,step)
#     print(i)

#--------------------let's practice------------
#qs # 1

# for el in range(1,101):
#     print(el)

#qs # 2

# for el in range(100,0,-1):
#     print(el)

#qs # 3

# n = int(input("Enter The Number :"))

# for el in range(1,11):
#     print(n,"*",el,"=",n*el)


#-------------------Pass statement------

# for i in range(10):
#     pass   

# print("Some useful work")


#---------------------------Let's Practice---------------

# qs # 1

# x = int(input("Enter the Number :"))
# i = 1
# sum = 0

# while i <= x:
#     sum += i
#     i +=1
# print("Total Sum is :",sum)


# qs # 2

x = int(input("Enter the Number :"))
fact = 1

for el in range( 1 , x+1):
    fact *= el
  
print("The factorial is :",fact)

































































































































