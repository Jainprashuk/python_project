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
    username=user.get()
    passkey=password.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and passkey==r[username]:
        print('logged in successully')
        root.destroy()
        import home2_farecal_book_status
    else:
        messagebox.showerror("Invalid","Invalid Credentials")

def sign_up():
    root.destroy()
    import sign_up

# .............................................................................................................................

img = PhotoImage(file='loginf.png')
Label(root,image=img,bg='white').place(x=80,y=80)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=500,y=80)

heading = Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)

# ..............................................................................................................................

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=75,y=100)
user.insert(0,'username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=250,height=2,bg='black').place(x=70,y=125)

# ........................................................................................................................................

def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'password')

password = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
password.place(x=75,y=170)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)
Frame(frame,width=250,height=2,bg='black').place(x=70,y=195)

# .............................................................................................................................

Button(frame,width=35,pady=7,text="sign in",bg='black',fg='white',border=0,command=login,cursor='hand2').place(x=70,y=220)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=95,y=270)
signup = Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign_up)
signup.place(x=235,y=270)

root.mainloop()