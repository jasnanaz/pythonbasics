from tkinter import *
window=Tk()
menubar=Menu(window)
def display():
    print("hiiiiiiiiiiii")
filemenu = Menu(menubar, tearoff=0)    #add file menu
filemenu.add_command(label="New", command=display)  #add new bar
menubar.add_cascade(label="file",menu=filemenu)
# filemenu.add_command(label="Open", command=donothing)
window.config(menu=menubar)
window.mainloop()