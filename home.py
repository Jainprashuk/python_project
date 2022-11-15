from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('     Parking Managment System')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


def login():
    root.destroy()
    import login


def sign_up():
    root.destroy()
    import sign_up

def login_error():
    messagebox.showerror("login", "login to use the services")

# .....................................................................................................................................................................

heading = Label(root,text="Welcome to Modern Parking Management System",bg='white',font=('Algerian',26,'bold')).place(x=55,y=50)


img = PhotoImage(file='main4.png')
Label(root,image=img,bg='white').place(x=525,y=100)
frame = Frame(root,bg='white',height='200',width='450').place(x=50,y=150)
Button(frame,width=25,pady=7,text="* see free parking slots",bg='white',fg='#57a1f8',border=0,command=login_error,font=('Microsoft YaHei UI Light',15),cursor='hand2').place(x=10,y=185)
Button(frame,width=25,pady=7,text="* book your slots now",bg='white',fg='#57a1f8',border=0,command=login_error,font=('Microsoft YaHei UI Light',15),cursor='hand2').place(x=255,y=185)
Button(frame,width=25,pady=7,text="* calculate expected fare ",bg='white',fg='#57a1f8',border=0,command=login_error,font=('Microsoft YaHei UI Light',15),cursor='hand2').place(x=120,y=255)
img1 = PhotoImage(file='hlogin.png')
Label(root,image=img1,bg='white').place(x=120,y=350)
img2 = PhotoImage(file='new1.png')
Label(root,image=img2,bg='white').place(x=330,y=350)
Button(root,width=25,pady=7,text="login now",bg='#57a1f8',fg='white',border=0,command=login,cursor='hand2').place(x=70,y=420)
Button(root,width=25,pady=7,text="register now",bg='#57a1f8',fg='white',border=0,command=sign_up,cursor='hand2').place(x=270,y=420)
footer = Label(root, relief=SUNKEN, anchor="w",height=2,bg="black",border=0)
footer.pack(side=BOTTOM, fill=X)
Label(footer,text="Copyright © 2022 Modern Parking System",fg='white',bg='black').place(x=80,y=4)
Label(footer,text="Terms and conditions",fg='white',bg='black').place(x=700,y=4)

root.mainloop()