#from room_page import room_page_function
from tkinter import*
from functools import partial
from tkinter.font import BOLD, families
from tkinter import messagebox
from room_page import room_page_function
#from PIL import ImageTk,Image
def back_function(welcome_page,block):
    block.destroy()
    welcome_page.deiconify()
def block_page_function(welcome_page):       
    block=Toplevel()
    block.title('BLOCKS')
    welcome_page.withdraw()
    bg_1=PhotoImage(file="C:/coding/python/dbms_project/pngs/pexels-abdullah-ghatasheh-1631677 (2).png")
    canvas_for_block_page=Canvas(block,height=1080,width=1920)
    canvas_for_block_page.pack(fill = "both", expand = True)
    canvas_for_block_page.create_image(0,0, image = bg_1,anchor = "nw")
   # block.geometry("1920x1080")
    text_top_bar=canvas_for_block_page.create_text(440,50,text="CHOOSE A BLOCK",font=("Abril fatface",30,BOLD),fill='BLACK')
    block_1=Button(canvas_for_block_page,text="BLOCK A",bg="black",fg="white",command=partial(room_page_function,1,block),font=("",10,BOLD),activeforeground="white",
              activebackground="blue",pady=20,padx=20)
    block_2=Button(canvas_for_block_page,text="BLOCK B",bg="black",fg="white",command=partial(room_page_function,2,block),activeforeground="white",
              activebackground="blue",pady=20,padx=20)
    block_3=Button(canvas_for_block_page,text="BLOCK C",bg="black",fg="white",command=partial(room_page_function,3,block),activeforeground="white",
             activebackground="blue",pady=20,padx=20)
    block_4=Button(canvas_for_block_page,text="BLOCK D",bg="black",fg="white",command=partial(room_page_function,4,block),activeforeground="white",
             activebackground="blue",pady=20,padx=20)
    block_1.place(x=440,y=230)
    block_2.place(x=570,y=230)
    block_3.place(x=700,y=230)
    block_4.place(x=830,y=230)
    back_button=Button(canvas_for_block_page,text="back",command=partial(back_function,welcome_page,block),padx=30,pady=10)
    back_button.place(x=100,y=700)
    block.mainloop()
#block_page_function()
