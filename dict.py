dict_1={"user_1":input("enter your name"),
        "age_1":input("enter your age"),
        "address_1":input("enter your address")}
dict_2={"user_2":input("enter your name"),
     "age_2":input("enter your age"),
      "address_2":input("enter your address")}
list1=[]
list1.append(dict_1)
list1.append(dict_2)
print(list1)
name=input("enter a name from above list")
# name_tomatch=
for i in list1:
    for key,value in i.items():

        if value==name:
            print(i)


    # if i["user_1"]==name:
    #     print(i)
    # else:
    #     print("do not match")


