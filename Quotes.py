# Import Module
from tkinter import *
from tkinter import font 
from PIL import Image, ImageTk
import tkinter as tk
import time
from datetime import date


# Create Tkinter Object
root = Tk()
root.geometry("330x380")
root.iconbitmap('pp.ico')
root.title("pro")
#root.attributes('-alpha',0.5)

#l2 = tk.Label(window,font=("Arial",12),text="Enter your birthday which includes the day-month-year.",fg="black",bg="#F7DC6F")

l = Label(root, text = "Quote of the Day",bg='grey',fg="red")
l.config(font =("Courier", 14))


T = Text(root, height = 5, width = 52,font=('times', 17, 'normal'),relief='flat',selectbackground='red',cursor='circle')
  

  
Fact = """ "Always do your best. What 
you plant now, you will harvest 
later." \n                         \t --Albert Eistein """

T.insert(tk.END, Fact)
T.config(state="disabled")

l.pack(side='top',expand=False,fill='both',padx=10,pady=10)#by default side  is  top
T.pack()  

def Next_get():
    print("Next")
    win = Tk()
    win.title("New Window")
    win.geometry("400x200")
    menubar1 = Menu(win, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
    file1 = Menu(menubar1, tearoff=0, background='#ffcc99', foreground='black')  
    file1.add_command(label="huhbyujgg")  
    file1.add_command(label="Bookmark",command=book_mark)  
    file1.add_command(label="Save")  
    file1.add_command(label="Save as")    
    file1.add_separator()  
    file1.add_command(label="Exit", command=win.quit)
    win.config(menu=menubar1)
    l = Label(win, text = "Quote of the Day",bg='grey',fg="red")
    l.config(font =("Courier", 14))
    pre = Text(win, height = 5, width = 52,font=('times', 17, 'normal'),relief='flat',selectbackground='red',cursor='circle') 
    Fact = """ "If you really want to be sucessfully,stop \t   worrying about what you can get and
    start focusing on what you can do." \n                         \t -- Sandeep Maheshwari """
    pre.insert(tk.END, Fact)
    pre.config(state="disabled")

    l.pack(side='top',expand=False,fill='both',padx=10,pady=10)#by default side  is  top
    pre.pack()  


def Prev_get():
    root = Tk()
    root.geometry("330x515")

    l = Label(root, text = "Quote of the Day")
    T = Text(root, height = 5, width = 52,fg='green',font=('times', 17, 'normal'),relief='flat',selectbackground='red',cursor='circle')
    Fact = """ "Always do your best. What 
    you plant now, you will harvest 
    later." \n                         \t --Albert Eistein """

    T.insert(tk.END, Fact)
    T.config(state="disabled")

    l.pack()
    T.pack() 

def book_mark():
    top = Toplevel()
    top.geometry("340x300")
    top.title("toplevel")
    l1 = Label(top, text = "-----------Your saved Bookmark----------------",font=('times', 12, 'normal'),fg='red')
    l1.pack(pady=10)
    a=IntVar()
    today = date.today()
    a.set(today.strftime("%d/%m/%Y"))
    l2 = Label(top, text = "Date",textvariable=a)
    l2.pack()
    k = Text(top, height = 5, width = 52,font=('times', 17, 'normal'),relief='flat',selectbackground='Black')
    Fact = """   "Always do your best. What 
    you plant now, you will harvest 
    later." \n                         \t --Albert Eistein """
    k.insert(tk.END, Fact)
    k.config(state="disabled")
    # e3=Entry(root,width=5)
    # e3.place(x=190,y=313)
    k.pack()

photo = PhotoImage(file = "index.png")
# Resizing image to fit on button
photoimage = photo.subsample(2, 2)
button = Button(root , text = "", font = "arial 14",width=0,height=0 ,image = photoimage,compound = LEFT,relief=FLAT,command=Next_get)
button.place(x=150,y=190)

img = Image.open("gra.png")
img = img.resize((102 ,102))
tkimage = ImageTk.PhotoImage(img)
button1 = Button(root , text = "", font = "arial 14",width=100,height=100 ,image = tkimage,compound = LEFT,relief=FLAT,command=Prev_get)
button1.place(x=30,y=190)



# root.iconify() 
# root.deiconify() 
#root.withdraw()

menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
file = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')  
file.add_command(label="New")  
file.add_command(label="Bookmark",command=book_mark)  
file.add_command(label="Save")  
file.add_command(label="Save as")    
file.add_separator()  
file.add_command(label="Exit", command=root.quit)  
menubar.add_cascade(label="File", menu=file)  

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
    
root.config(menu=menubar)








root.mainloop()


