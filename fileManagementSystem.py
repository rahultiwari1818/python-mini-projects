import datetime
#function definition
def gettime():
    return datetime.datetime.now()

def rahul():
    print("\n enter 1 for log: \n enter 2 for data retrival:")
    data_choice=int(input(""))
    if data_choice==1:
        rahul_log()
    elif data_choice==2:
        rahul_retrival()
    else:
        print("\n enter proper number")

def rahul_log():    
    print("\n enter 1 for food \n enter 2 for exercise:")
    choice=int(input("enter ur choice:"))
    if choice==1:
        rahul_food()
    elif choice==2:
        rahul_exe()
    else:
        print("\n enter proper choice")

def rahul_retrival():
    print("\n enter 1 for food:\n enter 2 for exercise:")
    choice=int(input(""))
    if choice==1:
        rahul_food_ret()
    elif choice==2:
        rahul_exe_ret()
    else:
        print("\n enter proper number.")





def lucky():
    print("\n enter 1 for log: \n enter 2 for data retrival:")
    data_choice=int(input(""))
    if data_choice==1:
        lucky_log()
    elif data_choice==2:
        lucky_retrival()
    else:
        print("\n enter proper number")

def lucky_log():
    print("\n enter 1 for food \n enter 2 for exercise:")
    choice=int(input("enter ur choice:"))
    if choice==1:
        lucky_food()
    elif choice==2:
        lucky_exe()
    else:
        print("\n enter proper choice")

def lucky_retrival():
    print("\n enter 1 for food:\n enter 2 for exercise:")
    choice=int(input(""))
    if choice==1:
        lucky_food_ret()
    elif choice==2:
        lucky_exe_ret()
    else:
        print("\n enter proper number.")

def rahul_food():
    print("enter ur data:\n")
    with open("rahul_food.txt","a") as pointer:
        data=input("")
        pointer.write(str(gettime())+" : "+data+"\n")
    print("data successfully entered.!!!!")

def rahul_exe():
    print("enter ur data:\n")
    with open("rahul_exe.txt","a") as pointer:
        data=input("")
        pointer.write(str(str(gettime()))+ " : "+data+"\n")
    print("data successfully entered.!!!!")

def rahul_food_ret():
##    print("enter ur data:\n")
    with open("rahul_food.txt") as pointer:
####        time=datetime.datetime.now()
##        pointer.write(time)
        print(pointer.read())
    print("data successfully retrived.!!!!")

def rahul_exe_ret():
##    print("enter ur data:\n")
    with open("rahul_exe.txt") as pointer:
        print(pointer.read())
    print("data successfully retrived.!!!!")

        

def lucky_food():
    print("enter ur data:\n")
    with open("lucky_food.txt","a") as pointer:
####        time=datetime.datetime.now()
##        pointer.write(time)
        data=input("")
        pointer.write(str(gettime())+" : "+data+"\n")
    print("data successfully entered.!!!!")

def lucky_exe():
    print("enter ur data:\n")
    with open("lucky_exe.txt","a") as pointer:
        data=input("")
        pointer.write(str(gettime())+" : "+data+"\n")
    print("data successfully entered.!!!!")

def lucky_food_ret():
##    print("enter ur data:\n")
    with open("lucky_food.txt") as pointer:
####        time=datetime.datetime.now()
##        pointer.write(time)
        print(pointer.read())
    print("data successfully retrived.!!!!")

def lucky_exe_ret():
##    print("enter ur data:\n")
    with open("lucky_exe.txt") as pointer:
        data=input("")
        pointer.write(str(gettime()),"+ value +",data)
    print("data successfully retrived.!!!!")


if __name__=='__main__':
    print("hey\n this is food management system.")
    print("\n enter 1 for rahul \n enter 2 for lucky")
    name=int(input("enter plz:"))
    if name==1:
        rahul()
    elif name==2:
        lucky()
    else:
        print("enter proper number.")

