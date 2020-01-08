from tkinter import *
from sqlite3 import *
conn=connect("students.db")
cur=conn.cursor()





def register(rollno,name,phno,email):
    rollno=rollno.get()
    name=name.get()
    phno=phno.get()
    email=email.get()
    create='''create table if not exists ece1(rollno varchar(20),name varchar(20),phno varchar(20),
                email varchar(20))'''
    cur.execute(create)
    conn.commit()
    insert="insert into ece1(rollno,name,phno,email)values(?,?,?,?)"
    values=[rollno,name,phno,email]
    #print(values)
    cur.execute(insert,values)
    T1.delete(0,END)
    T2.delete(0,END)
    T3.delete(0,END)
    T4.delete(0,END)

def view():
    view="select * from ece1"
    cur.execute(view)
    data=cur.fetchall()
    for i in data:
        for r in i:
            print(r,end=" ")
        print()
    


    
root=Tk()
root.title("My Project")
root.geometry("500x500")


L1=Label(root,text="Rollno")
L1.grid(row=0,column=0)
roll_text=StringVar()
T1=Entry(root,textvariable=roll_text)
T1.grid(row=0,column=1)


L2=Label(root,text="name")
L2.grid(row=0,column=2)
name_text=StringVar()
T2=Entry(root,textvariable=name_text)
T2.grid(row=0,column=3)


L3=Label(root,text="phno")
L3.grid(row=1,column=0)
phno_text=StringVar()
T3=Entry(root,textvariable=phno_text)
T3.grid(row=1,column=1)

L4=Label(root,text="email")
L4.grid(row=1,column=2)
email_text=StringVar()
T4=Entry(root,textvariable=email_text)
T4.grid(row=1,column=3)

b1=Button(root,text="Submit",command=lambda: register(roll_text,name_text,phno_text,email_text))
b1.grid(row=2,column=0,columnspan=4,rowspan=4)

b2=Button(root,text="view Data",command=view)
b2.grid(row=2,column=4,columnspan=4)

root.mainloop()
