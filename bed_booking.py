from multiprocessing import connection
from tkinter import* 
from functools import partial
from tkinter.font import families
import cx_Oracle
from update_room import update_floor_room
def booking_free(b1,r1,bed,bed_no,book_window):
    bed.withdraw()
    
    conn=cx_Oracle.connect('SYSTEM/aswin@localhost:1521/xe')
    cur =conn.cursor()
    cur.callproc('hostel_free',[b1,r1,bed_no])
    button_bed[bed_no].configure(background="green")
    bed.destroy()
    book_window.destroy()
    conn.commit()
    update_floor_room(b1,r1,button_dic)
    cur.close()
    
def booking_confirm(b1,r1,bed,bed_n1,book_window):
    bed.withdraw()
    conn=cx_Oracle.connect('SYSTEM/aswin@localhost:1521/xe')
    cur =conn.cursor()
    button_bed[bed_n1].configure(bg='red')
    cur.callproc('update_rooms',[b1,r1,bed_n1])
    conn.commit()
   
    #cur.callproc('update_floor_room',[b1,r1])
    # confirmation=Tk()
    # confirmation.title("Booking Confirmation ")
    bed.destroy()
    book_window.destroy()
    update_floor_room(b1,r1,button_dic)
    cur.close()
def booking_window(b1,r1,bed,bed_no,status):
    bed.withdraw()
    book_window=Tk()
    book_window.resizable(False,False)
    book_window.title("BOOKING window")
    
    Book_Button=Button(book_window,text="book",command=partial(booking_confirm,b1,r1,bed,bed_no,book_window))
    UnBook_Button=Button(book_window,text="unbook",command=partial(booking_free,b1,r1,bed,bed_no,book_window))
    if(status==1):
       # status_book_button=DISABLED
       Book_Button["state"]=DISABLED

    else:
        UnBook_Button["state"]=DISABLED
    Book_Button.place(x=50,y=50)
    UnBook_Button.place(x=100,y=50)
    book_window.mainloop()
def no_of_beds(block_no,room_no,button_dict):
   
    global button_dic
    button_dic=button_dict
    connection=cx_Oracle.connect("SYSTEM/aswin@localhost:1521/xe")
    cur=connection.cursor()
    bed=Tk()
    bed.geometry("200x230")
    bed.resizable(False,False)
    global button_bed
    button_bed={}
    x_axis=20
    y_axis=60
    bed_label=Label(bed,text="ROOMS",font=("Abril fatface",20))
    bed_label.place(x=5,y=0)
    for i in range(1,3):
        if(cur.callfunc('button_c_ch',int,[block_no,room_no,i])==0):
            button_bed[i]=Button(bed,text=i,bg='green',command=partial(booking_window,block_no,room_no,bed,i,0),padx=30,pady=20)
            button_bed[i].place(x=x_axis,y=y_axis)
            x_axis+=80
        else:
            button_bed[i]=Button(bed,text=i,bg='red',command=partial(booking_window,block_no,room_no,bed,i,1),padx=30,pady=20)
            button_bed[i].place(x=x_axis,y=y_axis)
            x_axis+=80
    x_axis=20
    y_axis=130
    for i in range(3,5):
        if(cur.callfunc('button_c_ch',int,[block_no,room_no,i])==0):
            button_bed[i]=Button(bed,text=i,bg='green',command=partial(booking_window,block_no,room_no,bed,i,0),padx=30,pady=20)
            button_bed[i].place(x=x_axis,y=y_axis)
            x_axis+=80
            #y_axis+=20
        else:
            button_bed[i]=Button(bed,text=i,bg='red',command=partial(booking_window,block_no,room_no,bed,i,1),padx=30,pady=20)
            button_bed[i].place(x=x_axis,y=y_axis)
            x_axis+=80
    
    bed.mainloop()

