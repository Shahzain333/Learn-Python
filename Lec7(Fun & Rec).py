#------------------- Function & Recursion-------------------------------

# def calc_sum (a,b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(4,3)
# calc_sum(24,3)
# calc_sum(4,53)
# print(calc_sum(2,3))

#----function definition 
# def calc_sum(a,b):   # parameter
#     return a + b

# print(calc_sum(3,4))

# sum = calc_sum(33,4)   # function call
# print(sum)


# def prit_hello():
#     print("Hello")

# prit_hello()
# prit_hello()
# prit_hello()
# prit_hello()


# def print_hello():
#     print("Hello")

# output = print_hello()

# print(output)  # None give

# ------ Average of 3 numbers -----

# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(2,4,6)


# print("Shahzain", end = " ")  # sep = " "
# print("Khan")   # end = \n


#----- Default Arguments---

# def calc_prod( a = 1 , b = 1 ):   # default parameters
#     print(a * b)
#     return a * b

# calc_prod()


# def calc_prod( a , b = 1 ):   # default parameters
#     print(a * b)
#     return a * b

# calc_prod(2)


# -------------------- Let's Practice ------------------------

# qs # 1

# cities = ["Karachi","Lahore","Punjab","Mumbai"]
# heroes = ["Thor","Bhajrangi","rocky"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)


# qs # 2

# def print_list(list):
#     for item in list:
#         print(item, end = " ")

# print_list(heroes)
# print()
# print_list(cities)


# qs # 3 

# def calc_fac(n):
#     fact = 1
#     for i in range(1 , n+1):
#         fact *= i   
#     print(fact)       
    
# calc_fac(n = int(input("Enter The Number :")))


# qs # 4

# def converter(usd_val):
#     inr_val = usd_val * 300
#     print(usd_val, "USD =", inr_val,"INR")


# converter(usd_val = int(input("Enter The Number :")))


# qs # 5 H.W

# def calc_string(n):
#     if( n % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# calc_string(n = int(input("Enter The Number :")))




#------------------------- Recursion ------------------------

# recursive function 

# def show(n):
#     if( n == 0 ):
#         return
#     print(n)
#     show(n-1)
#     print("End")
    
# show(int(input("Enter The Number :")))

# def fact(n):
#     if( n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(int(input("Enter The Number :"))))


# ----------------- Let's Practice -------------------------

# qs # 1

# def sum(n):
#     if( n == 0 ):
#         return 0
#     else:
#         return sum(n-1) + n
    
# print(sum(int(input("Enter The Number :"))))


# qs # 2

def print_list( list , idx = 0 ):
    if ( idx == len(list)):
        return
    print(list[idx])
    print_list( list , idx + 1)


fruits = ["Mango","Apple","Bannana","Litche","Watermelon"]

print_list(fruits)

































