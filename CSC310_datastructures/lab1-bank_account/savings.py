from account import Account
# savings account inherits the properties of Account
class Savings(Account):
    # super name, balance, and password for the Account class, 
    # and add interest rate with a default value of 4.5%
    def __init__(self, name, balance, password, interestRate=0.045):
        super().__init__(name, balance, password)
        self.interestRate = interestRate

    # Adds the interest to the bank account balance
    def addInterest(self):
        self.balance += self.balance * self.interestRate

    # shows info about the account
    def showInfo(self):
        print("")
        print("     Account Type: Savings")
        print("     Name:", self.name)
        print("     Balance:", self.balance)
        print("     Password:", self.password)
        print("     Interest Rate:", self.interestRate)
        print("")