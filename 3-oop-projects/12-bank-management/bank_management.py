from abc import ABC, abstractclassmethod
from time import sleep


class Bank_account(ABC):
    accounts = []

    def __init__(self, name, email, password, address, ac_type):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.ac_type = ac_type
        self.balance = 0
        self.bank_balance = 1000000
        self.loan = 0
        self.total_bank_loan = 0
        self.account_no = self.name+'-'+str(len(self.address))
        self.transaction = []
        self.limit = 2
        Bank_account.accounts.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.bank_balance += amount
            self.balance += amount
            print("\nDepositing...Please wait...")
            sleep(1)
            print(
                f"\nDeposited ${amount} successfully!!!\nNew balance: ${self.balance}")
            trn = f"You have deposited ${amount}"
            self.transaction.append(trn)
        else:
            print("\nInvalid amount!")

    def withdraw(self, amount):
        if amount < 0:
            print("\nInvalid amount!\n")

        elif amount <= self.balance:
            if amount <= self.bank_balance:
                self.balance -= amount
                self.bank_balance -= amount
                print("\nWithdrawing.....Please wait....")
                sleep(1)
                print(
                    f"\nWithdrew ${amount} from your account successfully!\n New balance: ${self.balance}")
                trn = f"You have withdrawn ${amount}"
                self.transaction.append(trn)
            else:
                print("\nThe bank is bankrupt\n")
        else:
            print("\nWithdrawal amount exceeded\n")

    def take_loan(self, amount):

        if amount > self.bank_balance or self.limit == 0:
            print("Sorry, loan failed!\n")

        else:
            self.balance += amount
            self.loan += amount
            self.bank_balance -= amount
            self.total_bank_loan += amount
            trn = f"You have taken ${amount} loan"
            self.transaction.append(trn)
            print(f"You have taken ${amount} loan from the bank!\n")
            self.limit -= 1

    def transaction_complete(self):
        for t in self.transaction:
            print(t)

    def transfer_balance(self, user, amount):
        # print(Bank_account.accounts.name)
        if amount <= 0:
            print("Please enter a valid amount!")
        else:
            flag = 1
            for u in Bank_account.accounts:
                # print(u.name)
                if u.name == user:
                    if amount < self.balance:
                        u.balance += amount
                        self.balance -= amount
                        print(
                            f"\nTransferring ${amount} to {u.name} .... Please wait...")
                        sleep(1)
                        print(
                            f"Transferred ${amount} to {u.name} successfully!")
                        tr = f"Received ${amount} from {self.name}"
                        tr_self = f"Transferred ${amount} to {u.name}"
                        u.transaction.append(tr)
                        self.transaction.append(tr_self)
                        flag = 0
                        break
                    else:
                        print("You don't have enough balance!")
                        break
            if flag == 1:
                print("Account does not exist!\n")


class SavingsAccount(Bank_account):
    def __init__(self, name, email, password, address, ac_type, interest_rate):
        super().__init__(name, email, password, address, "savings")
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance*(self.interestRate/100)
        print(f"{self.interest_rate}% Interest has been applied!")
        self.deposit(interest)

    def showInfo(self):
        print(f'\n{"*"*70}\n')
        print(f"       Infos of {self.ac_type} account of {self.name}:\n")
        print(f'\n\tE-mail : {self.email}\t\tName : {self.name}')
        print(
            f'\n\tAccount Type : {self.ac_type}\t\tAccount No : {self.account_no}')

        print(
            f'\n\tCurrent Balance : {self.balance}\t\t Your loan: {self.loan}\n')
        print(f'{"*"*70}')


class CurrentAccount(Bank_account):
    def __init__(self, name, email, password, address, ac_type, limit):
        super().__init__(name, email, password, address, "current")
        self.limit = limit

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.limit:
            if amount <= self.bank_balance:
                self.balance -= amount
                print("\nWithdrawing.....Please wait....")
                sleep(1)
                print(
                    f"\nWithdrew ${amount} from your account successfully!\n New balance: ${self.balance}")
                trn = f"You have withdrawn ${amount}"
                self.transaction.append(trn)
            else:
                print("\nThe bank is bankrupt\n")
        else:
            print("\nInvalid withdrawal amount or overdraft limit reached\n")

    def transfer_balance(self, user, amount):
        if amount <= 0:
            print("Please enter a valid amount!")
        else:
            flag = 1
            for u in Bank_account.accounts:
                # print(u.name)
                if u.name == user:
                    if amount < self.balance and (self.balance - amount) >= self.limit:
                        u.balance += amount
                        self.balance -= amount
                        print(
                            f"\nTransferring ${amount} to {u.name} .... Please wait...")
                        sleep(1)
                        print(
                            f"Transferred ${amount} to {u.name} successfully!")
                        tr = f"Received ${amount} from {self.name}"
                        tr_self = f"Transferred ${amount} to {u.name}"
                        u.transaction.append(tr)
                        self.transaction.append(tr_self)
                        flag = 0
                        break
                    else:
                        print("You don't have enough balance!")
                        flag = 0
                        break
            if flag == 1:
                print("Account does not exist!\n")

    def showInfo(self):
        print(f'\n{"*"*70}\n')
        print(f"       Infos of {self.ac_type} account of {self.name}:\n")
        print(f'\n\tE-mail : {self.email}\t\tName : {self.name}')
        print(
            f'\n\tAccount Type : {self.ac_type}\t\tAccount No : {self.account_no}')

        print(
            f'\n\tCurrent Balance : {self.balance}\t\t Your loan: {self.loan}\n')
        print(f'{"*"*70}')


# System run from here
bank_user = None

while True:

    if bank_user is None:
        print("\n######## Please login/register to continue! ########")
        choice = input("\n>>> Register/ Login (R/L): ")
        if choice == "R":
            name = input("Your name: ")
            email = input("Your email: ")
            password = input("Your password: ")
            address = input("Your address: ")
            ac_type = input("Account type - savings/current (sv/cu): ")
            flag = 1
            for user in Bank_account.accounts:
                if user.name == name:
                    print("\nUser already exists!\n")
                    bank_user = None
                    flag = 0
                    break
            if flag == 0:
                continue
            if ac_type == "sv":
                ir = int(input("Interest rate: "))
                bank_user = SavingsAccount(
                    name, email, password, address, ac_type, ir)

            elif ac_type == "cu":
                lm = int(input("Overdraft Limit: "))
                bank_user = CurrentAccount(
                    name, email, password, address, ac_type, lm)
            else:
                print("\nPlease select a valid account type!\n")

        elif choice == "L":
            user_name = input("User Name: ")
            password = input("Your password: ")
            if user_name == "admin" and password == "123":
                pass
            else:
                for user in Bank_account.accounts:
                    # print(user.name, user.password)
                    if user.name == user_name and user.password == password:
                        bank_user = user
                        break
        else:
            print("\nYou need to login/register to access to the bank\n")

    else:
        print(f"\n### Welcome to Bangla Bank {bank_user.name}! ###\n")

        if bank_user.ac_type == "savings":
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Account Details")
            print("4. Take loan from Bank")
            print("5. Your all transactions")
            print("6. Transfer balance")
            print("7. Log out")

            print("\n")
            choice = int(input("Choose option: "))

            if choice == 1:
                amount = int(input("Deposit amount: "))
                bank_user.deposit(amount)

            elif choice == 2:
                amount = int(input("Withdraw amount: "))
                bank_user.withdraw(amount)

            elif choice == 3:
                bank_user.showInfo()

            elif choice == 4:
                amount = int(input("Loan amount: "))
                bank_user.take_loan(amount)
                bank_user.limit -= 1

            elif choice == 5:
                bank_user.transaction_complete()

            elif choice == 6:
                user = input("Type username to transfer balance: ")
                amount = int(input("Amount: "))
                bank_user.transfer_balance(user, amount)

            elif choice == 7:
                print("\nLogging out...Please wait...")
                sleep(1)
                print(f"Have a good day {bank_user.name}!")
                sleep(1)
                print("\nLogged out successfully!")
                bank_user = None

        else:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Account Details")
            print("4. Take loan from Bank")
            print("5. Your all transactions")
            print("6. Transfer balance")
            print("7. Log out")

            print("\n")
            choice = int(input("Choose option: "))

            if choice == 1:
                amount = int(input("Deposit amount: "))
                bank_user.deposit(amount)

            elif choice == 2:
                amount = int(input("Withdraw amount: "))
                bank_user.withdraw(amount)

            elif choice == 3:
                bank_user.showInfo()

            elif choice == 4:
                amount = int(input("Loan amount: "))
                bank_user.take_loan(amount)
                bank_user.limit -= 1

            elif choice == 5:
                bank_user.transaction_complete()

            elif choice == 6:
                user = input("Type username to transfer balance: ")
                amount = int(input("Amount: "))
                bank_user.transfer_balance(user, amount)

            elif choice == 7:
                print("\nLogging out...Please wait...")
                sleep(1)
                print(f"Have a good day {bank_user.name}!")
                sleep(1)
                print("\nLogged out successfully!")
                bank_user = None
