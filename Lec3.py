#----------------------List & Tuple --------------------

# marks = [34,24,35,67,78,89]

# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[2])
# print(len(marks))

# #-------for positive Slicing (indexing)
# print(marks[1:4])
# print(marks[:3])
# print(marks[1:])

# #-------for Negative Slicing (indexing)
# print(marks[-6:-1])
# print(marks[-3:-1])
# print(marks[-6:])
# print(marks[:-2])

# Student = ["Shahzain",85,"Karachi"]

# print(Student)
# print(Student[0])
# print(len(Student))

# Student[0] = "Khan" # Allowable in list but not allowed in string 
# print(Student)

#--------------list Methood-------
# Ordered Collection of elements
# Enclosed in [] square brackets
# Mutable (can be changed)

# list = [34,24,35,67,78,89]
# list.append(40)

# print(list)

# list.sort()

# print(list)

# list.sort(reverse=True)

# print(list)

# list.reverse()

# print(list)

# print(list.append(10))

# print(list)

# list.insert(2,100)
# print(list)

# list3 = [2,1,3,1]

# list3.remove(1)
# print(list3)

# list3.pop(1)
# print(list3)

# list2 = ["banana","litche","apple"]

# list2.sort()
# print(list2)

# list2.sort(reverse=True)
# print(list2)


#-------------------------------Tuples-----------------------
# Ordered collection of element
# enclosed in () round brackets
# Different kind of element can be stored in tuple
# Tuples are immutable (cannot be changed)

# tup = (54,89,98,11,23)

# print(type(tup))
# print(tup[0])
# print(tup[1])
# print(tup[3])

# tup1 = ()
# print(tup1)
# print(type(tup1))

# tup3 = (1)
# print(type(tup3))
# print(tup3)

# tup2 = (1,)
# print(tup2)

#----------Positive Slicing-----

# print(tup[1:4])
# print(tup[1:])
# print(tup[:4])


# #----------Negative Slicing-----

# print(tup[-4:-1])
# print(tup[-3:])
# print(tup[:-1])


#------------Tuple Methods ----------

# tup = (1,2,3,4,2,1,3,5,6,7)

# print(tup.index(4))

# print(tup.count(2))


#--------------------Lets Practice------------------

#--1st Methood

# movies = [] # There is empty List Now

# movie1 = input("Enter The First Movie name :")
# movie2 = input("Enter The Second Movie name :")
# movie3 = input("Enter The Third Movie name :")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)

#---2nd Methood

# movies = [] # There is empty List Now

# mov = input("Enter The First Movie name :")
# movies.append(mov)
# mov = input("Enter The Second Movie name :")
# movies.append(mov)
# mov = input("Enter The Third Movie name :")
# movies.append(mov)

# print(movies)



#---3rd Methood

# movies = [] # There is empty List Now

# movies.append(input("Enter The First Movie name :"))

# movies.append(input("Enter The Second Movie name :"))

# movies.append(input("Enter The Third Movie name :"))


# print(movies)


# list1 = [1,2,1]

# list2 = [1,2,3]

# copy_list1  = list1.copy()
# copy_list1.reverse()

# if( copy_list1 == list1 ):
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
# copy_list2 = list2.copy()
# copy_list2.reverse()

# if( copy_list2 == list2 ):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# list3 = ["m","a","a","m"]

# copy_list3  = list3.copy()
# copy_list3.reverse()

# if( copy_list3 == list3 ):
#     print("Palindrome")
# else:
#     print("Not Palindrome")



grade = ("C","D","A","B","A","E")
print(grade.count("A"))

grade = ["C","D","A","B","A","E"]
grade.sort()
print(grade)
















































































