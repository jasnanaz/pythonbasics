from tkinter import *
window=Tk()
window.title("frame1")
window.geometry("100x100")
# window.geometry("500X500")
frame1=Frame(window)
frame1.pack()
window.title("frame2")
window.geometry("200x200")
# window.geometry("500X500")
frame2=Frame(window)
frame2.pack()
window.mainloop()