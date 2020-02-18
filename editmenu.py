from tkinter import *
window=Tk()
menubar=Menu(window)
def display():
    print("hiiiiiiiiiiii")
def donothing():
    print("nothing to show")
filemenu = Menu(menubar, tearoff=0)    #add file menu
filemenu.add_command(label="New", command=display)  #add new bar
filemenu.add_command(label="Open", command=donothing)
menubar.add_cascade(label="file",menu=filemenu)
def display1():
    print("hiiiiiiiiiiii")
def display2():
    print("none")
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="New", command=display1)
editmenu.add_command(label="write", command=display2)
menubar.add_cascade(label="Edit",menu=editmenu)
window.config(menu=menubar)
window.mainloop()
