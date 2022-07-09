class BankAccount():
    acc_balance = 500
    def __init__(self,pin):
        self.p = pin

    def deposit(self,pin,amount):
        if pin == self.p:
            BankAccount.acc_balance = BankAccount.acc_balance + amount
            print("you have deposited amount",amount,"rupees")
        else:
            print("you have entered the wrong pin")

    def withdraw(self,pin,amount):
        if pin == self.p:
            BankAccount.acc_balance = BankAccount.acc_balance - amount
            print("you have withdraw amount",amount,"rupees")
        else:
            print("you have entered the wrong pin")
    def get_balance(self,pin):
        if pin == self.p:
            print("your current bank account balance is",BankAccount.acc_balance)
        else:
            print("you have entered the wrong pin")
    def change_pin(self,oldpin,newpin):
        if oldpin == self.p:
            self.p = newpin
            print("your new pin is",newpin)
        else:
            print("enter the correct pin")

obj = BankAccount(4103)
obj.get_balance(4103)
obj.deposit(4103,500)
obj.get_balance(4103)
obj.withdraw(4103,500)
obj.get_balance(4103)
obj.change_pin(4103,1991)
obj.get_balance(1991)
