import mysql.connector as c
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter import Tk, ttk
con = c.connect(user = 'root', host = "localhost", passwd = "admin")
cur = con.cursor()
cur.execute("create database  if not exists air_quality")
con.commit()
cur.execute("use air_quality")
cur.execute("CREATE TABLE  if not exists air (date_01 varchar(250),pm2_5 INT,no2 INT,so2 INT)")
con.commit()
ls_pm2_5 = ["100-gud","351-430-warning","430+ hazardous"] #for reference
ls_no2 = ["80-gud","281-400- warning","400+ hazardous"]
ls_so2 = ["80-gud","801-1600-warning","1600+ hazardous"]


def add_new_record():
	window2 =Tk()
	window2.geometry("900x500")
	l1 = tk.Label(window2,text = "Date (YYYY-MM-DD)")
	l1.grid(row =1,column=1)
	e1 =tk.Entry(window2,width =30)
	e1.grid(row =1,column=3)
	l2 =tk.Label(window2,text ="PM2.5",width = 30, font ="bold")
	l2.grid(row=2,column=1)
	e2 = tk.Entry(window2)
	e2.grid(row = 2, column = 3)
	l3 =tk.Label(window2,text ="NO2",width = 30, font ="bold")
	l3.grid(row=3,column=1)
	e3 = tk.Entry(window2)
	e3.grid(row = 3, column = 3)
	l4 =tk.Label(window2,text ="SO2",width = 30, font ="bold")
	l4.grid(row=4,column=1)
	e4 = tk.Entry(window2)
	e4.grid(row = 4, column = 3)
	b1 = tk.Button(window2, text = "Proceed", width = 30, command = lambda:add_record_true(e1,e2,e3,e4))
	b1.grid(row =5, column =2)
	
	
	
	
def add_record_true(e1,e2,e3,e4):
        try:
                
                dt = e1.get()
                pm2_5 = e2.get()
                no2 = e3.get()
                so2 = e4.get()
                cmd = "insert into air values('{}',{},{},{})".format(dt,pm2_5,no2,so2)
                cur.execute(cmd)
                con.commit()
                messagebox.showinfo("Success","Record Updated sucessfully")
		
        except Exception as e:
                messagebox.showerror("Error","We ran down some errorr -->  " + str(e) + " please try again...")
def show_records():
        window3 = Tk()
        window3.geometry("700x400")
        l1 = tk.Label(window3, text = "Date (YYYY-MM-DD)", width =30, font = "bold")
        l1.grid(row =1, column =1)
        e1 = tk.Entry(window3, width =30)
        e1.grid(row =1 , column = 2)
        b1 = tk.Button(window3, text = "Check By Date", width = 30 ,command = lambda: check_by_date(e1))
        b1. grid(row =2 , column = 2)
        b2 = tk.Button(window3, text  = "List all", width = 30 ,command = lambda:check_all())
        b2.grid(row = 3, column =2)
        window3.mainloop()

def check_by_date(e1):
        dt = e1.get()
        window4 = Tk()
        window4.geometry("900x600")
        tree = ttk.Treeview(window4, columns = ("c1","c2","c3","c4"), show= "headings", height = 20)
        tree.column("#1", anchor = "center")
        tree.heading("#1", text ="Date")
        tree.column("#2", anchor = "center")
        tree.heading("#2", text ="PM 2.5")
        tree.column("#3", anchor = "center")
        tree.heading("#3", text ="NO2")
        tree.column("#4", anchor = "center")
        tree.heading("#4", text ="SO2")
        cmd = "select * from air where date_01 = '{}'".format(dt)
        cur.execute(cmd)
        data = cur.fetchall()
        c =1
        for i in data:
                pm2_5 = i[1]
                no2 = i[2]
                so2 = i[3]
                tree.insert('','end', text = c, values = (dt,pm2_5,no2,so2))
                c+=1
        tree.grid(row =1, column =1)
        
        if pm2_5> 351 and pm2_5 <430:
                messagebox.showerror("WARNING","PM2.5 is in danger levels CAUTION!")
        elif pm2_5>=430:
                messagebox.showerror("WARNING","PM2.5 is in HAZARDOUS level EVACUATE!")

        if no2 >281 and no2< 400:
                messagebox.showerror("WARNING","NO2 is in danger levels CAUTION!")
        elif no2>=400:
                messagebox.showerror("WARNING","NO2 is in HAZARDOUS level EVACUATE!")

        if so2>801 and so2<1600:
                messagebox.showerror("WARNING","SO2 is in danger levels CAUTION!")

        elif so2>=1600:
                messagebox.showerror("WARNING","NO2 is in HAZARDOUS level EVACUATE!")
        window4.mainloop()
def check_all():
        window5 = Tk()
        window5.geometry("900x600")
        tree = ttk.Treeview(window5, columns = ("c1","c2","c3","c4"), show= "headings", height = 20)
        tree.column("#1", anchor = "center")
        tree.heading("#1", text ="Date")
        tree.column("#2", anchor = "center")
        tree.heading("#2", text ="PM 2.5")
        tree.column("#3", anchor = "center")
        tree.heading("#3", text ="NO2")
        tree.column("#4", anchor = "center")
        tree.heading("#4", text ="SO2")
        cmd = "select * from air"
        cur.execute(cmd)
        data = cur.fetchall()
        c =1
        for i in data:
                dt = i[0]
                pm2_5 = i[1]
                no2 = i[2]
                so2 = i[3]
                tree.insert('','end', text = c, values = (dt,pm2_5,no2,so2))
                c+=1
        tree.grid(row =1, column =1)
        window5.mainloop()



                
window =Tk()
window.geometry("400x400")
window.configure(bg="blue")
l1 =tk.Label(window, text ="Welcome to air survialance system", font = "bold")
l1.pack()
l1.configure(bg ="blue",fg ="white")
b1 = tk.Button(window, text = "Add Record",width = 30, command = lambda:add_new_record())
b1.pack()
b2 = tk.Button(window, text = "Check Records", width = 30,command = lambda:show_records())
b2.pack()
window.mainloop()

