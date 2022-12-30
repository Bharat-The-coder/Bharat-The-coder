from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
from datetime import date as dt
import datetime
from time import strftime
from PIL import ImageTk, Image
#connetion establishing to database ......... 
conn = psycopg2.connect(database="project",user="postgres",password="Bharat@232",host="localhost",port='5432')
def insert_form():  
    # insert_form database connect
    window_2=Toplevel(width=600,height=700)
    
    def action():
        if p_id.get()=="" or name.get()=="" or p_type.get()=="" or quantity.get()=="" or price.get()=="" or company_name.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = window_2)
        else:
            try:
                cur = conn.cursor()
                sql=cur.execute('''INSERT INTO "product"(id, name, type, quantity, price, company_name, date)'''
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                        p_id.get(),
                        name.get(),
                        p_type.get(),
                        quantity.get(),
                        price.get(),
                        company_name.get(),
                        date
                        ))
                conn.commit()
                messagebox.showinfo("Success" , "Product data inserted Successfully" , parent = window_2)
                clear()
            except Exception as es:
                messagebox.showerror("Error" , "Cant Insert Values....\n ",es, parent = window_2)
    # clear data function
    def clear():
            p_id.delete(0,END),
            name.delete(0,END)
            p_type.set("Import")
            quantity.delete(0,END)
            price.delete(0,END)
            company_name.delete(0,END)
    
    #heading label
    heading = Label(window_2 , text = "Insert Form" , font = 'Verdana 25 bold',border=1)
    heading.place(x=220 , y=100)

    # form data label
    p_id = Label(window_2, text= "Product ID :" , font='Verdana 10 bold',bg="lightblue",bd=1)
    p_id.place(x=70,y=170)
    name = Label(window_2, text= "Product Name :" , font='Verdana 10 bold',bg="lightblue")
    name.place(x=70,y=200)
    p_type = Label(window_2, text= "Product_type :" , font='Verdana 10 bold',bg="lightblue")
    p_type.place(x=70,y=230)

    quantity = Label(window_2, text= "Quantity :" , font='Verdana 10 bold',bg="lightblue")
    quantity.place(x=70,y=260)
    price = Label(window_2, text= "Price :" , font='Verdana 10 bold',bg="lightblue")
    price.place(x=70,y=300)

    company_name = Label(window_2, text= "Company Name : " , font='Verdana 10 bold',bg="lightblue")
    company_name.place(x=70,y=340)

    # Entry Box ------------- --------------------------------------------------
    p_id=StringVar()
    name=StringVar()
    p_type = StringVar()
    quantity=IntVar()
    price=IntVar()
    company_name=StringVar()
    date=dt.today()
    #start of Entry Widgets.........
    p_id = Entry(window_2, width=40 , textvariable = p_id,bd=2)
    p_id.place(x=250 , y=170)
 
    name = Entry(window_2, width=40 , textvariable = name,bd=2)
    name.place(x=250 , y=200)
    
    Radio_button_male = ttk.Radiobutton(window_2,text='Import', value="Import", variable = p_type).place(x= 250 , y= 230)
    Radio_button_female = ttk.Radiobutton(window_2,text='Export', value="Export", variable = p_type).place(x= 330 , y= 230)
    
    quantity = Entry(window_2, width=40, textvariable=quantity,bd=2)
    quantity.place(x=250 , y=260)
 
    price = Entry(window_2, width=40 , textvariable = price,bd=2)
    price.place(x=250 , y=300)

    company_name = Entry(window_2, width=40,textvariable = company_name,bd=2)
    company_name.place(x=250 , y=340)
    # button login and clear
    btn_signup = Button(window_2, text = "Insert Data" ,font='Verdana 10 bold',bg="lightGreen", command = action)
    btn_signup.place(x=250, y=413+40)
    btn_login = Button(window_2, text = "Clear" ,font='Verdana 10 bold',fg="white",bg="Red" , command = clear)
    btn_login.place(x=360, y=413+40)
    window_2.mainloop()
#function to update a data in table
def update_form():
    # Update form database connect
    window_2=Toplevel(width=600,height=700)
    def action():
        if p_id.get()=="" or name.get()=="" or p_type.get()=="" or quantity.get()=="" or price.get()=="" or company_name.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = window_2)
        else:
            try:
                cur = conn.cursor()
                sql=cur.execute("UPDATE public.product SET name=%s, type=%s, quantity=%s, price=%s, company_name=%s, date=%s WHERE id=%s;",
                        (
                        name.get(),
                        p_type.get(),
                        quantity.get(),
                        price.get(),
                        company_name.get(),
                        date,
                        p_id.get()
                        ))
                conn.commit()
                var=cur.rowcount
                if var!=0:
                    messagebox.showinfo("Success" ,"Product Id "+p_id.get()+" updated successfully" , parent = window_2)
                else:
                    messagebox.showwarning("Error" , "Product Id "+p_id.get()+" doesn't exists" , parent = window_2)
                clear()
            except Exception as es:
                messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = window_2)
    # clear data function
    def clear():
            p_id.delete(0,END),
            name.delete(0,END)
            p_type.set("Import")
            quantity.delete(0,END)
            price.delete(0,END)
            company_name.delete(0,END)
    
    #heading label
    heading = Label(window_2 , text = "Update Form", font = 'Verdana 25 bold')
    heading.place(x=220 , y=100)

    # form data label
    p_id = Label(window_2, text= "Product ID :" , font='Verdana 10 bold',bg="lightblue")
    p_id.place(x=70,y=170)
    name = Label(window_2, text= "Product Name :" , font='Verdana 10 bold',bg="lightblue")
    name.place(x=70,y=200)
    p_type = Label(window_2, text= "Product_type :" , font='Verdana 10 bold',bg="lightblue")
    p_type.place(x=70,y=230)

    quantity = Label(window_2, text= "Quantity :" , font='Verdana 10 bold',bg="lightblue")
    quantity.place(x=70,y=260)
    price = Label(window_2, text= "Price :" , font='Verdana 10 bold',bg="lightblue")
    price.place(x=70,y=300)

    company_name = Label(window_2, text= "Company Name : " , font='Verdana 10 bold',bg="lightblue")
    company_name.place(x=70,y=340)

    # Entry Box ------------------------------------------------------------------
    p_id=StringVar()
    name=StringVar()
    p_type = StringVar()
    quantity=IntVar()
    price=IntVar()
    company_name=StringVar()
    date=dt.today()
    
    p_id = Entry(window_2, width=40 , textvariable = p_id,bd=3)
    p_id.place(x=250 , y=170)
 
    name = Entry(window_2, width=40 , textvariable = name,bd=3)
    name.place(x=250 , y=200)
    
    Radio_button_male = ttk.Radiobutton(window_2,text='Import', value="Import", variable = p_type).place(x= 250 , y= 230)
    Radio_button_female = ttk.Radiobutton(window_2,text='Export', value="Export", variable = p_type).place(x= 330 , y= 230)
    
    quantity = Entry(window_2, width=40, textvariable=quantity,bd=3)
    quantity.place(x=250 , y=260)
 
    price = Entry(window_2, width=40 , textvariable = price,bd=3)
    price.place(x=250 , y=300)

    company_name = Entry(window_2, width=40,textvariable = company_name,bd=3)
    company_name.place(x=250 , y=340)
    # button login and clear
    btn_signup = Button(window_2, text = "Update Data",font='Verdana 10 bold',bg="lightblue", command = action)
    btn_signup.place(x=250, y=413+40)
    btn_login = Button(window_2, text = "Clear" ,font='Verdana 10 bold',fg="white",bg="red",width=10, command = clear)
    btn_login.place(x=360, y=413+40)
    window_2.mainloop()

#show function to show data
def show():
    '''This is function to show data from a table '''
    cursor = conn.cursor()
    global p_id
    p_id=StringVar()
    show_w=Toplevel(width=900,height=700)
    show_w['bg'] = '#AC90F2'
    my_str=StringVar()
    #Label(show_w, text= "Output" , font='Verdana 10 bold',textvariable=my_str).place(x=140,y=200)
    show_frame = Frame(show_w)
    show_frame.pack()
    show_data = ttk.Treeview(show_frame)

    show_data['columns'] = ('id', 'name', 'type', 'quantity', 'price','company_name','date')

    show_data.column("#0", width=0,  stretch=NO)
    show_data.column("id",anchor=CENTER, width=80)
    show_data.column("name",anchor=CENTER,width=80)
    show_data.column("type",anchor=CENTER,width=80)
    show_data.column("quantity",anchor=CENTER,width=80)
    show_data.column("price",anchor=CENTER,width=80)
    show_data.column("company_name",anchor=CENTER,width=80)
    show_data.column("date",anchor=CENTER,width=80)

    show_data.heading("#0",text="",anchor=CENTER)
    show_data.heading("id",text="Id",anchor=CENTER)
    show_data.heading("name",text="Name",anchor=CENTER)
    show_data.heading("type",text="type",anchor=CENTER)
    show_data.heading("quantity",text="quantity",anchor=CENTER)
    show_data.heading("price",text="price",anchor=CENTER)
    show_data.heading("company_name",text="company_name",anchor=CENTER)
    show_data.heading("date",text="date",anchor=CENTER)
    # add one Label
    def show_one():
        try:
      # check input is integer or not
            #deleting existing tree
            for item in show_data.get_children():
                show_data.delete(item)
            try:
                    sql=('''SELECT * FROM "product" WHERE id=%s''')
                    data=[p_id.get()]
                    cursor.execute(sql,data)
                    var =cursor.fetchone()
                    if var==None:
                                        messagebox.showinfo("Error","Cant show values due "+p_id.get()+" Does not Exits")
                    else:
                                        
                                        show_data.insert(parent='',index='end' ,iid=0,text='',
                                        values=(var))
            except:
                messagebox.showerror("Error","While showing a values or Product ID is empty",parent=show_w)
        except:
            my_str.set("Check input")
    def show_all():
            #deleting existing tree
            for item in show_data.get_children():
                show_data.delete(item)
            my_cursor=cursor.execute('''SELECT * FROM "product" ORDER BY date desc''')
            var=cursor.fetchall()
            i=1
            if var==[]:
                messagebox.showinfo("Warning","Nothing to show here")
                show_w.destroy()
            else:
                j=0
                for product in var:
                    show_data.insert(parent='',index='end' ,iid=j,text='',
                    values=(product))
                    j+=1
    Label(show_w, text= "Product ID :" , font='Verdana 10 bold').place(x=400,y=280)
    Entry(show_w, width=40 ,textvariable = p_id,bd=3).place(x=500 , y=280)
    button=Button(show_w, text = "Show" ,font='Verdana 10 bold',bg="Green",fg="white",command = show_one)
    button.place(x=550,y=320)
    button2=Button(show_w, text = "Show all" ,font='Verdana 10 bold',bg="Green",fg="white",command = show_all)
    button2.place(x=650,y=320)
    show_data.pack()
#function to delete a data frm table
def delete_row():
    def delete_data():
        '''This is function to Delete data from a table '''
        var=messagebox.askquestion("Delete row?","are you really want to delete data?")
        if p_id.get()=="":
            try:
                if (var):
                    messagebox.showerror("error","please insert something" , parent = Delete_w)
                else:
                    my_conn = conn.cursor()
                    sql=('''DELETE FROM "product" WHERE id=%s''')
                    data=[p_id.get()]
                    my_conn.execute(sql,data)
                    var= my_conn.rowcount
                    if var ==0:
                        messagebox.showerror("error","No values to delete" , parent = Delete_w)
                    else:
                        conn.commit()
                        messagebox.showinfo("Success","Values Deleted successfully" , parent = Delete_w)
            except(Exception,psycopg2.Error) as error:
                messagebox.showerror("Cant delete values due to",error ,parent = Delete_w)
    global p_id
    Delete_w=Toplevel(width=500,height=500)
    p_id=StringVar()
    Label(Delete_w, text= "Product ID :" , font='Verdana 10 bold').place(x=40,y=100)
    Entry(Delete_w, width=40 ,textvariable = p_id,bd=3).place(x=180 , y=100)
    button=Button(Delete_w, text = "Delete" ,font='Verdana 10 bold',bg="red",fg="white",command = delete_data)
    button.place(x=150,y=150)
    window.mainloop()
def home():
    header=Label(window,font=('times new roman', 20, 'bold'),bg='yellow',text="Product Entry System",width=200).pack(anchor="center")
    lbl = Label(window, font=('calibri', 15, 'bold'),bg='yellow',width=150)
    lbl.pack()
    def date_time():
        string = strftime('Date:%D \n Time:%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,date_time)
    date_time()
#starting of main function
window=tk.Tk()
window.geometry("1200x800")
window.title("Product entry System")
window['bg'] = '#AC99F2'
window.resizable(True,True)
photo = PhotoImage(file = "icon.png")
window.iconphoto(False, photo)
menubar = Menu(window)
menubar.add_command(label="Home")  
menubar.add_command(label="Insert", command=insert_form)  
menubar.add_command(label="Update",command=update_form)  
menubar.add_command(label="Show",command=show)
menubar.add_command(label="Delete",command=delete_row)
menubar.add_command(label="Help")
menubar.add_command(label="Quit ", command=window.quit)  
window.config(menu=menubar)
home()
#use thie code to insert image
img = ImageTk.PhotoImage(Image.open("back.png"))
label = Label(window, image = img)
label.pack()
window.mainloop()
