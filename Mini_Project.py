
# # --------------------------- Guess The No -------------------

# import random

# target = random.randint( 1 , 100 )

# while True:
#     userChoice = input("Guess The Target or Quit(Q) :")
    
#     if(userChoice == "Q"):
#         break
    
#     userChoice = int(userChoice)
    
#     if(userChoice == target):
#         print("Success : Correct Guess !!")
#         break
#     elif(userChoice < target):
#         print("Your No was too small. Take a bigger Guess....")
#     else:
#         print("Your No was too big. Take a smaller Guess....")
    
# print("------- Game Over -------")




# --------------------------- Random Password Generator -------------------

import random
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

# pass_len = 12
# charVal = string.ascii_letters + string.digits + string.punctuation
# # print(charVal)

# password = ""
# for i in range(pass_len):
#     password += random.choice(charVal)
    
# print("Your Random Password is :" ,password)

# --------- For List Comprehension [function for i in range(n)]------------------

pass_len = 12
charVal = string.ascii_letters + string.digits + string.punctuation

# result = [random.choice(charVal) for i in range(pass_len)]
# print(result)

# ---------- join(All the list words)-----

result = "".join([random.choice(charVal) for i in range(pass_len)])
print("Your Random password is:",result)





























































































