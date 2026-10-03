import os

def heading(name):
    os.system("Cls")
    print(f"---------------{name}---------------\n")

def closeline():
    print("--------------------------------\n") 

def add_pizza():
    
    heading("ADD PIZZA")
    
    file = open ("dbMS.txt","a")
        
    try:
        while True:
            pizza_name = input("Enter The Pizza : ")
            pizza_price = int(input("Enter The Pizza price : "))
            yes_no = input("Do You Want To Add More Pizza's : ")
                
            file.writelines(f"{pizza_name} | {pizza_price} \n")
                
            if (yes_no == "no"):
                print("Added Successfully.......\n")
                break
           
    except Exception as e:
            print("Error in Add Pizza :",e)        
    closeline()
    
def load_data_from_file():
    
    database = ""
    file = open("dbMS.txt","r")
    
    try:
        database = file.readlines()
    except Exception as e:
        print("Error is load Data From file ",e)   
    
    return database 
       
def display_pizza():
    
    heading("MENU") 
   
    database = load_data_from_file()
   
    for count,content in enumerate(database,1):
       print(f"{count}. {content}")
   
    closeline()

def generate_bill():
    
    customer_pizza_num = []
    customer_quantity_num = []
    content = load_data_from_file()
    
    # heading("GENERATING BILL")
    display_pizza()
    
    while True:
        pizza_num = int(input("Enter The Pizza No : "))
        pizza_quantity = int(input("Enter The Quantity No : "))
        yes_no = input("Enter Another bill (yes/no) : ")
        
        customer_pizza_num.append(pizza_num-1)
        customer_quantity_num.append(pizza_quantity)
        
        if(yes_no == "no"):
            print("Bill Generate Successfully......")
            break
        
    print_bill(customer_pizza_num,customer_quantity_num,content)
    
def print_bill(customer_pizza_num,customer_quantity_num,content):
    
    customer_order = []
    prices = []
    price_and_quantity = []
    
    heading("Print Bill")
    
    for i in customer_pizza_num:
        customer_order.append(content[i])
    
    for item in customer_order:
        parts = item.split("|")
        price = parts[1]
        prices.append(int(price))
      
    total = 0  
    for num,value in enumerate(prices):
        price_of_pizza = value * customer_quantity_num[num]
        total = total + price_of_pizza
        price_and_quantity.append(price_of_pizza)
        
    for num, i in enumerate(customer_order):
        print(f'{num+1}. {i}countity : {customer_quantity_num[num]} --> {price_and_quantity[num]}\n')

    closeLine()
            
def menu():
    
    lst = ["Add Pizza","Display Pizza","Generate Bill","Delete Pizza","Search Pizza","Exit"]
    flag = True
    
    while flag:
        
        heading("RMS")
        
        for num,item in enumerate(lst,1):
           print(num,item)
           
        closeline()
        
        choice = int(input("Enter Your Choice : "))
    
        if(choice == 6):
            flag = False
            break
        else:
            match choice:
                case 1:
                   add_pizza()
                case 2:
                   display_pizza()
                case 3:
                    generate_bill()
                case 4:
                   delete_pizza()
                case 5:
                    search_pizza()
    
        wait = input("\nPlease Enter.......")
 
if __name__ == '__main__':
   menu()





























