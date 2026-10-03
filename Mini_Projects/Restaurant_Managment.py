import os
# from openpyxl import Workbook
def leading_page():
    os.system('cls')
    choice=int(input("1)To Add Dishes\n2)To Show Dishes\n3)To Exit\nEnter Your Choice:"))
    match choice:
        case 1:
            add_dish()
            leading_page()
        case 2:
            display_menu()
        case 3:
            exit_program()
        case _:
            print("Invalid Option")

def add_dish():
    os.system("cls")
    dish_name=input("Enter the name of the dish: ")
    dish_price=float(input("Enter the price of the dish: "))
    try:
        with  open ("Dishes.xlsx","a+") as file:
            file.write(f"{dish_name},{dish_price}\n")
    except Exception as e:
        print(e)
    print("Dish added successfully!")
    choice=input("Do you want to add more Dishes 'Y/N':")
    if choice.lower() == 'y' :
        add_dish()
    else:
        leading_page()
def display_menu():
    prices=[] 
    names=[]#
    order_list={}
    print("\n---------MENU----------\n")
    try:
        with open(r"Dishes.xlsx", "r") as file:
            data=file.readlines()
    except Exception as e:
        print(e)
    for x, key in enumerate(data):
        dish_name, dish_price = key.strip().split(',')
        print(f"{x}. {dish_name}    {dish_price}")
        prices.append(dish_price) #
        names.append(dish_name)
    print("-----------------------\n")
    new_dic={name:float(price) for name,price in zip(names,prices)}
    choice="y"
    total=0
    countity = []
    while(choice.lower()!='n'): 
        order_selection=int(input("Enter the dish number to order: "))
        plate=int(input("How many plate do You want to of this Dish: "))
        countity.append(plate)
        for index,(name,price) in enumerate(new_dic.items()):
            if order_selection == index:
                total += (price)*plate
                # price=price*2
                order_list.update({name:price})
        choice=input("Do You want to add some more item (Y/N): ")
    os.system("cls")
    print(order_list)
    print("You Order the food Following  :")
    for num,(name,price) in enumerate(order_list.items()):
        print(f"{name}: {price} ---> countity: {countity[num]}")
    print("Total Bill is: ",total)
    input("Please! Press Enter key to go in Main Menu:")
    os.system('cls')
    leading_page()


def exit_program():
    print("Exiting the Program:")
    exit()
leading_page()  
