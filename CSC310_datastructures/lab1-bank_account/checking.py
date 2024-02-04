from account import Account
# checkings account inherits the properties of Account
class Checking(Account):
    # super name, balance, and password for the Account class, 
    # and add a daily limit to the checking account. With a default of $2500
    def __init__(self, name, balance, password, dailyLimit=2500):
        super().__init__(name, balance, password)
        self.dailyLimit = 2500

    # function to change the daily amount you can withdraw
    def setDailyLimit(self):
        dailyLimit = ""
        while not dailyLimit.isnumeric and 100 < float(dailyLimit) < 1_000_000:
            dailyLimit = input("What do you want to set your daily limit to (100-1,000,000): ")
        
        self.dailyLimit = float(dailyLimit)
    
    # shows info about the account
    def showInfo(self):
        print("")
        print("     Account Type: Checking")
        print("     Name:", self.name)
        print("     Balance:", self.balance)
        print("     Password:", self.password)
        print("     Daily Limit:", self.dailyLimit)
        print("")