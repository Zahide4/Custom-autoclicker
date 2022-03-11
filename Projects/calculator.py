from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Calculator")

def submit():
    firstno = first_no.get()
    secondno = second_no.get()
    if signbox == "+":
        ans = Label(text = firstno + secondno)
        ans.place(100, 100)

first_no= IntVar()
second_no= IntVar()

textbox1 = Entry(root, textvariable=first_no)
textbox1.pack()

textbox2 = Entry(root, textvariable=second_no)
textbox2.pack()

signvar = StringVar()
signbox = Entry(root, textvariable=signvar)
signbox.pack()

submit_btn = Button(text = "Submit", command=submit)
submit_btn.pack()

root.mainloop()
