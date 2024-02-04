from savings import Savings
from checking import Checking

if __name__ == "__main__":
    # create new acccount variable
    newAccount = None
    # Get name
    name = input("What is your name: ")

    # Ask for account type in loop until a correct option is chosen
    accountType = ""
    while accountType not in ["c", "s"]:
        accountType = input(f"Hey {name}, do you want a Checkings (C) or Savings (S) account: ").lower()

    # Ask for balance in loop until balance is a positive number
    balance = "-1"
    while not balance.isnumeric() and not float(balance) > 0:
        balance = input("What is your accounts balance (number): ")

    # Ask for password until it is at least 7 charachters long
    password = ""
    while len(password) < 7: 
        password = input("Give a password of at least 7 charachters: ")

    # Create checkings, or savings account depending on users choice
    if accountType == "s":
        newAccount = Savings(name, float(balance), password)
    if accountType == "c":
        newAccount = Checking(name, float(balance), password)

    # withdrawing money, depositing money, and showing info
    print("$ After withdrawing half the balance:", newAccount.withdraw(float(balance)//2, password))
    print("$ After depositing 1000:", newAccount.deposit(1000, password))
    newAccount.showInfo()