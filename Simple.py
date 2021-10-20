# Import Module
from tkinter import * 
from PIL import Image, ImageTk
import tkinter as tk
import emoji

# Create Tkinter Object
root = Tk()
root.geometry("400x515")
root.resizable(width=False,height=TRUE)


# Read the Image
image = Image.open("simple.jpg")

# Resize the image using resize() method
resize_image = image.resize((400,200))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()
def get():
    d= int(e.get())  #principal
    x=int(e1.get())   #rate
    y=int(e2.get())   # year 
    #z=int(e3.get())  # S.I
    S=d*x*y//100
    print(S)
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,S)
    t1.config(state='normal')
def principal_get():
    z=int(e3.get())
    x=int(e1.get())   #rate
    y=int(e2.get())
    P=100*z//x*y   #if P=2000,r=5,y=6 ,S.I=600
    print(P)
def Rate_get():
    z=int(e3.get()) 
    d=int(e.get())  #principal
    y=int(e2.get()) 
    Rate=z*100//d*y
    print(Rate)
def time_get():
    z=int(e3.get())     # S.I
    d=int(e.get())  #principal
    x=int(e1.get())   #rate
    Tim=d*x
    bim=100*z
    print(bim//Tim)
i=IntVar()
l=IntVar()
m=IntVar()
L=Label(root,text="Principle :",fg='red',font=('Arial',12,"bold"))
l1=Label(root,text="Rate :",fg='red',font=('Arial',12,"bold"))
l2=Label(root,text="Year :",fg='red',font=('Arial',12,"bold"))
l3=Label(root,text="S.I :",fg='red',font=('Arial',12,"bold"))

e=Entry(root,width=5)
e1=Entry(root,width=5)
e2=Entry(root,width=5)
e3=Entry(root,width=5)
L.place(x=100,y=220)
l1.place(x=100,y=250)
l2.place(x=100,y=280)
l3.place(x=100,y=311)

e.place(x=190,y=224)
e1.place(x=190,y=252)
e2.place(x=190,y=282)
e3.place(x=190,y=313)
l3 = Label(root,text="The Calculated S.I is: ",font=('Arial',12,"bold"),fg="red")
l3.place(x=50,y=370)
t1=Text(root,width=5,height=0,state="disabled",insertontime=1000)
t1.place(x=220,y=370)
b1=Button(root,text="Calculate S.I ",font=("Arial",13),command=get)
b1.place(x=200,y=400)

b2=Button(root,text="Calculate Principal(P)",font=("Arial",13),command=principal_get).place(x=20,y=400)

b3=Button(root,text="Calculate Rate(R)",font=("Arial",13),command=Rate_get).place(x=20,y=440)

b4=Button(root,text="Calculate Time(T)",font=("Arial",13),command=time_get).place(x=200,y=440)
b2=tk.Button(root,text="Exit Application!",font=("Arial",13),command=root.destroy).place(x=100,y=480)

p=emoji.emojize(":grinning_face_with_big_eyes:")



button = Button(root , text = p , font = "arial 50",width=0,height=0 ,relief=FLAT)
button.place(x=280,y=210)


# Execute Tkinter
root.mainloop()
