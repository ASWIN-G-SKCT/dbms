from tkinter import*
from functools import partial
from tkinter.font import families
from tkinter import messagebox
from bed_booking import no_of_beds
import cx_Oracle
def back_function(room,block):
    room.destroy()
    block.deiconify()

def room_page_function(extra_index_for_block_indentifying,block):
    bg_2=PhotoImage(file="C:/coding/python/dbms_project/pngs/pexels-abdullah-ghatasheh-1631677 (2).png")
    room=Toplevel()
    block.withdraw()
    label1 = Label( room, image = bg_2)
    label1.place(x = 0,y = 0)
    room.geometry("1920x1080")
    x_axis=100
    y_axis=50
    st1="FLOOR "
    global button_dict
    button_dict = {}
    for floor in range(1,4):
        st1+=str(floor)
        l=Label(room,text=st1)
        l.place(x=x_axis,y=y_axis)
        st1="FLOOR "       
        no=floor*0
        y_axis+=50
        if(floor>=2):
            no=floor*100
            y_axis+=50
        sum1=0
        conn=cx_Oracle.connect('SYSTEM/aswin@localhost:1521/xe')
        cur =conn.cursor()
        for room_no in range(1,11):
                sum1=room_no+no 
               
                if(cur.callfunc('block_status',int,[extra_index_for_block_indentifying,room_no+no
                ])==0):          
                    button_dict[sum1]=Button(room,text=room_no+no,command=partial(no_of_beds,extra_index_for_block_indentifying,sum1,button_dict),bg="green",fg="black",activeforeground="white",
                    activebackground="blue",pady=10,padx=30)
                    button_dict[sum1].place(x=x_axis,y=y_axis)                    
                    x_axis+=100
                #cur.callproc('id_incrementor',[room_no+no])
                else:
                    button_dict[sum1]=Button(room,text=room_no+no,command=partial(no_of_beds,extra_index_for_block_indentifying,sum1,button_dict),bg="red",fg="black",activeforeground="white",
                    activebackground="blue",pady=10,padx=30)
                    button_dict[sum1].place(x=x_axis,y=y_axis)                    
                    x_axis+=100

                conn.commit()
        cur.close()                      
        x_axis=100
        y_axis+=100
    back_button=Button(room,text="back",command=partial(back_function,room,block),padx=30,pady=10)
    back_button.place(x=100,y=700)

    room.mainloop()
