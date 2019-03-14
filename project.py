from Tkinter import *

root1=Tk()
Label(root1,text='PYTHON PROJECT',font='times 50',fg='firebrick',bg='lemonchiffon').pack()
Label(root1,text='').pack()
Label(root1,text='LOAN\nMANAGEMENT\nSYSTEM',relief='ridge',font='times 45',fg='steelblue',bd=3,bg='antiquewhite').pack()
Label(root1,text='  \nCREATED BY  -   Sankesh Yadav',font='bold 15',fg='gray1').pack()
Label(root1,text='    ENROLLMENT NO. - 161B195',font='bold 15',fg='gray1').pack()
Label(root1,text='   BATCH     -    B-7',font='bold 15',fg='gray1').pack()

root1.after(5000,root1.destroy)
root1.mainloop()

root=Tk()
root.title("Loan Managing System")
Label(root,text='Welcome To Loan Management System',relief='ridge',font='times 30',bg='violetred4',fg='white').grid(row=0,column=1,columnspan=5)
a=PhotoImage(file='image4.gif')
Label(root,image=a).grid(row=1,column=0,columnspan=100,rowspan=100)
import sqlite3
con=sqlite3.Connection('3.db')
cur=con.cursor()





Label(root,text='\n    Personal Details :',font='bold 20',bg='navajowhite3').grid(row=2,column=1)
Label(root,text='Account No. *',font='bold 10',fg='red',bg='navajowhite2').grid(row=5,column=1)
Label(root,text='Customer Full Name',font='bold 10',bg='navajowhite2').grid(row=6,column=1)
Label(root,text='Address',font='bold 10',bg='navajowhite2').grid(row=6,column=3)
Label(root,text='State',font='bold 10',bg='navajowhite2').grid(row=7,column=1)
Label(root,text='City',font='bold 10',bg='navajowhite2').grid(row=7,column=3)
Label(root,text='Pincode',font='bold 10',bg='navajowhite2').grid(row=8,column=1)
Label(root,text='Occupation',font='bold 10',bg='navajowhite2').grid(row=9,column=1)
Label(root,text='E-mail',font='bold 10',bg='navajowhite2').grid(row=10,column=1)
Label(root,text='Phone No.',font='bold 10',bg='navajowhite2').grid(row=11,column=1)
Label(root,text='Account No. to be searched',font='bold 12',fg='orangered',bg='grey87',relief='ridge',bd=2).grid(row=11,column=3)
Label(root,text='Loan Type :',font='bold 20',bg='lightsteelblue').grid(row=17,column=1)
Label(root,text='Amount of Loan ',font='bold 10',bg='navajowhite2').grid(row=23,column=1)
Label(root,text='Interest Rate :',font='bold 10',bg='navajowhite2').grid(row=24,column=1)
Label(root,text='Monthly Payment :',font='bold 10',bg='navajowhite2').grid(row=26,column=1)
Label(root,text='Aadhar No *',font='bold 10',bg='navajowhite2').grid(row=5,column=3)




e1=Entry(root,width=20,bd=5)
e1.grid(row=5,column=2)
e2=Entry(root,width=20,bd=3)
e2.grid(row=6,column=2)
e3=Entry(root,width=20,bd=3)
e3.grid(row=6,column=4)
e4=Entry(root,width=20,bd=3)
e4.grid(row=7,column=2)
e5=Entry(root,width=20,bd=3)
e5.grid(row=7,column=4)
e6=Entry(root,width=20,bd=3)
e6.grid(row=8,column=2)
e7=Entry(root,width=20,bd=3)
e7.grid(row=9,column=2)
e8=Entry(root,width=20,bd=3)
e8.grid(row=10,column=2)
e9=Entry(root,width=20,bd=3)
e9.grid(row=11,column=2)
e10=Entry(root,width=20,bd=4)
e10.grid(row=11,column=4)
e11=Entry(root,width=20,bd=3)
e11.grid(row=23,column=2)
e12=Entry(root,width=20,bd=3)
e12.grid(row=24,column=2)
e13=Entry(root,width=20,bd=3)
e13.grid(row=26,column=2)
e14=Entry(root,width=20,bd=4)
e14.grid(row=5,column=4)

def insert():
    cur.execute("create table if not exists Loan(Account_no varchar(20) primary key,Aadhar_no number,Customer_Full_name char(20),Address varchar(50),State char(20),City char(10),Pincode number,Occupation char(30),Email varchar(20),Phone_no number,Loan_Type char(20),Amount_of_loan number,Interest_rate number,Monthly_payments number)") 
    cur.execute("insert into Loan values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e14.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),v1.get(),e11.get(),e12.get(),e13.get()))
    con.commit()            
    e1.delete(0,END)
    e2.delete(0,END)            
    e3.delete(0,END)
    e4.delete(0,END)            
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)

    
    

def show():
    show=Tk()
    show.configure(bg='floralwhite')
    show.title("Searched Record")
    Label(show,text='CUSTOMER DETAILS',relief='ridge',font='bold 30',bg='gray90').grid(row=0,column=1)
    Label(show,text='',bg='floralwhite').grid(row=1,column=1)
    Label(show,text='Account_no.',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=5,column=0)
    cur.execute("select Account_no from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=5,column=4)

    Label(show,text='Aadhar No.',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=6,column=0)
    cur.execute("select Aadhar_no from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=6,column=4)


    

    Label(show,text='Customer Name',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=7,column=0)
    cur.execute("select Customer_Full_name from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=7,column=4)

    Label(show,text='Address',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=8,column=0)
    cur.execute("select Address from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=8,column=4)

    Label(show,text='State',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=9,column=0)
    cur.execute("select State from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=9,column=4)

    Label(show,text='City',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=10,column=0)
    cur.execute("select City from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=10,column=4)

    Label(show,text='Pincode',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=11,column=0)
    cur.execute("select Pincode from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=11,column=4)

    Label(show,text='Occupation',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=12,column=0)
    cur.execute("select Occupation from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=12,column=4)

    Label(show,text='E-mail',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=13,column=0)
    cur.execute("select Email from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=13,column=4)

    Label(show,text='Phone No.',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=14,column=0)
    cur.execute("select Phone_no from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=14,column=4)

    Label(show,text='Loan Type',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=15,column=0)
    cur.execute("select Loan_Type from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=15,column=4)
 
    Label(show,text='Amount Of Loan',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=16,column=0)
    cur.execute("select Amount_of_loan from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=16,column=4)

    Label(show,text='Interest Rate',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=17,column=0)
    cur.execute("select Interest_Rate from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=17,column=4)

    Label(show,text='Monthly Payment',relief='ridge',bg='lightsteelblue1',font='bold 15').grid(row=18,column=0)
    cur.execute("select monthly_payments from loan where account_no=?",(e10.get(),))
    Label(show,text=cur.fetchall(),relief='ridge',font='bold 15').grid(row=18,column=4)

    Button(show,text='Exit',command=show.destroy,font='bold 15',bg='gray80').grid(row=30,column=1)
    show.mainloop()
    
                
def showall():
    showall=Tk()
    showall.configure(bg='cornsilk')
    showall.title("ALL RECORDS")
    Label(showall,text='ALL CUSTOMER DETAILS',relief='ridge',font='Arial 30',bg='coral',fg='white').pack()
    Label(showall,text='',bg='cornsilk').pack()
    
    cur.execute("select * from loan")
    a=cur.fetchall()
    for i in a:
        Label(showall,text=i).pack()
    showall.mainloop()

        
    

v1=StringVar(value="0")
r=Radiobutton(root,text='Home Loan',font='bold 15',bg='lightsteelblue1',variable=v1,value='Home Loan')
r.grid(row=18,column=1)
r=Radiobutton(root,text='Personal Loan',font='bold 15',bg='plum1',variable=v1,value='Personal Loan')
r.grid(row=18,column=2)
r=Radiobutton(root,text='Educational Loan',font='bold 15',bg='lightblue',variable=v1,value='Educational Loan')
r.grid(row=18,column=3)
r=Radiobutton(root,text='Vehicle Loan',font='bold 15',bg='skyblue',variable=v1,value='Vehicle Loan')
r.grid(row=18,column=4)
r=Radiobutton(root,text='Agricultural Loan',font='bold 15',bg='yellowgreen',variable=v1,value='Agricultural Loan')
r.grid(row=18,column=5)
r=Radiobutton(root,text='Gold Loan',font='bold 15',bg='gold',variable=v1,value='Gold Loan')
r.grid(row=18,column=6)



def calc():
    calc=Tk()
    calc.configure(bg='ivory')
    calc.title("CALCULATOR")
    Label(calc,text='EMI CALCULATOR',relief='ridge',font='bold 20',bg='gold').grid(row=0,column=1,columnspan=2)
    Label(calc,text='',bg='ivory').grid(row=7,column=1)
    Label(calc,text='Loan amount',relief='ridge',bd=3).grid(row=8,column=1)
    Label(calc,text='Yearly Interest Rate',relief='ridge',bd=3).grid(row=9,column=1)
    Label(calc,text='No. of Monthly Instalments',relief='ridge',bd=3).grid(row=10,column=1)

    
    e1=Entry(calc)
    e1.grid(row=8,column=2)
    e2=Entry(calc)
    e2.grid(row=9,column=2)
    e3=Entry(calc)
    e3.grid(row=10,column=2)

    def calculate():
        P=float(e1.get())
        R1=float(e2.get())
        R=R1/1200
        N=float(e3.get())
        EMI=P*R*((1+R)**(N)/((1+R)**(N)-1))
        Label(calc,text='').grid(row=14,column=1)
        Label(calc,text='The EMI is',font='bold 15').grid(row=15,column=1)
        Label(calc,text=EMI,font='bold 15',relief='ridge',bg='silver').grid(row=15,column=2)

        
    Button(calc,text='Calculate',command=calculate,bd=5).grid(row=13,column=2)
    Button(calc,text='Exit',command=calc.destroy,font='bold 15',bg='gray80').grid(row=20,column=4)


    calc.mainloop()
    
Button(root,text='Calculate EMI',command=calc,font='bold 15',bg='gray80',bd=3).grid(row=25,column=1)

Button(root,text='Insert',command=insert,font='bold 15',bg='gray80').grid(row=30,column=1)
Button(root,text='Showall',command=showall,font='bold 15',bg='gray80').grid(row=30,column=3)
Button(root,text='Show',command=show,font='bold 15',bg='gray80').grid(row=30,column=2)
Button(root,text='Exit',command=root.destroy,font='bold 15',bg='gray80').grid(row=30,column=4)

mainloop()

















