from sre_parse import State
from tkinter import*
from functools import partial
from tkinter.font import families
from tkinter import messagebox
from block_page import block_page_function
import cx_Oracle
#     INPUT for login andpassword
def input_login(login,password):
    check_login_id=Text_field_login.get(1.0,"end-1c")
    check_password=Text_field_password.get(1.0,"end-1c")
    connection=cx_Oracle.connect('SYSTEM/aswin@localhost:1521/xe')
    cur =connection.cursor()
    if(check_password!=""):            
        verify=cur.callfunc('return_login_id',str)
        verify_password=cur.callfunc('return_password',str)
        # l=Label(canvas_for_homepage,text=var)
        # l.place(x=100,y=100)
        if(check_login_id==verify):
            if(check_password==verify_password):
               login.delete(1.0,END)
               password.delete(1.0,END)
               block_page_function(welcome_page)
            else:
                messagebox.showinfo("Error","Wrong Password,Check again! :(")
                login_buuton_function()
        else:
            messagebox.showinfo("Error","Wrong Login_Id,Check again! :(")
            login_buuton_function()
        
    else:
        messagebox.showinfo("error")
        login_buuton_function()
    login.delete(1.0,END)
    password.delete(1.0,END)
    connection.commit()
    cur.close()
    return 0









welcome_page=Tk()
#welcome_page.geometry("1980x1080")
welcome_page.title("LOGIN PAGE")
bg=PhotoImage(file="C:/coding/python/dbms_project/pngs/homepage.png")
# canvas CREATION 
canvas_for_homepage=Canvas(welcome_page,height=1080,width=1920)
canvas_for_homepage.pack(fill = "both", expand = True)
canvas_for_homepage.create_image( 0, 0, image = bg,anchor = "nw")
# FRAME CREATION
login_field=Frame(canvas_for_homepage,width=320,height=300,bg="WHITE")

Text_field_login=Text(canvas_for_homepage,height=1.5,width=30,bg="#d5e2e3",font=("Abril fatface",10))
Text_field_password=Text(canvas_for_homepage,height=1.5,width=30,bg="#d5e2e3",font=("Abril fatface",10))
welcome_text=canvas_for_homepage.create_text(500,50,text="Hostel Management System",font=('Abril fatface',30),fill="white") 
login_label=Label(canvas_for_homepage,text="Login",font=("",20),fg="black",bg="white")
password_label=Label(canvas_for_homepage,text="Password",font=("",20),fg="black",bg="white")
def login_buuton_function():
            login_button=Button(canvas_for_homepage,text="Login",command=partial(input_login,Text_field_login,Text_field_password),bg='white',fg='black',padx=5,pady=5,)
            login_button.place(x=600,y=450)
login_buuton_function()
#login
#Text_field_login.insert(INSERT,'SYSTEM')
# Text_field_password.insert(INSERT,'aswin')
login_label.place(x=420,y=220)
Text_field_login.place(x=420,y=270)
login_field.place(x=400,y=200)
#passowrd
password_label.place(x=420,y=320)
Text_field_password.place(x=420,y=380)


welcome_page.mainloop()

