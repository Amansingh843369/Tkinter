from  tkinter import *
from tkinter import font
root=Tk()   
root.title('Google People card')
root.geometry('580x520')
root.resizable(False,False)

frame = Frame(root, bg="white",width=200,height=100,highlightbackground='red')
frame.place(x=150,y=100, relheight=0.5, relwidth=0.5)
Google=Label(root, text="Google people card",bg='#EEEEFF',font="roboto 12 bold").place(x=201,y=10)

a=Label(frame, text="Aman Singh",bg='white').place(x=60,y=10)  

b=Label(frame, text="Developer",bg='white').place(x=60,y=30)

c=Label(frame, text=".",bg='white',font="roboto 10 bold").place(x=117,y=27) 

d=Label(frame, text="Mumbai",bg='white').place(x=125,y=30) 
e=Label(frame, text="I'm  currently focus on python and java  projects.",bg='white').place(x=2,y=60) 
e=Label(frame, text="I'm passionate about my work.",bg='white').place(x=2,y=78) 
d=Label(frame, text="Education:",bg='white',font="roboto 9 bold").place(x=1,y=120) 
d=Label(frame, text="S.N. College",bg='white').place(x=65,y=120) 
d=Label(frame, text="Hometown:",bg='white',font="roboto 9 bold").place(x=1,y=150) 
d=Label(frame, text="Bhayandar,Mumbai",bg='white').place(x=69,y=150) 



pic=PhotoImage(file="profile.png")
bt=Button(frame,image=pic,borderwidth=0,highlightthickness=0,width=60,bg='white',height=60).place(x=0,y=0)

insta_pic=PhotoImage(file="insta.png")
insta=Button(frame,image=insta_pic,borderwidth=0,highlightthickness=0,width=60,bg='white',height=60).place(x=0,y=180)

face_pic=PhotoImage(file="face.png")
face=Button(frame,image=face_pic,borderwidth=0,highlightthickness=0,width=60,bg='white',height=60).place(x=50,y=180)

pinterest_pic=PhotoImage(file="pin.png")
pinterest=Button(frame,image=pinterest_pic,borderwidth=0,highlightthickness=0,width=60,bg='white',height=60).place(x=100,y=180)

source=Label(frame, text="Source: Aman Singh",bg='white',font="roboto 9 ").place(x=10,y=235) 


backg_pic=PhotoImage(file="backg.png")
img=Label(root,image=backg_pic,width=550,height=200).place(x=207,y=362)

root.mainloop()



# import  tkinter as tk
# from tkinter import *

# def make_window():
#     global a
#     root.withdraw()
#     a=tk.Toplevel()
#     a.title('Student ')
#     a.geometry('580x520')

# root=tk.Tk()   
# root.title('Hello users')
# root.geometry('580x520')
# pic=tk.PhotoImage(file="secure.png")
# bt=tk.Button(root,image=pic,borderwidth=0,highlightthickness=0,command=make_window).place(x=62,y=205)
# # bt=tk.Label(root,image=pic,borderwidth=0,highlightthickness=0).place(x=62,y=205)
# root.mainloop()

# import  pyautogui as p
# a=p.typewrite("a")
# p.hotkey('right','enter')
# print(a)a