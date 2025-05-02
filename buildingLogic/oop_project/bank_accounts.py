class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,acctname):
        self.balance=initialAmount
        self.name=acctname
        print(f"\nAccount '{self.name}' created. \nBalance=${self.balance:.2f} ")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance is ${self.balance:.2f} ")

    def deposit(self,amount):
        self.balance+=amount
        print("\nDeposit successful.")
        self.getBalance()
    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"sorry,account '{self.name}' only has balance of ${self.balance:.2f} ")
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance-=amount
            print("\nWithdraw successful.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nwithdrawn interruppted:{error}")
    def transfer(self,amount,account):
        try:
            print("\n **************\n\n beginning transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer successful.")
        except BalanceException as error:
            print(f"\nTransfer interrupted:{error}")

class IntrestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance =self.balance + (amount * 1.05)
        print("\nDeposit successful.")
        self.getBalance()   

class savingsAcct(IntrestRewardAcct):
    def __init__(self,initialAmount,acctname):
        super().__init__(initialAmount,acctname)
        self.fee=5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance-=amount
            self.balance-=self.fee
            print("\nWithdraw successful.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nwithdrawn interruppted:{error}")