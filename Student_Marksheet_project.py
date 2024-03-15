import tkinter as tk
from tkinter import *
from typing import Optional,Any
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox



def clear():
	username.delete(0,END)
	password.delete(0,END)
def close():
	master.destroy()

def login():
        if username.get()=="Rutuja" and password.get()=="Rutu@123":
                messagebox.showinfo("Success" , "Successfully Login")
                close()
                marksheet()
        else:
                messagebox.showerror("Error","Enter User Name And Password")


master = tk.Tk()
master.geometry("900x900")
master.title("Admin Panel")
load = Image.open('board.jpg')
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=0, y=0)



username = StringVar()
password = StringVar()

l1 = tk.Label(master,text="Username",font=("Times New Roman", 18), fg="white", bg="black")
l1.place(x=280,y=215)


username = Entry(master, width=150 , textvariable = username,font=("Times New Roman", 16), fg="black", bg="white")
username.focus()
username.place(x=400,y=220,width=150,height=20)

l2 = tk.Label(master,text = "Password",font=("Times New Roman", 18), fg="white", bg="black")
l2.place(x=280,y=265)


password = Entry(master, width=100, show="*" ,textvariable = password,font=("Times New Roman", 16), fg="black", bg="white")
password.place(x=400,y=270,width=150,height=20)



bt1 =tk.Button(master,text = 'Login',font=("Times New Roman", 14), bg = 'lightblue', command = login)
bt1.place(x=270, y=350, width = 120,height= 50)

bt1 =tk.Button(master,text = 'Clear',font=("Times New Roman", 14), bg = 'Pink', command = clear)
bt1.place(x=450, y=350, width = 120,height= 50)



def marksheet():
        # creating a new tkinter window
        master = tk.Tk()

        master.title("STUDENT MARKSHEET USING GUI")
        master.geometry("900x600")

        load = Image.open('board.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=0, y=0)


        def submit_fc():
                Name = e1.get()
                Seat_No = e2.get()
                PRN_No = e3.get()

                Internal1 = int(e4.get())
                Theory1 = int(e44.get())
                Computer_Fundamental = Internal1 + Theory1

                Internal2 = int(e5.get())
                Theory2 = int(e55.get())
                Digital_Electronics = Internal2 + Theory2

                Internal3 = int(e6.get())
                Theory3 = int(e66.get())
                Data_Structure = Internal3 + Theory3

                Internal4 = int(e7.get())
                Theory4 = int(e77.get())
                Microprocessor = Internal4 + Theory4

                Internal5 = int(e8.get())
                Theory5 = int(e88.get())
                Programming_C = Internal5 + Theory5

                Internal6 = int(e9.get())
                Theory6 = int(e99.get())
                Communication_Skill = Internal6 + Theory6

                total = Computer_Fundamental + Digital_Electronics + Data_Structure + Microprocessor + Programming_C + Communication_Skill

                percentage = round(total / 6, 2)


                db = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Rutuja#1510',
                    database='student_marksheet'
                )
                #print(db)
                c1 = db.cursor()

                syntax = "INSERT INTO Marksheet_Records(Name,Seat_No,PRN_No,internal1,theory1,internal2,Theory2,internal3,Theory3,internal4,Theory4,internal5,Theory5,internal6,Theory6,total,percentage)" \
                 "VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s)"

                data = (Name, Seat_No, PRN_No, Internal1, Theory1, Internal2, Theory2, Internal3, Theory3, Internal4, Theory4, Internal5 ,Theory5, Internal6, Theory6, total, percentage)
                c1.execute(syntax, data)

                db.commit()  # to make the changes happened
                db.close()
                messagebox.showinfo("Message", "Record save successfully")

                e1.delete(0, 'end')
                e2.delete(0, 'end')
                e3.delete(0, 'end')
                e4.delete(0, 'end')
                e44.delete(0, 'end')
                e5.delete(0, 'end')
                e55.delete(0, 'end')
                e6.delete(0, 'end')
                e66.delete(0, 'end')
                e7.delete(0, 'end')
                e77.delete(0, 'end')
                e8.delete(0, 'end')
                e88.delete(0, 'end')
                e9.delete(0, 'end')
                e99.delete(0, 'end')

                e1.focus()


        e1 = tk.Entry(master)
        e2 = tk.Entry(master)
        e3 = tk.Entry(master)

        e4 = tk.Entry(master)
        e44 = tk.Entry(master)

        e5 = tk.Entry(master)
        e55 = tk.Entry(master)

        e6 = tk.Entry(master)
        e66 = tk.Entry(master)

        e7 = tk.Entry(master)
        e77 = tk.Entry(master)

        e8 = tk.Entry(master)
        e88 = tk.Entry(master)

        e9 = tk.Entry(master)
        e99 = tk.Entry(master)

        tk.Label(master, text="Dr.Babasaheb Ambedkar Marathwada Univeristy,\nChhatrapati Sambhajinagar", font=("Times New Roman", 22,"bold"),
                    fg ="LIGHT BLUE", bg="black").place(x=150, y=80)
        load = Image.open('DR.BAMU LOGO.jfif')
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image = render
        img.place(x=70, y=70)

        tk.Label(master, text="Name", font=("Times New Roman", 16), fg="white", bg="black").place (x=80, y=180)
        e1 = tk.Entry(master, width=15)
        e1.place(x=160, y=180)


        tk.Label(master, text="Seat No.", font=("Times New Roman", 16), fg="white", bg="black").place(x=80, y=220)
        e2 = tk.Entry(master, width=15)
        e2.place(x=160, y=220)

            # label for roll Number
        tk.Label(master, text="PRN No.", font=("Times New Roman", 16), fg="white", bg="black").place (x=600, y=190)
        e3 = tk.Entry(master, width=15)
        e3.place(x=690, y=190)

        # labels for serial numbers
        tk.Label(master, text="Sr.No", font=("Times New Roman", 16),fg="light blue", bg="black").place (x=100, y=280)
        tk.Label(master, text="1", font=("Times New Roman", 14), fg="white", bg="black").place(x=120, y=320)
        tk.Label(master, text="2", font=("Times New Roman", 14), fg="white", bg="black").place(x=120, y=345)
        tk.Label(master, text="3", font=("Times New Roman", 14), fg="white", bg="black").place(x=120, y=370)
        tk.Label(master, text="4", font=("Times New Roman", 14), fg="white", bg="black").place(x=120, y=395)
        tk.Label(master, text="5", font=("Times New Roman", 14), fg="white", bg="black").place (x=120, y=420)
        tk.Label(master, text="6", font=("Times New Roman", 14), fg="white", bg="black").place (x=120, y=445)


        # labels for subject codes
        tk.Label(master, text="Subject", font=("Times New Roman", 16), fg="light blue", bg="black" ).place(x=240, y=280)
        tk.Label(master, text="Internal Marks", font=("Times New Roman", 16), fg="light blue", bg="black").place ( x=400, y=280 )
        tk.Label(master, text="Theory Marks", font=("Times New Roman", 16), fg="light blue", bg="black").place ( x=560, y=280 )
        tk.Label(master, text="Total", font=("Times New Roman", 16), fg="light blue", bg="black").place(x=720, y=280)
        tk.Label(master, text="Computer Fundamental", font=("Times New Roman", 14,), fg="white", bg="black").place ( x=200, y=320 )
        e4 = tk.Entry(master, width="14")
        e4.place(x=420, y=320)
        e44 = tk.Entry(master, width="14")
        e44.place(x=580, y=320)

        tk.Label(master, text="Digital Electronics", font=("Times New Roman", 14), fg="white", bg="black").place(x=200,y=345)

        e5 = tk.Entry(master,width="14")
        e5.place(x=420, y=345)
        e55 = tk.Entry(master, width="14")
        e55.place(x=580, y=345)

        tk.Label(master, text="Data structure", font=("Times New Roman", 14), fg="white", bg="black").place(x=200, y=370)
        e6 = tk.Entry(master, width="14")
        e6.place ( x=420, y=370 )
        e66 = tk.Entry(master, width="14")
        e66.place(x=580, y=370)

        tk.Label(master, text="Microprocessor", font=("Times New Roman", 14), fg="white", bg="black").place(x=200, y=395)
        e7 = tk.Entry(master, width="14")
        e7.place(x=420, y=395)
        e77 = tk.Entry(master, width="14")
        e77.place(x=580, y=395)

        tk.Label(master, text="Programming C", font=("Times New Roman", 14), fg="white", bg="black").place(x=200, y=420)
        e8 = tk.Entry(master, width="14")
        e8.place(x=420, y=420)
        e88 = tk.Entry(master, width="14")
        e88.place(x=580, y=420)

        tk.Label(master, text="Communication Skill", font=("Times New Roman", 14), fg="white", bg="black").place(x=200, y=445)

        e9 = tk.Entry(master, width="14")
        e9.place(x=420, y=445)
        e99 = tk.Entry(master, width="14")
        e99.place(x=580, y=445)


        def display():
                tot = 0
                c1 = int (e4.get())
                c2 = int ( e44.get () )
                Computer_Fundamental = c1 + c2
                t1=tk.Label(master, text=Computer_Fundamental,font=("Times New Roman", 14), fg="white", bg="black")
                t1.place(x=740, y=320)
                tot += Computer_Fundamental

                DE1 = int(e5.get())
                DE2 = int(e55.get())
                Digital_Electronics = DE1 + DE2
                t2 = tk.Label(master, text=Digital_Electronics, font=("Times New Roman", 14), fg="white", bg="black")
                t2.place(x=740, y=345)
                tot += Digital_Electronics

                DS1 = int(e6.get())
                DS2 = int(e66.get())
                Data_Structure = DS1 + DS2
                t3 = tk.Label(master, text=Data_Structure, font=("Times New Roman", 14), fg="white", bg="black")
                t3.place(x=740, y=370)
                tot += Data_Structure

                M1 = int(e7.get())
                M2 = int(e77.get())
                Microprocessor = M1 + M2
                t4 = tk.Label(master, text=Microprocessor, font=("Times New Roman", 14), fg="white", bg="black")
                t4.place(x=740, y=395)
                tot += Microprocessor

                P1 = int(e8.get())
                P2 = int(e88.get())
                Programming_C = P1 + P2
                t5=tk.Label(master, text=Programming_C, font=("Times New Roman", 14), fg="white", bg="black")
                t5.place(x=740, y=420)
                tot += Programming_C

                CS1 = int(e9.get())
                CS2 = int (e99.get())
                Communication_Skill = CS1 + CS2
                t6 = tk.Label(master, text=Communication_Skill, font=("Times New Roman", 14), fg="white", bg="black" )
                t6.place(x=740, y=445)
                tot += Communication_Skill

                # to display total Mark
                tk.Label(master, text=str(tot) + "/600", font=("Times New Roman", 14), fg="white", bg="black").place(x=720, y=470)

                # to display Percentage
                percentage = round ( tot / 6, 2 )
                tk.Label(master, text=str(percentage) + "%", font=("Times New Roman", 14), fg="white", bg="black").place(x=720, y=495)


                if (percentage <= 100) and (percentage >= 90):
                    gr = "O"
                    O=tk.Label( master, text=gr, font=("Times New Roman", 14),fg="white",bg="black" )
                    O.place( x=740, y=520 )

                elif(percentage < 90) and (percentage >= 75):
                    gr = "A"
                    A=tk.Label( master, text=gr,font=("Times New Roman", 14),fg="white", bg="black" )
                    A.place(x=740, y=520 )

                elif(percentage < 75) and (percentage >= 55):
                    gr = "B"
                    B=tk.Label ( master, text=gr,font=("Times New Roman", 14),fg="white", bg="black")
                    B.place ( x=740, y=520 )

                elif(percentage < 55) and (percentage >= 35):
                    gr = "C"
                    C=tk.Label ( master, text=gr,font=("Times New Roman", 14),fg="white", bg="black" )
                    C.place ( x=740, y=520 )

                elif(percentage < 35):
                    gr = "F"
                    F=tk.Label ( master, text=gr,font=("Times New Roman", 14),fg="white", bg="black" )
                    F.place ( x=740, y=520 )



        def show():
                my_w = tk.Tk()
                my_w.title("RECORDS")
                my_w.geometry("1400x400")
                my_connect = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Rutuja#1510",
                    database="student_marksheet"
                )
                my_conn = my_connect.cursor()

                e = Label(my_w, width=10, text='ID', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid ( row=0, column=0)
                e = Label(my_w, width=10, text='Student Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=1)
                e = Label(my_w, width=12, text='Seat Number', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=2)
                e = Label(my_w, width=12, text='PRN_No', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=3)

                e = Label(my_w, width=18, text='Computer Fundamental', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=4, columnspan=2)
                e = Label(my_w, width=5, text='CA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=4)
                e = Label(my_w, width=5, text='UA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=5)

                e = Label(my_w, width=18, text='Digital Electronics', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=6, columnspan=2)
                e = Label(my_w, width=5, text='CA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=6)
                e = Label(my_w, width=5, text='UA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=7)

                e = Label(my_w, width=18, text='Data structure', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=8, columnspan=2)
                e = Label(my_w, width=5, text='CA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=8)
                e = Label(my_w, width=5, text='UA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=9)

                e = Label(my_w, width=18, text='Microprocessor', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=10, columnspan=2)
                e = Label(my_w, width=5, text='CA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=10)
                e = Label(my_w, width=5, text='UA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=11)

                e = Label(my_w, width=18, text='Programming C', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=12, columnspan=2)
                e = Label (my_w, width=5, text='CA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=12)
                e = Label(my_w, width=5, text='UA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=13)

                e = Label(my_w, width=18, text='Communication Skill', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=14, columnspan=2)
                e = Label(my_w, width=5, text='CA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=14)
                e = Label(my_w, width=5, text='UA', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=15)

                e = Label ( my_w, width=18, text='total and percentage ', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=0, column=16, columnspan=2)
                e = Label(my_w, width=8, text='Total', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=16)
                e = Label(my_w, width=10, text='Percentage', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                e.grid(row=1, column=17)


                #my_conn = my_connect.cursor ()
                my_conn.execute("SELECT * FROM Marksheet_Records limit 0,10")
                i: int = 2
                for Marksheet_Records in my_conn:
                    for j in range(len(Marksheet_Records)):
                        e = Label(my_w,width=10, fg='blue',text=Marksheet_Records[j],relief='ridge', anchor="w")
                        e.grid(row=i, column=j)
                    i = i + 1
                my_w.mainloop()



        def clear():
                e1.delete(0, 'end')
                e2.delete(0, 'end')
                e3.delete(0, 'end')
                e4.delete(0, 'end')
                e44.delete(0, 'end')
                e5.delete(0, 'end')
                e55.delete(0, 'end')
                e6.delete(0, 'end')
                e66.delete(0, 'end')
                e7.delete(0, 'end')
                e77.delete(0, 'end')
                e8.delete(0, 'end')
                e88.delete(0, 'end')
                e9.delete(0, 'end')
                e99.delete(0, 'end')

                e1.focus()

        # button to display all the calculated credit scores and sgpa
        button1 = tk.Button(master, text="Submit", font=("Times New Roman", 14), bg="light blue", command=display)
        button1.place(x=140, y=520, width=90)

        button1 = tk.Button(master, text="Save", font=("Times New Roman", 14), bg="yellow", command=submit_fc)
        button1.place(x=240, y=520, width=90)

        button1 = tk.Button(master, text="Show", font=("Times New Roman", 14), bg="light blue", command=show)
        button1.place(x=340, y=520, width=90)

        button1 = tk.Button(master, text="Clear", font=("Times New Roman", 14), bg="yellow", command=clear)
        button1.place(x=440, y=520, width=90)


        tk.Label(master, text="Total Marks", font=("Times New Roman", 14), fg="white", bg="black").place(x=580, y=470)
        tk.Label(master, text="Percentage", font=("Times New Roman", 14), fg="white", bg="black").place (x=580, y=495)
        tk.Label(master, text="Grade", font=("Times New Roman", 14), fg="white", bg="black").place(x=580, y=520)

master.mainloop()


