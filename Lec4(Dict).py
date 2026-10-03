#------------------------Dictionary in python------------------
# An unordered collections of elements
# Key and Value pair
# curly braces {} are used to define dictionary
# Mutable (can be changed)

info = {
    "Name" : "Shahzain",
    "Subjects" : ["Python","Java","C++"],
    "Topics" : ("Dictionary","Set"),
    "Learning" : "Coding",
    "Marks" : 94.5,
    "Age" : 23,
    "is_Adult" : True,
}

# print(info)
# print(type(info))

# print(info["Name"])
# print(info["Subjects"])
# print(info["Topics"])
# print(info["Learning"])

# info["Name"] = "Khan"
# info["SurName"] = "Niazi"
# print(info)


# null_dict = {}   # Null Dictionary in python ----

# null_dict["Name"] = "ApnaCollege"


# print(null_dict)


Student = {
    "Name" : "Shahzain",
    "Score" :{
        "Os" : 90,
        "Se" : 82,
        "Nc" : 94.5
    }
}

# print(Student)
# print(Student["Score"])
# print(Student["Score"]["Se"])

#----------Dict Method-----

# print(list(Student.keys()))

# print(len(Student))

# print(len(list(Student.keys())))


# print(list(Student.values()))

# print(len(list(Student.values())))

# print(Student.items())

# print(list(Student.items()))

# pairs = list(Student.items())

# print(pairs[0])
# print(pairs[1])
# print(pairs[1][2])

# print(Student["Name"])       #it will show error age glt parameters dain toh
# print(Student.get("Name"))   # it will Show None agr glt parameter dain toh


# print(Student["Name2"])       
# print(Student.get("Name2")) 

# Student.update({"City" : "Karachi"})
# print(Student)

# new_dict = {"Name" : "Khan" , "City" : "Karachi" , "Age" : 16}
# Student.update(new_dict)
# print(Student)



#-----------------------Set In Python--------------------------------------------
# Unordered & Unindexed collection of elements
# Enclosed in {} curly braces
# No duplicate elements allowed

# collection = {1,2,3,4}

# print(type(collection))
# print(collection)

# collection = {1,2,3,4,"hi","hello"}

# print(collection)
# print(type(collection))


# collection = {1,2,3,4,2,3,"hi","hello","hi"}

# print(collection)
# print(type(collection))
# print(len(collection))

# null_set = set()

# print(null_set)
# print(type(null_set))

# null_set.add(1)
# null_set.add(2)
# null_set.add(3)
# null_set.add(2)
# null_set.add(5)
# null_set.add(4)
# null_set.add(5)
# null_set.add("Shahzain")

# print(null_set)

# null_set.remove(2)

# print(null_set)

# null_set.clear()

# print(null_set)

# collection = {"Apna college","Python","C++","Java"}

# print(collection.pop())
# print(collection.pop())


# set1 = {1,2,3}
# set2 = {2,3,4,5}

# print(set1.union(set2))
# print(set1)
# print(set2)

# print(set1.intersection(set2))  # common values return





#---------------------------Let's practice --------------------------

# dict = {
#     "Cat" : "A Small Cat",
#     "Table" : ["A Piece Of Furniture","List of facts $ figure"]
# }

# print(dict)


# set = {"python" , "java" , "C++" , "python" , "js" , "java" , "python" , "java" , "C++" , "C"}

# print(set)
# print(len(set))


# marks = {}

# x = int(input("Enter  Phy  Marks :"))
# marks.update({"Phy" : x})

# x = int(input("Enter  Chem  Marks :"))
# marks.update({"Chem" : x})

# x = int(input("Enter  Math  Marks :"))
# marks.update({"Math" : x})

# print(marks)

# null_set = set()

# null_set.add(9)
# null_set.add(9.0)
# null_set.add("9.0")

# print(null_set)





# Values = {
#     ("float" , 9.0),
#     ("int" , 9)
# }

# print(Values)































































































