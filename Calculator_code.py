#import libraries

from tkinter import *
import tkinter.messagebox
from tkinter import ttk


class RepaymentCalculation:

    def __init__(self, root):
        self.root = root
        self.root.title("Loan Repayment Calculator", )
        self.root.configure(background="cyan3")
        self.root.geometry("1366x768+0+0")

        # ==============================        Variables        =========================================================
        ui_pricipalamount = StringVar()
        ui_interestrate = StringVar()
        ui_loanperiod = StringVar()
        ui_periodvalue = StringVar()

        PaymentAmount = []
        PrincipalAmount = []
        InterestAmount = []
        BalanceAmount = []
        PaymentNumber = []

        # ==============================        Functions       =========================================================

        def reset():

            ui_pricipalamount.set("")
            ui_interestrate.set("")
            ui_loanperiod.set("")
            ui_periodvalue.set("")
            PaymentAmount.clear()
            PrincipalAmount.clear()
            InterestAmount.clear()
            BalanceAmount.clear()
            PaymentNumber.clear()
            tree.delete(*tree.get_children())
            tree.pack_forget()
            BottomFrame.grid_forget()
            self.CalculateButton.config(state=NORMAL)
            self.LoanPeriodChoiceMonths.select()
            self.LoanPeriodChoiceYears.deselect()

        def pageexit():
            pageexit = tkinter.messagebox.askyesno("Confirm Exit", "Do you want to Exit the process(Y/N)")
            if pageexit > 0:
                root.destroy()
                return

        def paymentcalculation():

            BottomFrame.grid()
            tree.delete(*tree.get_children())
            tree.pack_forget()
            tree.pack()
            tree.pack(side=LEFT)
            scroll.pack(side='right', fill='y')
            self.CalculateButton.config(state=DISABLED)

            print(ui_periodvalue.get())

            iLoanAmount = float(ui_pricipalamount.get())
            iInterestRate = float(ui_interestrate.get())
            mInterestRate = round(iInterestRate / 1200, 3)

            if ui_periodvalue.get() == "M":
                iLoanPeriod = int(ui_loanperiod.get())
            else:
                iLoanPeriod = int(ui_loanperiod.get()) * 12

            for i in range(1, iLoanPeriod + 1):

                iPayment = ((iLoanAmount * mInterestRate) * ((1 + mInterestRate) ** iLoanPeriod)) / (
                        ((1 + mInterestRate) ** iLoanPeriod) - 1)
                Payment = round(iPayment,2)
                PrincipalPortion = round(Payment / ((1 + mInterestRate) ** (1 + iLoanPeriod - i)), 2)
                Interest = round((Payment - PrincipalPortion), 2)
                OutstandingBalance = round(((Interest / mInterestRate) - PrincipalPortion), 2)

                if OutstandingBalance < 0:
                    OutstandingBalance = 0
                PaymentNumber.append(i)
                PaymentAmount.append(Payment)
                PrincipalAmount.append(PrincipalPortion)
                InterestAmount.append(Interest)
                BalanceAmount.append(OutstandingBalance)

            for i in range(iLoanPeriod):
                tree.insert('', 'end',
                            values=(PaymentNumber[i], PaymentAmount[i], PrincipalAmount[i], InterestAmount[i], BalanceAmount[i]))


        # ==============================        Main Frames        =========================================================

        TopFrame = Frame(self.root, bd=5, height=300, width=1360, padx=250, pady=10, relief=RIDGE, bg="LightBlue1")
        TopFrame.grid()

        LeftFrame = Frame(TopFrame, bd=5, height=300, width=800, padx=10, pady=10, relief=RIDGE, bg="white")
        LeftFrame.pack(side=LEFT)

        LeftFrameHeader = Frame(LeftFrame, bd=5, height=100, width=750, padx=10, pady=10, relief=RIDGE, bg="SkyBlue")
        LeftFrameHeader.grid(row=0, column=0)

        LeftFrameValueReader = Frame(LeftFrame, bd=5, height=100, width=750, padx=10, pady=10, relief=RIDGE,
                                     bg="SkyBlue")
        LeftFrameValueReader.grid(row=3, column=0)

        RightFrame = Frame(TopFrame, bd=5, height=300, width=560, padx=10, pady=10, relief=RIDGE, bg="white")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(self.root, bd=5, height=160, width=1360, padx=250, pady=10, relief=RIDGE, bg="LightBlue1")
        #

        # ==============================        Table        =========================================================

        tree = ttk.Treeview(BottomFrame, columns=(1, 2, 3, 4,5), height=6, show="headings")
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('arial', 10, 'bold'))
        style.configure("Treeview", font=('arial', 8, 'bold'))

        tree.heading(1, text="Payment No.")
        tree.heading(2, text="Payment Amount")
        tree.heading(3, text="Principal Amount Paid")
        tree.heading(4, text="Interest Amount Paid")
        tree.heading(5, text="Loan Outstanding Balance")

        tree.column(1, width=100, anchor="center")
        tree.column(2, width=150, anchor="center")
        tree.column(3, width=150, anchor="center")
        tree.column(4, width=150, anchor="center")
        tree.column(5, width=200, anchor="center")

        scroll = ttk.Scrollbar(BottomFrame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)

        # ==============================        Input Readers        ==================================================

        self.Titlelabel = Label(LeftFrameHeader, text="LOAN REPAYMENT CALCULATOR", padx=54, pady=10, bd=4, justify=LEFT,
                                font=('arial', 20, 'bold'), bg="SkyBlue")
        self.Titlelabel.pack()

        self.PrincipalLabel = Label(LeftFrameValueReader, text="Please enter the Loan Amount : ", padx=10, pady=10, bd=4,
                                    justify=LEFT,
                                    font=('arial', 10, 'bold'), bg="SkyBlue")
        self.PrincipalLabel.grid(row=0, column=0, padx=10, pady=10)

        self.PrincipalEntry = Entry(LeftFrameValueReader, textvariable=ui_pricipalamount, font=('arial', 10, 'bold'),
                                    bd=4, justify=LEFT)
        self.PrincipalEntry.grid(row=0, column=1, padx=10, pady=10)

        self.InterestLabel = Label(LeftFrameValueReader, text="Please enter the Interest Rate % : ", padx=10, pady=10,
                                   bd=4,
                                   justify=LEFT, font=('arial', 10, 'bold'), bg="SkyBlue")
        self.InterestLabel.grid(row=1, column=0, padx=10, pady=10)

        self.InterestEntry = Entry(LeftFrameValueReader, textvariable=ui_interestrate, font=('arial', 10, 'bold'),
                                   bd=4, justify=LEFT)
        self.InterestEntry.grid(row=1, column=1, padx=10, pady=10)

        self.LoanPeriodLabel = Label(LeftFrameValueReader, text="Please enter the Loan Period : ", padx=10,
                                     pady=10,
                                     bd=4,
                                     justify=LEFT, font=('arial', 10, 'bold'), bg="SkyBlue")
        self.LoanPeriodLabel.grid(row=2, column=0, padx=10, pady=10)

        self.LoanPeriodEntry = Entry(LeftFrameValueReader, textvariable=ui_loanperiod, font=('arial', 10, 'bold'),
                                     bd=4, justify=LEFT)
        self.LoanPeriodEntry.grid(row=2, column=1, padx=10, pady=10)

        self.LoanPeriodChoiceMonths = Radiobutton(LeftFrameValueReader, text="Months", justify=CENTER,
                                                  variable=ui_periodvalue, value="M", font=('arial', 10, 'bold'),
                                                  bg="SkyBlue")
        self.LoanPeriodChoiceMonths.grid(row=2, column=2)

        self.LoanPeriodChoiceYears = Radiobutton(LeftFrameValueReader, text="Years", justify=CENTER,
                                                 variable=ui_periodvalue, value="Y", font=('arial', 10, 'bold'),
                                                 bg="SkyBlue")
        self.LoanPeriodChoiceYears.grid(row=2, column=3)

        self.LoanPeriodChoiceMonths.select()
        self.LoanPeriodChoiceYears.deselect()



        # ==============================        Buttons        =========================================================

        self.CalculateButton = Button(RightFrame, text="Calculate", padx=9, pady=10, bd=4,
                                      justify=CENTER,
                                      font=('arial', 10, 'bold'), bg="SkyBlue", relief=RAISED,
                                      command=paymentcalculation)
        self.CalculateButton.grid(row=0, column=0, padx=10, pady=10)


        self.ResetButton = Button(RightFrame, text="Reset", padx=19, pady=10, bd=4,
                                  justify=CENTER,
                                  font=('arial', 10, 'bold'), bg="SkyBlue", relief=RAISED, command=reset)
        self.ResetButton.grid(row=1, column=0, padx=10, pady=10)

        self.ExitButton = Button(RightFrame, text="Exit", padx=24, pady=10, bd=4,
                                 justify=CENTER,
                                 font=('arial', 10, 'bold'), bg="SkyBlue", relief=RAISED, command=pageexit)
        self.ExitButton.grid(row=2, column=0, padx=10, pady=10)


if __name__ == '__main__':
    root = Tk()
    application = RepaymentCalculation(root)
    root.mainloop()

