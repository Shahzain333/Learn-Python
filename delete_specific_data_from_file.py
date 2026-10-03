def load_data_from_file():
    
    database1 = ""
    data = open("dbms.txt","r")
    
    try:
        database1 = data.readlines()
    except Exception as e:
        print("Error in Loading File....",e)
        
    return database1

def delete_tsk():
        
    database4 = load_data_from_file()
    emails = []
    new_data = []
    
    for item in database4:
        parts = item.split("|")
        emails.append(parts[1].strip())
    
    try:
        
        email_inp = input("Enter The Email : ")
        idx = emails.index(email_inp)
        # print(idx)
        # print(database4)
        
        print(f"\nFound Data\n{database4[idx]}")
        
        
                    
        for num, item in enumerate(database4):
            if num == idx:
                pass
            else:
                new_data.append(item)
            
            data = open("dbms.txt","w")
            
            for item in new_data:
                data.writelines(item)
                
        print("\nDelete Task Successfully....")
        
    except ValueError:
        print("Error in Delete Task.......")   







