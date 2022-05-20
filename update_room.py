import  cx_Oracle
import config
from tkinter import*
from functools import partial
from tkinter.font import families
def update_floor_room(b1,r1,b):
    #b[r1].config(bg='green')
    conn=cx_Oracle.connect('SYSTEM/aswin@localhost:1521/xe')
    cur =conn.cursor()
    check1=1
    s=0
    for i in range(1,5):

        if(cur.callfunc('bed_status',int,[b1,r1,i])==0):
            check1=0
            break
  
    if(check1==1):
       sql=('update hostel set book_status =1 where block_no= :block_no and room_no= :room_no')
       cur.execute(sql,block_no=b1,room_no=r1)
       b[r1].configure(background="red")
    else:
        sql=('update hostel set book_status =0 where block_no= :block_no and room_no= :room_no')
        cur.execute(sql,block_no=b1,room_no=r1)     
        b[r1].configure(background="green")
    conn.commit()
    cur.close()
    return 0
#update_floor_room(1,305,)