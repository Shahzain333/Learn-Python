import os

lst = []
x = int(input("Which Item Do You Want To Add :"))
count = 1

for i in range(x):
    inp = eval(input(f"Enter The {count} No Of Items : "))
    lst.append(inp)
    count += 1

print(lst)

def menu():
    os.system("Cls")
    
    lst = ["List Comprehension","Dictionary Comprehension","Set Comprehension","Exit"]
    
    flag = True
    while flag:
        
        for num , item in enumerate(lst,1):
           print(num,item)
           
        Choice = int(input("Enter Your Choice : "))
        
        if(Choice == 4):
           flag = False
           break
        else:
            match Choice:
                case 1:
                   list_comprehension()
                case 2:
                   dict_comprehension()
                case 3:
                   set_comprehension()
                
        wait = input("\nPlease Enter.......")

def list_comprehension():
    lst2 = [i for i in lst ]
    print(lst2)
 
def dict_comprehension():
    dict1 = {i : f"Item {i}" for i in lst }
    print(dict1)
    
    dict2 = {value : key for key,value in dict1.items()}
    print(dict2)

def set_comprehension():
    set1 = {i for i in lst }
    print(set1)

       
menu()







