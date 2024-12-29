from  tkinter import *
from tkinter import messagebox


def login_button():
    email=email_input.get()
    password=password_input.get()
    if email=='abc@gmail.com' and password=='1234':
        messagebox.showinfo('Login successful')
    else:
        messagebox.showinfo('Wrong email or password')

root=Tk()

root.title("Login")
#root.minsize(600,600)
#root.maxsize()
root.geometry('500x600')
root.configure(background='#000') # red , black etc.

text_lable=Label(root,text="Hello",fg='white',bg='#000')
text_lable.pack()
text_lable.configure(font=(59))

email_label = Label(root,text='Enter Email',fg='white',bg='#000')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root,text='Enter Password',fg='white',bg='#000')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=login_button)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))


root.mainloop()
