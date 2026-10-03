# -------- using loops -----

marks = [20,30,40,50,60]
new_marks = []

for x in marks:    
    new_marks.append(x+2)
print("Using Loop : ",new_marks)

# ------ using list comprehension 

marks = [20,30,40,50,60]
new_marks = [ x + 2 for x in marks ]
print("Using list comprehension" , new_marks)

# ----- using loops

cubes = []
for x in range(11):
    if( x % 2 == 0):
        cubes.append(x ** 3)    
print("Using Loops :",cubes)

# ---- using list comprehension 

cubes = [ x ** 3 for x in range(11) if x % 2 == 0 ]
print("List Comprehension" ,cubes)















