class Account:
    # initialize account object with name, balance, and password
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
     
    # when depositing check if password is correct, and if the amount to deposit is a positive number.
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry incorrect password")
            return 
        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return
        self.balance += amountToDeposit
        return self.balance
    
    # when withdrawing check if password is correct, and if the amount to withdraw is a 
    # positive number smaller than the current account balance
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Sorry incorrect password")
            return 
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return
        if amountToWithdraw > self.balance:
            print("You cannot withdraw a negative amount")
        self.balance -= amountToWithdraw
        return self.balance
    
    # If the password is correct it returns the accoun balance.
    def getBalance(self, password):
        if password != self.password:
            print("Sorry incorrect password")
            return 
        return self.balance