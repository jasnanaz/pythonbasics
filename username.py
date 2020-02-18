import mysql.connector
from tkinter import *
window=Tk()
window.title("LOGIN")
window.geometry("500x500")
label1=Label(window,text="username")
label1.grid(row=0,column=0)
# label1.pack()
entry1=Entry(window)
entry1.grid(row=0,column=1)
label2=Label(window,text="password")
label2.grid(row=1,column=0)
entry2=Entry(window)
entry2.grid(row=1,column=1)
def display1():
    user=entry1.get()
    password=entry1.get()
    mydb = mysql.connector.connect(
        host="192.168.1.250",
        user="scopeinternship",
        password="scopeinternship",
        database="scopeinternship"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select * from logingui")
    show = mycursor.fetchall()
    flag=0
    for i in show:
        if user==i[0] and password==i[1] :
            flag=1
    if flag == 1:
        print(" match")
    else:
        print("do not match")
button=Button(window,text="login",command=display1)
button.grid(row=2,column=1)
window.mainloop()
