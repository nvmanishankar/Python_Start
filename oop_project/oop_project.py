from bank_accounts import *

Mani= BankAccount(1000,"Mani")
sara=BankAccount( 2000,"Sara")

Mani.getBalance()
sara.getBalance()

sara.deposit(500)

Mani.withdraw(2000)

Mani.withdraw(50)

Mani.getBalance()

Mani.transfer(100,sara)

jim=IntrestRewardAcct(1000,"Jim")
jim.getBalance()
jim.deposit(100)
jim.transfer(100,Mani)

blaze=savingsAcct(1000,"Blaze")
blaze.getBalance()
blaze.deposit(100)
blaze.withdraw(100)
blaze.transfer(100,Mani)
blaze.getBalance()
