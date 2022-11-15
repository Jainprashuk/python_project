from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)
# .............................................................................................................................
def login():
    root.destroy()
    import login

def signup():
    username=user.get()
    passkey=password.get()
    cpasskey=cpassword.get()
    mobile_no = number.get()

    if passkey == cpasskey:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:passkey}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('signup','sucessfully signed up')

        except:
            file=open('datasheet.txt','w')
            pp=str({'username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('invalid','both password should match')




# .............................................................................................................................

img = PhotoImage(file='signupfi.png')
Label(root,image=img,bg='white').place(x=80,y=70)

frame = Frame(root,width=350,height=450,bg='white')
frame.place(x=500,y=60)

heading = Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)

# ..............................................................................................................................

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'name/email')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=75,y=90)
user.insert(0,'name/email')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=250,height=2,bg='black').place(x=70,y=115)

# ........................................................................................................................................

def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'password')

password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
password.place(x=75,y=140)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
Frame(frame,width=250,height=2,bg='black').place(x=70,y=165)

# ........................................................................................................................................

def on_enter(e):
    cpassword.delete(0,'end')
def on_leave(e):
    name=cpassword.get()
    if name=='':
        cpassword.insert(0,'confirm password')

cpassword = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
cpassword.place(x=75,y=190)
cpassword.insert(0,'confirm Password')
cpassword.bind('<FocusIn>',on_enter)
cpassword.bind('<FocusOut>',on_leave)
Frame(frame,width=250,height=2,bg='black').place(x=70,y=215)

# ........................................................................................................................................

def on_enter(e):
    number.delete(0,'end')
def on_leave(e):
    name=number.get()
    if name=='':
        number.insert(0,'mobile number')

number = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
number.place(x=75,y=240)
number.insert(0,'mobile number')
number.bind('<FocusIn>',on_enter)
number.bind('<FocusOut>',on_leave)
Frame(frame,width=250,height=2,bg='black').place(x=70,y=265)

# .............................................................................................................................

Button(frame,width=35,pady=7,text="sign up",bg='#57a1f8',fg='white',border=0,command=signup).place(x=70,y=275)
label = Label(frame,text="Alredy have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=95,y=310)
signin = Button(frame,width=6,text='login',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=login)
signin.place(x=235,y=311)

root.mainloop()












