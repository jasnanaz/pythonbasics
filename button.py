from tkinter import *
window=Tk()
window.title("GUI WINDOW")
window.geometry("500x500")
label=Label(window,text="hello welcome to tkinter")
label.pack()
def display():
    label.config(text="button clicked")
button=Button(window,text="clickme",command=display)
button.pack()
window.mainloop()