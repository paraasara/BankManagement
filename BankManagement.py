import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector as con
from mysql.connector import Error
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ACER\Desktop\Suhas\College\DBMS\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

mycon=con.connect(host="localhost",user="root",passwd="password")

A=mycon.cursor()
A.execute("Create  database IF NOT EXISTS DBMS_PROJECT")
A.execute("Use DBMS_PROJECT")

A.execute('''CREATE TABLE IF NOT EXISTS LOGIN (USER_ID INT PRIMARY KEY,
          USER_NAME VARCHAR(20), NAME VARCHAR(20), MAIL_ID VARCHAR (40), 
          PHONE_NUMBER INT, ADDRESS VARCHAR(75), PASSWORD INT);''')

A.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT (ACCOUNT_NO INT PRIMARY KEY,
          USER_ID INT,BANK VARCHAR(20),BRANCH VARCHAR(20),ACCOUNT_TYPE VARCHAR(20),
          BALANCE DECIMAL(10,2));''')

A.execute('''CREATE TABLE IF NOT EXISTS TRANSACTION (TRANSACTION_ID INT AUTO_INCREMENT PRIMARY KEY,
          ACCOUNT_NO INT, SCHEDULE DATE, AMOUNT DECIMAL(10,2), TRANSACTION_TYPE ENUM('DEPOSIT','WITHDRAWAL'),
          TO_ACC_NO INT, BALANCE DECIMAL(10.2));''')

def create_connection():
    try:
        conn = mycon
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error: {e}")
    return None

def TransactionHistory_HP():
    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT SCHEDULE,TRANSACTION_ID,AMOUNT,TRANSACTION_TYPE,ACCOUNT_NO,BALANCE FROM TRANSACTION''')
        Data=cursor.fetchall()
    
    except Error as e:
        print(f"Error: {e}")
    
    canvas6 = Canvas(windowL,bg = "#FFFFFF",height = 539,width = 794,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas6.place(x=286,y=61)
    canvas6.create_text(26.0,26.0,anchor="nw",text="Transaction History",fill="#072EFF",font=("KottaOne Regular", 25 * -1))
    canvas6.create_text(26.0,70.0,anchor="nw",text="NOTE: Contains History of all the accounts",fill="#000000",font=("KottaOne Regular", 15 * -1))
    canvas6.create_rectangle(10.0,100.0,783.0,150.0,fill="#072EFF",outline="")
    canvas6.create_text(36.0,115.0,anchor="nw",text="Date",fill="#FFFFFF",font=("Alice Regular", 15 * -1))
    canvas6.create_text(104.0,115.0,anchor="nw",text="Transaction ID",fill="#FFFFFF",font=("Alice Regular", 15 * -1))
    canvas6.create_text(247.0,115.0,anchor="nw",text="Amount",fill="#FFFFFF",font=("Alice Regular", 15 * -1))
    canvas6.create_text(351.0,115.0,anchor="nw",text="Transaction type",fill="#FFFFFF",font=("Alice Regular", 15 * -1))
    canvas6.create_text(509.0,115.0,anchor="nw",text="Source Acc Number",fill="#FFFFFF",font=("Alice Regular", 15 * -1))
    canvas6.create_text(700.0,115.0,anchor="nw",text="Balance",fill="#FFFFFF",font=("Alice Regular", 15 * -1))
    canvas_TH = Canvas(windowL,height = 350,width = 765,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas_TH.place(x=297,y=211)
    columns = ('Column1', 'Column2', 'Column3','Column4', 'Column5', 'Column6')
    tree = ttk.Treeview(canvas_TH, columns=columns, show='headings',height=17)
    tree.column('Column1', width=90,anchor='center')
    tree.column('Column2', width=125,anchor='center')
    tree.column('Column3', width=120,anchor='center')
    tree.column('Column4', width=150,anchor='center')
    tree.column('Column5', width=160,anchor='center')
    tree.column('Column6', width=123,anchor='center')
    for item in Data:
        tree.insert('', 0, values=item)
    tree.pack(side='left', fill='both')
    canvas_TH.mainloop()
    canvas6.mainloop()

def Accounts_HP():
    canvas5 = Canvas(windowL,bg = "#FFFFFF",height = 539,width = 794,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas5.place(x=286,y=61)

    canvas5.create_rectangle(11.0,11.0,783.0,47.0,fill="#0024E3",outline="")
    canvas5.create_rectangle(11.0,56.0,783.0,160.0,fill="#E7E7E7",outline="")
    canvas5.create_rectangle(11.0,190.0,783.0,530.0,fill="#E7E7E7",outline="")

    ACentry_5 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ACentry_5.place(x=514.0,y=502.0,width=436.0,height=24.0)

    ACentry_4 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ACentry_4.place(x=514.0,y=459.0,width=436.0,height=24.0)

    ACentry_3 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ACentry_3.place(x=514.0,y=416.0,width=436.0,height=24.0)

    ACentry_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ACentry_2.place(x=514.0,y=373.0,width=436.0,height=24.0)

    ACentry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    ACentry_1.place(x=514.0,y=330.0,width=436.0,height=24.0)

    canvas5.create_text(136.0,445.0,anchor="nw",text="Balance",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas5.create_text(88.0,402.0,anchor="nw",text="Account Type",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas5.create_text(141.0,359.0,anchor="nw",text="Branch",fill="#000000",    font=("Alice Regular", 18 * -1))
    canvas5.create_text(157.0,316.0,anchor="nw",text="Bank",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas5.create_text(61.0,273.0,anchor="nw",text="Account Number",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas5.create_text(42.0,221.0,anchor="nw",text="Create Account",fill="#0024E3",font=("KottaOne Regular", 20 * -1))

    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        User_ID_is = 0
        cursor.execute("SELECT USER_ID FROM LOGIN WHERE USER_NAME = %s", (User_name_is,))
        User_ID_is=cursor.fetchone()
        def Creating_Account():
            cursor.execute("INSERT INTO ACCOUNT VALUES (%s, %s, %s, %s, %s, %s)",(int(ACentry_1.get()),User_ID_is[0],ACentry_2.get(),ACentry_3.get(),ACentry_4.get(),int(ACentry_5.get())))
            conn.commit()
            messagebox.showinfo("Done","Account Created.")
            Back_Login()
            cursor.close()
    
    except Error as e:
        print(f"Error: {e}")

    value_inside = StringVar(canvas5)
    value_inside.set(primary_acc_no[0])
    ACoption_1=OptionMenu(canvas5,value_inside, *account_no_of_user)
    ACoption_1.place(x=225.0,y=72.0,width=436.0,height=24.0)

    def Sel_Option():
        global primary_acc_no
        temp=value_inside.get()
        Temp=eval(temp)
        if Temp in account_no_of_user:
            primary_acc_no = Temp
            messagebox.showinfo("Done","Account Changed.")
            Dashboard_HP()

    button_image_3 = PhotoImage(file=relative_to_assets("ACbutton_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=Sel_Option,relief="flat",cursor="hand2")
    button_3.place(x=689.0,y=176.0,width=85.3448257446289,height=25.0)

    ACbutton_image_2 = PhotoImage(file=relative_to_assets("ACbutton_2.png"))
    ACbutton_2 = Button(image=ACbutton_image_2,borderwidth=0,highlightthickness=0,command=Creating_Account,relief="flat",cursor="hand2")
    ACbutton_2.place(x=645.0,y=547.0,width=174.0,height=30.0)

    canvas5.create_text(80.0,77.0,anchor="nw",text="Select Account",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas5.create_text(42.0,15.0,anchor="nw",text="Account",fill="#FFFFFF",font=("KottaOne Regular", 20 * -1))
    canvas5.create_text(383.0,164.0,anchor="nw",text="OR",fill="#000000",font=("Alice Regular", 20 * -1))
    canvas5.mainloop()

def FundsTransfer_HP():
    canvas4 = Canvas(windowL,bg = "#FFFFFF",height = 539,width = 794,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas4.place(x=286,y=61)
    canvas4.create_rectangle(10.0,17.0,782.0,62.0,fill="#0024E3",outline="")
    canvas4.create_rectangle(10.0,187.0,782.0,509.0,fill="#E7E7E7",outline="")

    canvas4.create_text(61.0,239.0,anchor="nw",text="Account Number",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas4.create_text(109.0,279.0,anchor="nw",text="Bank name",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas4.create_text(88.0,396.0,anchor="nw",text="Enter Amount",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas4.create_text(116.0,318.0,anchor="nw",text="IFSC Code",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas4.create_text(56.0,357.0,anchor="nw",text="Beneficiary Name",fill="#000000",font=("Alice Regular", 18 * -1))

    entryFT_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    entryFT_1.place(x=514.0,y=297.0,width=436.0,height=24.0)

    entryFT_2 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    entryFT_2.place(x=514.0,y=336.0,width=436.0,height=24.0)

    entryFT_3 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    entryFT_3.place(x=514.0,y=375.0,width=436.0,height=24.0)

    entryFT_4 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    entryFT_4.place(x=514.0,y=414.0,width=436.0,height=24.0)

    entryFT_5 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    entryFT_5.place(x=514.0,y=453.0,width=436.0,height=24.0)

    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT ACCOUNT_NO, ACCOUNT_TYPE, BALANCE FROM ACCOUNT WHERE ACCOUNT_NO = %s", (primary_acc_no[0],))
        result = cursor.fetchone()
        current_balance = result[2]
        def FUN_FOR_BT():
            if current_balance < int(entryFT_5.get()):
                messagebox.showerror("Result", "Insufficient funds.")
                conn.rollback()
                return
            new_balance = current_balance - int(entryFT_5.get())
            cursor.execute("UPDATE ACCOUNT SET BALANCE = %s WHERE ACCOUNT_NO = %s", (new_balance, primary_acc_no[0]))
            cursor.execute('''INSERT INTO TRANSACTION (ACCOUNT_NO, SCHEDULE, AMOUNT, TRANSACTION_TYPE, TO_ACC_NO, BALANCE)
                           VALUES (%s, CURDATE(), %s, 'WITHDRAWAL', %s, %s)''',(primary_acc_no[0], int(entryFT_5.get()), int(entryFT_1.get()), new_balance))
            conn.commit()
            messagebox.showinfo("Done", "Transaction Successful.")
            Dashboard_HP()
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    buttonFT_image_1 = PhotoImage(file=relative_to_assets("FTbutton_1.png"))
    buttonFT_1 = Button(image=buttonFT_image_1,borderwidth=0,highlightthickness=0,command=FUN_FOR_BT,relief="flat",cursor="hand2")
    buttonFT_1.place(x=645.0,y=501.0,width=174.0,height=35.0)

    canvas4.create_text(26.0,206.0,anchor="nw",text="Transfer Details",fill="#0024E3",font=("Alice Regular", 20 * -1))
    canvas4.create_text(26.0,26.0,anchor="nw",text="One Time Transfer",fill="#FFFFFF",font=("KottaOne Regular", 20 * -1))
    canvas4.create_text(60.0,78.0,anchor="nw",text="From Account Number:",fill="#000000",font=("Alice Regular", 15 * -1))
    canvas4.create_text(60.0,100.0,anchor="nw",text=str(result[0]),fill="#000000",font=("Alice Regular", 20 * -1))
    canvas4.create_text(60.0,130.0,anchor="nw",text=str(result[1])+" ACCOUNT",fill="#000000",font=("Alice Regular", 15 * -1))
    canvas4.create_text(60.0,153.0,anchor="nw",text="Balance: "+str(result[2]),fill="#000000",font=("Alice Regular", 20 * -1))

    button_image_2 = PhotoImage(file=relative_to_assets("FTbutton_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,relief="flat",cursor="hand2")
    button_2.place(x=950.0,y=143.0,width=109.0,height=17.0)
    canvas4.mainloop()

def Withdraw_HP():
    canvas3 = Canvas(windowL,bg = "#FFFFFF",height = 539,width = 794,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas3.place(x=286,y=61)
    canvas3.create_rectangle(11.0,84.0,783.0,129.0,fill="#0024E3",outline="")
    canvas3.create_rectangle(11.0,148.0,783.0,455.0,fill="#E7E7E7",outline="")
    canvas3.create_text(65.0,200.0,anchor="nw",text="Account Number:",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas3.create_text(240.0,200.0,anchor="nw",text=primary_acc_no[0],fill="#000000",font=("Alice Regular", 18 * -1))    
    canvas3.create_text(133.0,240.0,anchor="nw",text="Amount",fill="#000000",font=("Alice Regular", 18 * -1))
    WTentry_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    WTentry_1.place(x=514.0,y=297.0,width=436.0,height=24.0)
    canvas3.create_text(44.0,92.0,anchor="nw",text="Withdraw",fill="#FFFFFF",font=("KottaOne Regular", 20 * -1))

    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT BALANCE FROM ACCOUNT WHERE ACCOUNT_NO = %s", (primary_acc_no[0],))
        result = cursor.fetchone()
        if result is None:
            messagebox.showerror("Error","Account not found.")
            conn.rollback()
            return
        current_balance = result[0]
        def FN_FOR_BT():
            if current_balance < int(WTentry_1.get()):
                messagebox.showerror("Result", "Insufficient funds.")
                conn.rollback()
                return
            new_balance = current_balance - int(WTentry_1.get())
            cursor.execute("UPDATE ACCOUNT SET BALANCE = %s WHERE ACCOUNT_NO = %s", (new_balance, primary_acc_no[0]))
            cursor.execute('''INSERT INTO TRANSACTION (ACCOUNT_NO, SCHEDULE, AMOUNT, TRANSACTION_TYPE, BALANCE)
                           VALUES (%s, CURDATE(), %s, 'WITHDRAWAL', %s)''',(primary_acc_no[0], int(WTentry_1.get()), new_balance))
            conn.commit()
            messagebox.showinfo("Done", "Transaction Successful.")
            Dashboard_HP()
            cursor.close()

    except Error as e:
        print(f"Error: {e}")      
        conn.rollback()
    
    WTbutton_image_1 = PhotoImage(file=r"C:\Users\ACER\Desktop\Suhas\College\DBMS\assets\frame0\WTbutton_1.png")
    WTbutton_1 = Button(image=WTbutton_image_1,borderwidth=0,highlightthickness=0,command=FN_FOR_BT,relief="flat",cursor="hand2")
    WTbutton_1.place(x=596.0,y=391.0,width=174.0,height=35.0)

    canvas3.mainloop()

def Deposit_HP():
    canvas2 = Canvas(windowL,bg = "#FFFFFF",height = 539,width = 794,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas2.place(x=286,y=61)
    canvas2.create_rectangle(11.0,84.0,783.0,129.0,fill="#0024E3",outline="")
    canvas2.create_rectangle(11.0,148.0,783.0,455.0,fill="#E7E7E7",outline="")

    canvas2.create_text(65.0,200.0,anchor="nw",text="Account Number:",fill="#000000",font=("Alice Regular", 18 * -1))
    canvas2.create_text(240.0,200.0,anchor="nw",text=primary_acc_no[0],fill="#000000",font=("Alice Regular", 18 * -1))    
    canvas2.create_text(133.0,240.0,anchor="nw",text="Amount",fill="#000000",font=("Alice Regular", 18 * -1))

    entryDP_1 = Entry(bd=0,bg="#FFFFFF",fg="#000716",highlightthickness=0)
    entryDP_1.place(x=514.0,y=297.0,width=436.0,height=24.0)
    canvas2.create_text(44.0,92.0,anchor="nw",text="Deposit",fill="#FFFFFF",font=("KottaOne Regular", 20 * -1))

    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT BALANCE FROM ACCOUNT WHERE ACCOUNT_NO = %s", (primary_acc_no[0],))
        result = cursor.fetchone()
        if result is None:
            messagebox.showerror("Error", "Account not found.")
            conn.rollback()
            return
        current_balance = result[0]
        def FN_BTN():
            new_balance = current_balance + int(entryDP_1.get())
            cursor.execute("UPDATE ACCOUNT SET BALANCE = %s WHERE ACCOUNT_NO = %s", (new_balance, primary_acc_no[0]))
            cursor.execute('''INSERT INTO TRANSACTION (ACCOUNT_NO, SCHEDULE, AMOUNT, TRANSACTION_TYPE, BALANCE)
                           VALUES (%s, CURDATE(), %s, 'DEPOSIT', %s)''',(primary_acc_no[0], int(entryDP_1.get()),new_balance))
            conn.commit()
            messagebox.showinfo("Done", "Transfer Complete.")
            Dashboard_HP()
            cursor.close()

    except Error as e:
        print(f"Error: {e}")      
        conn.rollback()

    buttonDP_image_1 = PhotoImage(file=r"C:\Users\ACER\Desktop\Suhas\College\DBMS\assets\frame0\DPbutton_1.png")
    buttonDP_1 = Button(image=buttonDP_image_1,borderwidth=0,highlightthickness=0,command=FN_BTN,relief="flat",cursor="hand2")
    buttonDP_1.place(x=596.0,y=391.0,width=174.0,height=35.0)
    canvas2.mainloop()

def Dashboard_HP():
    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT A.ACCOUNT_NO, A.BANK,A.ACCOUNT_TYPE, A.BRANCH, L.PHONE_NO, L.NAME, A.BALANCE 
                       FROM ACCOUNT A, LOGIN L WHERE A.USER_ID=L.USER_ID AND A.ACCOUNT_NO =  %s''', (primary_acc_no[0],))
        result=cursor.fetchone()
        
    except Error as e:
        print(f"Error: {e}")

    canvas1 = Canvas(windowL,bg = "#FFFFFF",height = 539,width = 794,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas1.place(x=286,y=61)
    canvas1.create_rectangle(27.0,34.0,381.0,198.0,fill="#0024E3",outline="")
    canvas1.create_rectangle(410.0,34.0,764.0,198.0,fill="#0024E3",outline="")

    canvas1.create_text(36.0,50.0,anchor="nw",text="Name: "+str(result[5]),fill="#FFFFFF",font=("Alice Regular", 25 * -1))
    canvas1.create_text(420.0,100.0,anchor="nw",text="Account Number:\n"+str(result[0]),fill="#FFFFFF",font=("Alice Regular", 17 * -1))
    canvas1.create_text(620.0,150.0,anchor="nw",text="Branch:\n"+str(result[3]),fill="#FFFFFF",font=("Alice Regular", 17 * -1))
    canvas1.create_text(36.0,150.0,anchor="nw",text="Bank Name:\n"+str(result[1]),fill="#FFFFFF",font=("Alice Regular", 17 * -1))
    canvas1.create_text(420.0,150.0,anchor="nw",text="Account Type:\n"+str(result[2]),fill="#FFFFFF",font=("Alice Regular", 17 * -1))
    canvas1.create_text(36.0,100.0,anchor="nw",text="Phone Number:\n"+str(result[4]),fill="#FFFFFF",font=("Alice Regular", 17 * -1))
    canvas1.create_text(420.0,50.0,anchor="nw",text="Balance: "+str(result[6]),fill="#FFFFFF",font=("Alice Regular", 25 * -1))
    canvas1.create_text(27.0,238.0,anchor="nw",text="Transaction History",fill="#000000",font=("AlegreyaSans Bold", 30 * -1))

    #image_PSM_BANK = PhotoImage(file=relative_to_assets("image_PSM_BANK.png"))
    #image_3 = canvas1.create_image(396.0,365.0,image=image_PSM_BANK)

    columns = ('Column1', 'Column2', 'Column3','Column4', 'Column5', 'Column6')
    tree = ttk.Treeview(canvas1, columns=columns, show='headings')
    tree.column('Column1', width=90,anchor='center')
    tree.column('Column2', width=130,anchor='center')
    tree.column('Column3', width=130,anchor='center')
    tree.column('Column4', width=160,anchor='center')
    tree.column('Column5', width=130,anchor='center')
    tree.column('Column6', width=120,anchor='center')
    tree.heading("#0",text='',anchor='center')
    tree.heading("Column1",text='Date',anchor='center')
    tree.heading("Column2",text='Transaction ID',anchor='center')
    tree.heading("Column3",text='Amount',anchor='center')
    tree.heading("Column4",text='Transaction Type',anchor='center')
    tree.heading("Column5",text='Source Acc Number',anchor='center')
    tree.heading("Column6",text='Balance',anchor='center')

    #for item in Data:
    #    tree.insert('', tk.END, values=item)
    tree.place(x=12,y=300)

    canvas1.mainloop()

def HomePage():
    window.destroy()
    global windowL
    windowL = Tk()
    windowL.geometry("1080x600")
    windowL.configure(bg = "#FFFFFF")
    canvas = Canvas(windowL,height = 600,width = 1080,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(0.0,61.0,282.0,600.0,fill="#F0EDED",outline="")

    HPbutton_image_1 = PhotoImage(file=relative_to_assets("HPbutton_1.png"))
    HPbutton_1 = Button(image=HPbutton_image_1,borderwidth=0,highlightthickness=0,command=Back_Login,relief="flat",cursor="hand2")
    HPbutton_1.place(x=926.0,y=12.0,width=132.0,height=37.0)

    HPbutton_image_2 = PhotoImage(file=relative_to_assets("HPbutton_2.png"))
    HPbutton_2 = Button(image=HPbutton_image_2,borderwidth=0,highlightthickness=0,command=TransactionHistory_HP,relief="flat",cursor="hand2")
    HPbutton_2.place(x=17.0,y=484.0,width=248.0,height=50.0)

    HPbutton_image_3 = PhotoImage(file=relative_to_assets("HPbutton_3.png"))
    HPbutton_3 = Button(image=HPbutton_image_3,borderwidth=0,highlightthickness=0,command=Accounts_HP,relief="flat",cursor="hand2")
    HPbutton_3.place(x=23.0,y=408.0,width=193.2341766357422,height=50.0)

    HPbutton_image_4 = PhotoImage(file=relative_to_assets("HPbutton_4.png"))
    HPbutton_4 = Button(image=HPbutton_image_4,borderwidth=0,highlightthickness=0,command=FundsTransfer_HP,relief="flat",cursor="hand2")
    HPbutton_4.place(x=20.0,y=337.0,width=228.0,height=50.0)

    HPbutton_image_5 = PhotoImage(file=relative_to_assets("HPbutton_5.png"))
    HPbutton_5 = Button(image=HPbutton_image_5,borderwidth=0,highlightthickness=0,command=Withdraw_HP,relief="flat",cursor="hand2")
    HPbutton_5.place(x=23.0,y=261.0,width=189.0,height=50.0)

    HPbutton_image_6 = PhotoImage(file=relative_to_assets("HPbutton_6.png"))
    HPbutton_6 = Button(image=HPbutton_image_6,borderwidth=0,highlightthickness=0,command=Deposit_HP,relief="flat",cursor="hand2")
    HPbutton_6.place(x=20.0,y=181.0,width=179.19619750976562,height=50.0)

    HPbutton_image_7 = PhotoImage(file=relative_to_assets("HPbutton_7.png"))
    HPbutton_7  = Button(image=HPbutton_image_7,borderwidth=0,highlightthickness=0,command=Dashboard_HP,relief="flat",cursor="hand2")
    HPbutton_7.place(x=17.0,y=105.0,width=213.0,height=50.0)

    canvas.create_rectangle(-1.0,58.0,1079.999966128482,61.9999997829774,fill="#000000",outline="")
    canvas.create_text(113.0,12.0,anchor="nw",text="PSM BANK",fill="#000000",font=("Times New Roman", 30 * -1))

    HPimage_image_1 = PhotoImage(file=relative_to_assets("HPimage_1.png"))
    HPimage_1 = canvas.create_image(49.0,29.0,image=HPimage_image_1)

    Dashboard_HP()
    windowL.mainloop()

def Create_Account_Page():
    window.destroy()
    global window1
    window1= Tk()
    window1.title("PSM Bank")
    window1.geometry("750x400")
    window1_notebook = ttk.Notebook(window1)
    window1_notebook.pack()

    window1_frame1 = Frame(window1_notebook,width=750,height=400,bg="blue")
    window1_frame2 = Frame(window1_notebook,width=750,height=400,bg="#021B9A")
    window1_frame1.pack(fill="both",expand=1)
    window1_frame2.pack(fill="both",expand=1)

    window1_notebook.add(window1_frame1,text="User Creation")
    window1_notebook.add(window1_frame2,text="Primary Account Creation")

    Create_acc_For_PA=Label(window1_frame2,text="Create Primary Account",font=("Times New Roman",25),background="#021B9A",foreground="white")
    Create_acc_For_PA.place(x=10.0,y=10.0)
    Create_acc_ACNO_PA=Label(window1_frame2,text="Account Number",font=("Times New Roman",15),background="#021B9A",foreground="white")
    Create_acc_ACNO_PA.place(x=50.0,y=70.0)
    CA_PA_entry_1=Entry(window1_frame2,bd=0,font=("kotha one",15))
    CA_PA_entry_1.place(x=350,y=70)
    Create_acc_Bank_PA=Label(window1_frame2,text="Bank",font=("Times New Roman",15),background="#021B9A",foreground="white")
    Create_acc_Bank_PA.place(x=50.0,y=105.0)
    CA_entry_2_PA=Entry(window1_frame2,bd=0,font=("kotha one",15))
    CA_entry_2_PA.place(x=350,y=105)
    Create_acc_Branch_PA=Label(window1_frame2,text="Branch",font=("Times New Roman",15),background="#021B9A",foreground="white")
    Create_acc_Branch_PA.place(x=50,y=140)
    CA_entry_3_PA=Entry(window1_frame2,bd=0,font=("kotha one",15))
    CA_entry_3_PA.place(x=350,y=140)
    Create_acc_AccT=Label(window1_frame2,text="Account Type",font=("Times New Roman",15),background="#021B9A",foreground="white")
    Create_acc_AccT.place(x=50,y=175)
    CA_entry_4_PA=Entry(window1_frame2,bd=0,font=("kotha one",15))
    CA_entry_4_PA.place(x=350,y=175)
    Create_acc_Bal=Label(window1_frame2,text="Balance",font=("Times New Roman",15),background="#021B9A",foreground="white")
    Create_acc_Bal.place(x=50,y=210)
    CA_entry_5_PA=Entry(window1_frame2,bd=0,font=("kotha one",15))
    CA_entry_5_PA.place(x=350,y=210)

    def Button_for_PA():
        if not (CA_entry_5_PA.get() or CA_entry_4_PA.get() or CA_entry_3_PA.get() or CA_entry_2_PA.get() or CA_PA_entry_1.get()):
            messagebox.showerror("Error","Enter all the Fields.")
        else:
            conn = create_connection()
            if conn is None:
                return
            try:
                cursor = conn.cursor()
                User_ID_PA = 0
                cursor.execute("SELECT USER_ID FROM LOGIN WHERE USER_NAME = %s", (User_name_for_PA,))
                User_ID_PA=cursor.fetchone()
                cursor.execute("INSERT INTO ACCOUNT VALUES (%s,%s,%s,%s,%s,%s)",(int(CA_PA_entry_1.get()),User_ID_PA[0],CA_entry_2_PA.get(),CA_entry_3_PA.get(),CA_entry_4_PA.get(),CA_entry_5_PA.get()))
                conn.commit()
                messagebox.showinfo("Done","Account Created.")
                cursor.close()

            except Error as e:
                print(f"Error: {e}")
            window1.destroy()
            login()

    CA_PA_button=Button(window1_frame2,text="Create Account",fg="black",font=("calidri",10),bg='light blue',padx=10,pady=5,command=Button_for_PA,cursor="hand2")
    CA_PA_button.place(x=400,y=280)

    Create_acc=Label(window1_frame1,text="Create Account",font=("Times New Roman",25),background="blue",foreground="white")
    Create_acc.place(x=10.0,y=10.0)

    Create_acc_Name=Label(window1_frame1,text="Name",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_Name.place(x=50.0,y=70.0)
    CA_entry_1=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_1.place(x=350,y=70)

    Create_acc_UserName=Label(window1_frame1,text="User Name",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_UserName.place(x=50.0,y=105.0)
    CA_entry_2=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_2.place(x=350,y=105)

    Create_acc_Mail=Label(window1_frame1,text="Mail ID",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_Mail.place(x=50,y=140)
    CA_entry_3=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_3.place(x=350,y=140)

    Create_acc_PhoneNo=Label(window1_frame1,text="Phone Number",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_PhoneNo.place(x=50,y=175)
    CA_entry_4=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_4.place(x=350,y=175)

    Create_acc_Add=Label(window1_frame1,text="Address",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_Add.place(x=50,y=210)
    CA_entry_5=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_5.place(x=350,y=210)

    Create_acc_Passwd1=Label(window1_frame1,text="Password",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_Passwd1.place(x=50,y=245)
    CA_entry_6=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_6.place(x=350,y=245)

    Create_acc_Passwd2=Label(window1_frame1,text="Re Enter Password",font=("Times New Roman",15),background="blue",foreground="white")
    Create_acc_Passwd2.place(x=50,y=280)
    CA_entry_7=Entry(window1_frame1,bd=0,font=("kotha one",15))
    CA_entry_7.place(x=350,y=280)

    def FINAL_FN_FOR_BUT():
        global User_name_for_PA
        if not (CA_entry_6.get() or CA_entry_5.get() or CA_entry_4.get() or CA_entry_3.get() or CA_entry_2.get() or CA_entry_1.get()):
            messagebox.showerror("Error","Enter all the Fields.")
        else:
            if CA_entry_7.get() == CA_entry_6.get():
                User_name_for_PA=CA_entry_2.get()
                conn = create_connection()
                if conn is None:
                    return
                try:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO LOGIN (USER_NAME,NAME,MAIL_ID,PHONE_NO,ADDRESS,PASSWORD) VALUES (%s,%s,%s,%s,%s,%s)",(CA_entry_2.get(),CA_entry_1.get(),CA_entry_3.get(),int(CA_entry_4.get()),CA_entry_5.get(),CA_entry_6.get()))
                    conn.commit()
                    messagebox.showinfo("Done","Account Created.")
                    cursor.close()

                except Error as e:
                    print(f"Error: {e}")
                window1_frame1.destroy()
                window1_notebook.select(window1_frame2)
            else:
                messagebox.showerror("Error","Passwords doesn't match!\n Please retry.")

    CA_button=Button(window1_frame1,text="Create Account",fg="black",font=("calidri",10),bg='light blue',padx=10,pady=5,command=FINAL_FN_FOR_BUT,cursor="hand2")
    CA_button.place(x=400,y=320)

    window1.resizable(False, False)
    window1.mainloop()

def login():
    global window
    window = Tk()
    window.title("PSM BANK")
    window.geometry("750x400")
    window.configure(bg = "#021B9A")
    canvas = Canvas(window,bg = "#021B9A",height = 400,width = 750,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(50.0,35.0,346.0,345.0,fill="#CECBCB",outline="")
    canvas.create_text(175.0,50.0,anchor="nw",text="Login",fill="#000000",font=("Times New Roman", 20 * -1))

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(199.5,122.5,image=entry_image_1)

    entry_1 = Entry(bd=0,bg="#B6B5B5",fg="#000716",highlightthickness=0)
    entry_1.place(x=97.0,y=104.0,width=205.0,height=35.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(199.5,190.5,image=entry_image_2)

    entry_2 = Entry(bd=0,bg="#B6B5B5",fg="#000716",highlightthickness=0,show="*")
    entry_2.place(x=97.0,y=172.0,width=205.0,height=35.0)

    def For_Login():    
        conn = create_connection()
        if conn is None:
            return
        
        try:
            cursor = conn.cursor()
            global User_name_is
            User_name_is=entry_1.get()
            cursor.execute("SELECT * FROM LOGIN WHERE USER_NAME = '{}'".format(User_name_is))
            result=cursor.fetchall()
            if not result:
                messagebox.showwarning("ERROR","USERNAME DOESNT EXIST")
            else:
                if result[0][6] == entry_2.get():
                    messagebox.showinfo("login", "LOGIN SUCCESSFULL")
                    cursor.execute("SELECT A.ACCOUNT_NO FROM ACCOUNT A, LOGIN L WHERE A.USER_ID = L.USER_ID AND L.USER_NAME = %s", (User_name_is,))
                    global account_no_of_user , primary_acc_no
                    account_no_of_user = cursor.fetchall()
                    primary_acc_no = account_no_of_user[0]
                    HomePage()

                else:
                    messagebox.showwarning("ERROR","INCORRECT PASSWORD")
        except Error as e:
            print(f"Error: {e}")
        
    canvas.create_text(109.0,86.0,anchor="nw",text="Username",fill="#000000",font=("KottaOne Regular", 10 * -1))
    canvas.create_text(109.0,154.0,anchor="nw",text="Password",fill="#000000",font=("KottaOne Regular", 10 * -1))

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_Login = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=For_Login,relief="flat",cursor="hand2")
    button_Login.place(x=148.0,y=227.0,width=102.0,height=32.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=window.destroy,relief="flat",cursor="hand2")
    button_2.place(x=148.0,y=282.0,width=102.0,height=32.0)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(100.0,95.0,image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(100.0,163.0,image=image_image_2)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=Create_Account_Page,bg=window.cget("background"),relief=tk.FLAT,cursor="hand2")
    button_3.place(x=221.0,y=345.0,width=125.0,height=29.0)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(545.0,147.0,image=image_image_3)

    canvas.create_text(420.0,266.0,anchor="nw",text="PSM BANK",fill="#3752E1",font=("Times New Roman", 48 * -1))  #pora soodra mooskora bank
    canvas.create_text(60.0,349.0,anchor="nw",text="Don't have an account ?",fill="#FF1818",font=("KottaOne Regular", 14 * -1))

    window.resizable(False, False)
    window.mainloop()

def Back_Login():
    windowL.destroy()
    login()


account_no_of_user = [0]
primary_acc_no = 0
login()