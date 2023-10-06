from tkinter import *
import getpass
#password=getpass.getpass()
root=Tk()
root.geometry("500x300")
def getvals():
    print("Acccepted")
Label(root, text="LOGIN",font="arial 18 bold").grid(row=0,column=3)
username=Label(root, text="Username")
password=Label(root, text="Password")
username.grid(row=1,column=2)
password.grid(row=2,column=2)
usernamevalue=StringVar
passwordvalue=StringVar
checkvalue=IntVar
usernameentry=Entry(root, textvariable=usernamevalue)
passwordentry=Entry(root, textvariable=passwordvalue)
usernameentry.grid(row=1,column=3)
passwordentry.grid(row=2,column=3)
#password=getpass.getpass()
checkbtn=Checkbutton(text="proceed submit", variable=checkvalue)
checkbtn.grid(row=3,column=4)
Button(text="SUBMIT",command=getvals).grid(row=4,column=4)
root.mainloop()