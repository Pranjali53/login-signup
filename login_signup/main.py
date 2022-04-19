import json
import os
from re import L 
user=input("What do you want to do? login or signup! \n For login press:-2 :-  \n For signup press:-1 :- ")
G_dic={ }
L_dic={ }
G_list=[ ]
if user=="1":
    user_name=input("Plase enter your name :- ")
    password1=input("enter password :- ")
    l, u, p, d = 0, 0, 0, 0
    if (len(password1) >= 8):
        for i in password1:
            if (i.islower()):
                l+=1
            if (i.isupper()):
                u+=1
            if (i.isdigit()):
                d+=1
            if(i=='@'or i=='$' or i=='_'):
                p+=1        
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password1)):
        password2=input("confirm the password :- ")
        if password1==password2:
            print("congrats",user_name,"you are signed up successefully")
            discription=input("enter your discription :- ")
            birth_date=input("Date of birth :- ")
            gender=input("Gender :- ")
            hobbies=input("Hobbies :- ")
            L_dic["user_name"]=user_name
            L_dic["Password"]=password1
            L_dic["Discription"]=discription
            L_dic["Birth_date"]=birth_date
            L_dic["Gender"]=gender
            L_dic["Hobbies"]=hobbies
            if os.path.exists("userdetails.json")==True:
                file=open("userdetails.json")
                p_data=json.load(file)
                G_list=p_data["user"]
                G_list.append(L_dic)
                G_dic["user"]=G_list
                file=open("userdetails.json","w")
                json_data=json.dump(G_dic,file,indent=4)
                file.close()
            else:
                G_list.append(L_dic)
                G_dic["user"]=G_list
                file=open("userdetails.json","w")
                json_data=json.dump(G_dic,file,indent=4)
                file.close()
        else:
            print("Both password are not same")
    else:
       print('your password is not valid')            
elif user=="2":
    user_name=input("Plase enter your name :- ")
    password1=input("Password :- ")
    file=open("userdetails.json","r")
    data=False
    new=json.load(file)
    for i in new["user"]:
        if i["user_name"]==user_name and i["Password"]==password1:
            data=True
            print(i)
            break
    if data==False:
        print("Invalid user_name and password")
else:
    print("please choose only 1 or 2")