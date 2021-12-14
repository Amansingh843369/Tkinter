import datetime
from os import pipe
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from tkinter .filedialog import asksaveasfile
from ttkthemes import ThemedStyle


# Creating the universal font variables
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

# Connecting to the Database where all information will be stored
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()




# Initializing the GUI window
main = Tk()
main.title('Aman School Management System')
main.geometry('1000x700')
main.resizable(0, 0)

# Creating the background and foreground color variables
l = 'MediumSpringGreen' # bg color for the left_frame
c = 'PaleGreen' # bg color for the center_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()

# Placing the components in the main window
Label(main, text="SCHOOL MANAGEMENT SYSTEM", font=headlabelfont, bg='black',fg='white').pack(side=TOP, fill=X)


def reset_form():
    global tree
    tree.delete(*tree.get_children())

    


def display_records():
    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM SCHOOL_MANAGEMENT')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)


def add_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar

    name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    DOB = dob.get_date()
    stream = stream_strvar.get()

    if not name or not email or not contact or not gender or not DOB or not stream:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            connector.execute(
            'INSERT INTO SCHOOL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)', (name, email, contact, gender, DOB, stream)
            )
            connector.commit()
            mb.showinfo('Record added', f"Record of {name} was successfully added")
      
            display_records()
        except:
            mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')


def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        tree.delete(current_item)

        connector.execute('DELETE FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
        connector.commit()

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        display_records()


def view_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))

    name_strvar.set(selection[1]); email_strvar.set(selection[2])
    contact_strvar.set(selection[3]); gender_strvar.set(selection[4])
    dob.set_date(date); stream_strvar.set(selection[6])

def reset_fields():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar

    for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
        exec(f"{i}.set('')")
    dob.set_date(datetime.datetime.now().date())


def reset_form():
    global tree
    tree.delete(*tree.get_children())

    reset_fields()

def sql_query():
    import sqlite3
    my_child=Toplevel(main)
    my_child.title("I am new window5")
    my_child.geometry("500x500")
    my_child.resizable(False,True)

    conn=sqlite3.connect('opa.db')
    # conn.execute(""" CREATE TABLE AMAN(
    #      ADMIN_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #      USER TEXT NOT NULL,
    #      PASS TEXT NOT NULL
    # )""")
    print( " Table AMAN  CREATE SUCCESS")
    # conn.execute("INSERT INTO AMAN(USER,PASS) VALUES('suraj','86667')")
    # conn.execute("INSERT INTO AMAN(USER,PASS) VALUES('rahul','park667')")
    conn.commit()
    print( " Record inserted succesfully ")
    cur=conn.execute("SELECT * from AMAN")
    for row in cur:
           print("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
    conn.close()       
   
    # amu=IntVar()
    amu=sqlite3.connect('opa.db')
    poil=amu.execute("SELECT * from AMAN")
    for row in poil:
           print("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
         
           l=Label(my_child,width=59,height=14,bg='wheat',text=row)
           l.place(x=20,y=30)
    amu.close()
    

    

    
   
   



left_frame = Frame(main, bg=l)
left_frame.place(x=0, y=460, relheight=0.4, relwidth=1)

center_frame = Frame(main)
center_frame.place(x=798, y=50, relheight=0.5, relwidth=0.2)

right_frame = Frame(main, bg="green")
right_frame.place( x=10,y=34, relheight=0.6, relwidth=0.8)


Label(left_frame, text="Name :", font=labelfont, bg=l).place(x=0,y=10)
Label(left_frame, text="Contact Number :", font=labelfont, bg=l).place(x=250,y=10)
Label(left_frame, text="Email Address :", font=labelfont, bg=l).place(x=580,y=10)
Label(left_frame, text="Gender :", font=labelfont, bg=l).place(x=0,y=50)
Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=l).place(x=200,y=50)
Label(left_frame, text="Stream :", font=labelfont, bg=l).place(x=600,y=50)

Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=70,y=10)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=400,y=10)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=710,y=10)
Entry(left_frame, width=19, textvariable=stream_strvar, font=entryfont).place(x=670,y=50)

OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=90,y=50)

dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=400,y=50)

Button(left_frame, text='Submit and Add Record', font=labelfont,command=add_record, width=18).place(x=600,y=200)

Button(center_frame, text='Run Query', font=labelfont, command=sql_query, width=15).place(x=20,y=40)
Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(x=20,y=80)
Button(center_frame, text='View Record', font=labelfont, command=view_record, width=15).place(x=20,y=120)
Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(x=20,y=160)
Button(center_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(x=20,y=200)

Label(right_frame, text='Students Records', font=headlabelfont,bg='green', fg='white').place(x=300,y=2)

tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=('Student ID', "Name", "Email Address", "Contact Number", "Gender", "Date of Birth", "Stream"))

X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)

tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)
tree.column('#7', width=150, stretch=NO)

tree.place(y=30, relwidth=1, relheight=0.9, relx=0)


Button(center_frame, text='Save file', font=labelfont, command=lambda:save(), width=15).place(x=20,y=240)
def save():

    #main.config(bg="black")
    # center_frame.config(bg='black')
    # left_frame.config(bg="black")
    #right_frame.config(bg='red')
    files=[('Text document', '* .text')]
    file=asksaveasfile(filetypes=files)
    q="SELECT * FROM SCHOOL_MANAGEMENT"
    my=connector.execute(q)
    fetc=my.fetchall()
    file.write(str(fetc))
    file.close()
    for row in fetc:
       print(row[0],row[1],row[2],row[3],row[4]) 
   

display_records()

# Finalizing the GUI window
main.update()
# def make_window():
#     global a
#     main.withdraw()
#     a=Toplevel()
#     a.title('Student')
#     a.geometry('580x520')
#     photo_top=PhotoImage(file="secure.png")



# pic=PhotoImage(file="secure.png")
# bt=Button(main,image=pic,borderwidth=0,highlightthickness=0,command=make_window).place(x=62,y=205)

main.mainloop()



