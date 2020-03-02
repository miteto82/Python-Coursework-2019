from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3

Item4 = 0

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()


# main Class
class user:
    def __init__(self, master):
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome, " + self.username.get()
            self.head.configure(fg="black")
            self.head.pack(fill=X)
            application = travel(root)

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Already Taken!')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()

        # Frame Packing Methords

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2,
                                                                                                              column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


class travel:

    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System - Uber")
        self.root.geometry(geometry)

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref = StringVar()
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        journeyType = IntVar()
        carType = IntVar()

        varl1 = StringVar()
        varl2 = StringVar()
        varl3 = StringVar()
        reset_counter = 0

        Firstname = StringVar()
        Surname = StringVar()
        Mobile = StringVar()

        TaxiTax = StringVar()
        Km = StringVar()
        Luggage = StringVar()
        Receipt = StringVar()

        Standard = StringVar()
        Vip = StringVar()

        TaxiTax.set("0")
        Km.set("0")
        Luggage.set("0")

        Standard.set("0")
        Vip.set("0")

        # ==========================================Define Functiom==================================================

        def iExit():
            iExit = ms.askyesno("Prompt!", "Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            TaxiTax.set("0")
            Km.set("0")
            Luggage.set("0")

            Standard.set("0")
            Vip.set("0")

            Firstname.set("")
            Surname.set("")
            Mobile.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0", END)
            self.txtReceipt2.delete("1.0", END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            journeyType.set(0)
            carType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")

            self.cboPickup.current(0)
            self.cboDrop.current(0)

            self.txtTaxiTax.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)

            self.txtStandard.configure(state=DISABLED)
            self.txtVip.configure(state=DISABLED)
            self.reset_counter = 1

        def Receiptt():
            if reset_counter is 0 and Firstname.get() != "" and Surname.get() != "" and Mobile.get() != "" :
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                x = random.randint(10853, 500831)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END, "Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END, 'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END, 'Taxi No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END, 'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END, 'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END, 'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END, 'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END, 'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END, 'Standard:\n')
                self.txtReceipt2.insert(END, Standard.get() + "\n")
                self.txtReceipt1.insert(END, 'Vip:\n')
                self.txtReceipt2.insert(END, Vip.get() + "\n")
                self.txtReceipt1.insert(END, 'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END, 'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END, 'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))

            else:
                self.txtReceipt1.delete("1.0", END)
                self.txtReceipt2.delete("1.0", END)
                self.txtReceipt1.insert(END, "\nNo Input")

        def Taxi_Tax():
            global Item1
            if var1.get() == 1:
                self.txtTaxiTax.configure(state=NORMAL)
                Item1 = float(4)
                TaxiTax.set(str(Item1) + " лв")
            elif var1.get() == 0:
                self.txtTaxiTax.configure(state=DISABLED)
                TaxiTax.set("0")
                Item1 = 0

        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Burgas Free University":
                    switch = {"Jumbo": 10, "Metro": 8, "GaleriaMall": 3, "Burgas Free University": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Jumbo":
                    switch = {"Jumbo": 0, "Metro": 2, "GaleriaMall": 6, "Burgas Free University": 10}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Metro":
                    switch = {"Jumbo": 2, "Metro": 0, "GaleriaMall": 3, "Burgas Free University": 8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "GaleriaMall":
                    switch = {"Jumbo": 6, "Metro": 3, "GaleriaMall": 0, "Burgas Free University": 3}
                    Km.set(switch[varl2.get()])


        def Lug():
            global Item4
            if (var4.get() == 1):
                self.txtLuggage.configure(state=NORMAL)
                Item4 = float(5)
                Luggage.set(str(Item4) + " лв")
            elif var4.get() == 0:
                self.txtLuggage.configure(state=DISABLED)
                Luggage.set("0")
                Item4 = 0

        def selectCar():
            global Item5
            if carType.get() == 1:
                self.txtVip.configure(state=DISABLED)
                Vip.set("0")
                self.txtStandard.configure(state=NORMAL)
                Item5 = float(5)
                Standard.set(str(Item5) + " лв")
            elif carType.get() == 2:
                self.txtStandard.configure(state=DISABLED)
                Standard.set("0")
                self.txtVip.configure(state=NORMAL)
                Item5 = float(8)
                Vip.set(str(Item5) + " лв")

        def Total_Paid():
            if ((
                    var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and carType.get() != 0 and journeyType.get() != 0 and (
                    varl1.get() != "" and varl2.get() != "")):
                if journeyType.get() == 1:
                    Item2 = Km.get()
                    Cost_of_fare = ((float(Item2) * Item5))
                    Cost_details = Item1 + Item4

                    Tax = str('%.2f' % ((Cost_details)) + " лв")
                    ST = str('%.2f' % ((Cost_of_fare)) + " лв")
                    TT = str('%.2f' % (Cost_of_fare + ((Cost_details))) + " лв")
                elif journeyType.get() == 2:
                    Item2 = Km.get()
                    Cost_of_fare = ((float(Item2) * Item5) * 1.5)
                    Cost_details = Item1 + Item4

                    Tax = str('%.2f' % ((Cost_details)) + " лв")
                    ST = str('%.2f' % ((Cost_of_fare)) + " лв")
                    TT = str('%.2f' % (Cost_of_fare + ((Cost_details))) + " лв")
                else:
                    Item2 = Km.get()
                    Cost_of_fare = ((float(Item2) * Item5) * 2)
                    Cost_details = Item1 + Item4

                    Tax = str('%.2f' % ((Cost_details)) + " лв")
                    ST = str('%.2f' % ((Cost_of_fare)) + " лв")
                    TT = str('%.2f' % (Cost_of_fare + ((Cost_details))) + " лв")

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !", "Invalid Input\nPlease try again !!!")

        # ================================================mainframe========================================================================

        MainFrame = Frame(self.root)
        MainFrame.pack(fill=BOTH, expand=True)

        Tops = Frame(MainFrame, bd=20, width=1350, relief=RIDGE)
        Tops.pack(side=TOP, fill=BOTH, expand=True)

        self.lblTitle = Label(Tops, font=('arial', 70, 'bold'), text=" Taxi Booking System - Uber")
        self.lblTitle.grid()

        # ================================================customerframedetail=============================================================
        CustomerDetailsFrame = LabelFrame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        FrameDetails = Frame(CustomerDetailsFrame, width=880, height=400, bd=10, relief=RIDGE)
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)

        CustomerName = LabelFrame(FrameDetails, width=150, height=250, bd=10, font=('arial', 12, 'bold'),
                                  text="Customer Name", relief=RIDGE)
        CustomerName.grid(row=0, column=0)

        TravelFrame = LabelFrame(FrameDetails, bd=10, width=300, height=250, font=('arial', 12, 'bold'),
                                 text="Booking Detail", relief=RIDGE)
        TravelFrame.grid(row=0, column=1)

        Book_Frame = LabelFrame(FrameDetails, width=300, height=150, relief=FLAT)
        Book_Frame.grid(row=1, column=0)

        CostFrame = LabelFrame(FrameDetails, width=150, height=150, bd=5, relief=FLAT)
        CostFrame.grid(row=1, column=1)

        # ===============================================recipt======================================================================
        Receipt_BottonFrame = LabelFrame(CustomerDetailsFrame, bd=10, width=450, height=400, relief=RIDGE)
        Receipt_BottonFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        ReceiptFrame = LabelFrame(Receipt_BottonFrame, width=350, height=300, font=('arial', 12, 'bold'),
                                  text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0, column=0)

        ButtonFrame = LabelFrame(Receipt_BottonFrame, width=350, height=100, relief=RIDGE)
        ButtonFrame.grid(row=1, column=0)
        # =========================================================CustomerName====================================================

        self.lblFirstname = Label(CustomerName, font=('arial', 14, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Firstname, bd=7, insertwidth=2,
                                  justify=RIGHT)
        self.txtFirstname.grid(row=0, column=1)

        self.lblSurname = Label(CustomerName, font=('arial', 14, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=1, column=0, sticky=W)
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Surname, bd=7, insertwidth=2,
                                justify=RIGHT)
        self.txtSurname.grid(row=1, column=1, sticky=W)

        self.lblMobile = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Mobile, bd=7, insertwidth=2,
                               justify=RIGHT)
        self.txtMobile.grid(row=5, column=1)

        # ===============================================Taxi Information==============================================================
        self.lblPickup = Label(TravelFrame, font=('arial', 14, 'bold'), text="Pickup", bd=7)
        self.lblPickup.grid(row=0, column=0, sticky=W)

        self.cboPickup = ttk.Combobox(TravelFrame, textvariable=varl1, state='readonly', font=('arial', 20, 'bold'),
                                      width=14)
        self.cboPickup['value'] = ('', 'GaleriaMall', 'Metro', 'Jumbo', 'Burgas Free University')
        self.cboPickup.current(0)
        self.cboPickup.grid(row=0, column=1)

        self.lblDrop = Label(TravelFrame, font=('arial', 14, 'bold'), text="Drop", bd=7)
        self.lblDrop.grid(row=1, column=0, sticky=W)

        self.cboDrop = ttk.Combobox(TravelFrame, textvariable=varl2, state='readonly', font=('arial', 20, 'bold'),
                                    width=14)
        self.cboDrop['value'] = ('', 'Burgas Free University', 'Jumbo', 'Metro', 'GaleriaMall')
        self.cboDrop.current(0)
        self.cboDrop.grid(row=1, column=1)

        # ===============================================Taxi Information==============================================================

        self.chkTaxiTax = Checkbutton(TravelFrame, text="Base Charge Tax *", variable=var1, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), command=Taxi_Tax).grid(row=3, column=0, sticky=W)
        self.txtTaxiTax = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=TaxiTax, bd=6, width=18,
                                bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtTaxiTax.grid(row=3, column=1)

        self.chkKm = Checkbutton(TravelFrame, text="Distance *", variable=var2, onvalue=1, offvalue=0,
                                 font=('arial', 16, 'bold'), command=Kilo).grid(row=4, column=0, sticky=W)
        self.txtKm = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Km, bd=6, width=18, bg="white",
                           state=DISABLED, justify=RIGHT, relief=SUNKEN, highlightthickness=0)
        self.txtKm.grid(row=4, column=1)

        self.chkLuggage = Checkbutton(TravelFrame, text="Luggage", variable=var4, onvalue=1, offvalue=0,
                                      font=('arial', 16, 'bold'), command=Lug).grid(row=6, column=0, sticky=W)
        self.txtLuggage = Label(TravelFrame, font=('arial', 14, 'bold'), textvariable=Luggage, bd=6, width=18,
                                bg="white", state=DISABLED, justify=RIGHT, relief=SUNKEN)
        self.txtLuggage.grid(row=6, column=1)

        # =================================payment information ===========================================================================

        self.lblPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), text="Aditional Tax\t\t", bd=7)
        self.lblPaidTax.grid(row=0, column=2, sticky=W)
        self.txtPaidTax = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, width=26,
                                justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtPaidTax.grid(row=0, column=3)

        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="Distance Tax", bd=7)
        self.lblSubTotal.grid(row=1, column=2, sticky=W)
        self.txtSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7, width=26,
                                 justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtSubTotal.grid(row=1, column=3)

        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="Total Cost", bd=7)
        self.lblTotalCost.grid(row=2, column=2, sticky=W)
        self.txtTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, width=26,
                                  justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtTotalCost.grid(row=2, column=3)

        # ==========================================================taxiselect=======================================================================

        self.chkStandard = Radiobutton(Book_Frame, text="Standard", value=1, variable=carType,
                                       font=('arial', 14, 'bold'), command=selectCar).grid(row=0, column=0, sticky=W)
        self.txtStandard = Label(Book_Frame, font=('arial', 14, 'bold'), width=7, textvariable=Standard, bd=5,
                                 state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtStandard.grid(row=0, column=1)

        self.chkVip = Radiobutton(Book_Frame, text="Vip", value=2, variable=carType,
                                          font=('arial', 14, 'bold'), command=selectCar).grid(row=1, column=0, sticky=W)
        self.txtVip = Label(Book_Frame, font=('arial', 14, 'bold'), width=7, textvariable=Vip, bd=5,
                                   state=DISABLED, justify=RIGHT, bg="white", relief=SUNKEN)
        self.txtVip.grid(row=1, column=1)

        self.chkSingle = Radiobutton(Book_Frame, text="Single", value=1, variable=journeyType,
                                     font=('arial', 14, 'bold')).grid(row=0, column=2, sticky=W)
        self.chkReturn = Radiobutton(Book_Frame, text="Return", value=2, variable=journeyType,
                                     font=('arial', 14, 'bold')).grid(row=1, column=2, sticky=W)
        self.chkSpecialsNeeds = Radiobutton(Book_Frame, text="SpecialNeeds", value=3, variable=journeyType,
                                            font=('arial', 14, 'bold')).grid(row=2, column=2, sticky=W)

        # =======================================Recipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt1.grid(row=0, column=0, columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame, width=22, height=21, font=('arial', 10, 'bold'), borderwidth=0)
        self.txtReceipt2.grid(row=0, column=2, columnspan=2)

        # ======================================Button========================================================================================

        self.btnTotal = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Total',
                               command=Total_Paid).grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Receipt',
                                 command=Receiptt).grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Reset',
                               command=Reset).grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, padx=18, bd=7, font=('arial', 11, 'bold'), width=2, text='Exit',
                              command=iExit).grid(row=0, column=3)

    # ====================================================================================================================================


if __name__ == '__main__':
    root = Tk()

    # =========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry = "%dx%d+%d+%d" % (w, h, 0, 0)

    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()