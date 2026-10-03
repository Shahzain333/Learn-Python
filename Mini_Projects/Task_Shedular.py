import os

def main():
    
    os.system("Cls")
    
    lst = ["Add Task","Display Task","Update Task","Delete Task","Search Task","Exit"]
    flag = True
    
    while flag:
        heading("MENU")
 
        for num,item in enumerate(lst,1):
            print(f"{num}. {item}")
        
        closeline()
        
        choice = int(input("\nEnter Your Choice : "))
        if(choice == 6):
            flag = False
            break
        else:
            match choice:
                
                case 1:
                   add_tsk()
                case 2:
                    display_tsk()
                case 3:
                    update_tsk()
                case 4:
                    delete_tsk()
                case 5:
                    search_tsk()
                case 6:
                    exit()
        input("\nPlease Enter........")


def heading(name):
    os.system("Cls")
    print(f"--------------{name}---------------\n")

def closeline():
    print("--------------------------------") 
      
def add_tsk():
    os.system("Cls")   
    
    heading("Add Task")
    
    data = open("dbms.txt","a")
    try:
        while True:
            name = input("Enter The Name : ")
            email = input("Enter The Email : ")
            tsk = input("Enter The Task : ")
            date_time = input("Enter The Date & Time : ")
            yes_no = input("Do You Want To Add Another Task (yes/no) : ")
            
            data.writelines(f"{name} | {email} | {tsk} | {date_time} \n")
            
            if (yes_no == "no"):
                print("\nAdded Successfully........\n")
                break
               
    except Exception as e:
        print("Error is Add Task",e)            
    
    closeline()

def load_data_from_file():
    
    database1 = ""
    data = open("dbms.txt","r")
    
    try:
        database1 = data.readlines()
    except Exception as e:
        print("Error in Loading File....",e)
        
    return database1

def display_tsk():
    os.system("Cls")
    
    databse2 = load_data_from_file()
    
    try:
        
        for num,item in enumerate(databse2,1):
            print(f"{num}. {item}")
            
    except Exception as e:
        print("Error in display task.....",e)

def search_tsk():
    
    os.system("Cls")
    
    heading("SEARCH TASK")
     
    database3 = load_data_from_file()
    emails = []
        
    for item in database3:
        parts = item.split("|")
        emails.append(parts[1].strip())
        
    try:
        
        email_inp = input("Enter Your Email : ")
        
        find = emails.index(email_inp)
        
        print(f"\nFound Data\n{database3[find]}")
        
        
    except Exception as e:
        print("Error in Search Task.......",e)

def update_tsk():
    
    heading("UPDATE TASK")
    
    database4 = load_data_from_file()
    emails = []
    new_data = []
    
    for item in database4:
        parts = item.split("|")
        emails.append(parts[1].strip())
    
    try:
        
        email_inp = input("Enter The Email : ")
        idx = emails.index(email_inp)
        
        print(f"\nFound Data\n{database4[idx]}\n")
        
        with open("dbms.txt","w") as file:
        
           for num,item in enumerate(database4):
            
             if num == idx:
                parts2 = item.split("|")
                for count in range(4):
                    new_data.append(parts2[count].strip())
                # new_data.append(parts2[0].strip())
                # new_data.append(parts2[1].strip())
                # new_data.append(parts2[2].strip())
                # new_data.append(parts2[3].strip())
                
                update_name = input("The Name is : " + new_data[0])
                update_email = input(f"The Email is : " + new_data[1])
                update_tsk = input(f"The Task is : " + new_data[2])
                update_date_time =input(f"The date is : " + new_data[3])
                
                file.writelines(f"{update_name} | {update_email} | {update_tsk} | {update_date_time} \n")
                
             else:
                file.writelines(item)
        
    except Exception as e:
        print("Error in Update Task.......",e)
    
    
    
    # os.system("Cls")
    
    # heading("Update TASK")
    
    # database4 = load_data_from_file()
    # emails = []
    
    # for item in database4:
    #     parts = item.split("|")
    #     emails.append(parts[1].strip())
    
    # try:
        
    #     email_inp = input("Enter The Email : ")
    #     idx = emails.index(email_inp)
        
    #     print(f"\nFound Data\n{database4[idx]}")
        
    #     with open('dbms.txt','w') as file:
            
    #         for num,item in enumerate(database4):
    #             if idx == num:
    #                 # continue
    #                 name = input("Enter The Name : ")
    #                 email = input("Enter The Email : ")
    #                 tsk = input("Enter The Task : ")
    #                 date_time = input("Enter The Date & Time : ")
            
    #                 file.writelines(f"{name} | {email} | {tsk} | {date_time} \n")
    #             else:
    #                 file.writelines(item)
                    
    # except Exception as e:       
    #     print("\nData Updated Successfully....",e)
        
def delete_tsk():
    
    os.system("Cls")
    
    heading("DELETE TASK")
    
    database5 = load_data_from_file()
    emails = []
    
    for item in database5:
        parts = item.split("|")
        emails.append(parts[1].strip())
    
    try:
        
        email_inp = input("Enter The Email : ")
        idx = emails.index(email_inp)
        
        print(f"\nFound Data\n{database5[idx]}")
        
        with open('dbms.txt','w') as file:
            
            for num,item in enumerate(database5):
                if idx == num:
                    continue
                else:
                    file.writelines(item)
                
        print("\nDelete Task Successfully....")
        
    except Exception as e:
        print("Error in Delete Task.......",e)   
    
          
if __name__ == "__main__":    
    main()





























    