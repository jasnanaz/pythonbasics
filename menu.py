from tkinter import *
window=Tk()
menubar=Menu(window)
def display():
    print("hiii")
menubar.add_command(label="file",command=display)
# menubar.add_command(label="quit" command=window.quit)
window.config(menu=menubar)
window.mainloop()