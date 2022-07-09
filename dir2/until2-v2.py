class BankAccount():
    condition = True

    acc_balance = 500
    def __init__(self,pin):
        self.p = pin

    def __deposit(self,pin,amount):
        if pin == self.p:
            BankAccount.acc_balance = BankAccount.acc_balance + amount
            print("you have deposited amount",amount,"rupees")
        else:
            print("you have entered the wrong pin")

    def __withdraw(self,pin,amount):
        if pin == self.p:
            BankAccount.acc_balance = BankAccount.acc_balance - amount
            print("you have withdraw amount",amount,"rupees")
        else:
            print("you have entered the wrong pin")
    def __get_balance(self,pin):
        if pin == self.p:
            print("your current bank account balance is",BankAccount.acc_balance)
        else:
            print("you have entered the wrong pin")
    def __change_pin(self,oldpin,newpin):
        if oldpin == self.p:
            self.p = newpin
            print("your new pin is",newpin)
        else:
            print("enter the correct pin")

    def access(self):
        while BankAccount.condition == True:
            inp = int(input("select one of the options: \n\n 1. withdraw amount \n 2. deposit amount \n 3. get bank balance \n "
                           "4. change pin \n 5. quit \n // "))
            if inp == 1:
                p = int(input("Enter the pin : "))
                amt = int(input("Enter the amount : "))
                BankAccount.__withdraw(self,p,amt)
            elif inp == 2:
                p = int(input("Enter the pin : "))
                amt = int(input("Enter the amount : "))
                BankAccount.__deposit(self,p,amt)
            elif inp == 3:
                p = int(input("Enter the pin : "))
                BankAccount.__get_balance(self,p)
            elif inp == 4:
                p = int(input("Enter the old pin : "))
                np = int(input("Enter the new pin : "))
                BankAccount.__change_pin(self,p,np)
            elif inp == 5:
                BankAccount.condition = False
            else:
                print("please select a valid option")

obj = BankAccount(4103)
obj.access()