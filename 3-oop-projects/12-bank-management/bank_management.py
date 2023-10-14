from time import sleep


class Bank_account():
    accounts = []

    def __init__(self, name, email, password, address, ac_type):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.ac_type = ac_type
        self.balance = 0
        self.bank_balance = 1000000
        self.loan_condition = True
        self.loan = 0
        self.total_bank_loan = 0
        self.account_no = self.name+'-'+str(len(self.name))
        self.transaction = []
        self.limit = []
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
                    f"\nWithdrew ${amount} from your account successfully!\nNew balance: ${self.balance}")
                trn = f"You have withdrawn ${amount}"
                self.transaction.append(trn)
            else:
                print("\nThe bank is bankrupt\n")
        else:
            print("\nWithdrawal amount exceeded\n")

    def take_loan(self, amount):
        if amount > self.bank_balance or len(self.limit) >= 2:
            if amount > self.bank_balance:
                print("Sorry, loan failed!\n")
            else:
                print("You can take loan maximum 2 times!\n")

        else:
            self.balance += amount
            self.loan += amount
            self.bank_balance -= amount
            self.total_bank_loan += amount
            trn = f"You have taken ${amount} loan from the bank!"
            self.transaction.append(trn)
            print(trn)
            self.limit.append(trn)
            # print(len(self.limit))

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
                        flag = 0
                        break
            if flag == 1:
                print("Account does not exist!\n")


class AdminAccount(Bank_account):
    def __init__(self, name, email, password, address, ac_type):
        super().__init__(name, email, password, address, "admin")

    def show_admin_panel(self):
        print(f'\n{"*"*70}\n')
        print(f" >>>    Infos of Bangla Bank\n")
        print(
            f'\n\tTotal Bank balance : {self.cur_bank_balance()}\t\tTotal Bank Loan : {self.cur_bank_loan()}\n')

        total_user = 0

        counter = 0
        for user in Bank_account.accounts:
            # print(user.name)
            if user.name == 'admin':
                # print("Found")
                counter += 1

        total_user = len(Bank_account.accounts)-counter
        print(
            f'\n\tTotal User : {total_user}\\n')

        print(f'{"*"*70}')

    def loan_feature(self):
        status = None
        for user in SavingsAccount.accounts:
            if user.loan_condition == True:
                status = "Active"
                break
            else:
                status = "Disabled"
                break
        print(f"Current Bank loan status is {status}")
        # print(self.loan_condition)

        if status == "Active":
            ch = input(
                "\nDo you want to turn off loan feature for all users? (Y/N): ")

            if (ch == "Y"):
                for user in Bank_account.accounts:
                    if user.loan_condition == True:
                        user.loan_condition = False

                print("\nPlease wait...processing...")
                sleep(1)
                print("\nLoan feature is turned off now!")
                status = "Disabled"
            else:
                print(f"\nCurrent Bank loan status is {status}\n")
        else:
            ch = input(
                "\nDo you want to turn on loan feature for all users? (Y/N): ")

            if (ch == "Y"):
                for user in Bank_account.accounts:
                    if user.loan_condition == False:
                        user.loan_condition = True

                print("\nPlease wait...processing...")
                sleep(1)
                print("\nLoan feature is turned on now!")
                status = "Active"
            else:
                print(f"\nCurrent Bank loan status is {status}\n")

    def remove_account(self, name):
        flag = 1
        if name == "admin":
            print("\nCan't remove admin!\n")
        else:
            for user in Bank_account.accounts:
                if user.name == name:
                    Bank_account.accounts.remove(user)
                    print(f"Deleted account of {name}")
                    flag = 0
                    break
            if flag == 1:
                print("\nNo such user exists!\n")

    def cur_bank_balance(self):
        l = self.bank_balance
        for user in Bank_account.accounts:
            # print("getting user")
            l += user.balance
            l -= user.loan
        return l

    def cur_bank_loan(self):
        b = self.total_bank_loan
        for user in Bank_account.accounts:
            # print("getting user")
            b += user.loan
        return b

    @staticmethod
    def all_accounts():
        number = 1
        if len(Bank_account.accounts) != 0:
            print("\n*** All Bank account holder info's *** \n")
        else:
            print("\n*** No users exist!\n")
        for user in Bank_account.accounts:
            if user.name != "admin":
                print(
                    f"{number} -> Username: {user.name}\tUser email: {user.email}\tUser Balance: {user.balance}\tUser Loan: {user.loan}\tUser account type: {user.ac_type}\tUser Address: {user.address}\nLoan condition: {user.loan_condition}\n")
                number += 1


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
    def __init__(self, name, email, password, address, ac_type, lim):
        super().__init__(name, email, password, address, "current")
        self.lim = lim
        for user in Bank_account.accounts:
            self.bank_balance += user.balance
            self.bank_balance -= user.loan

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


SavingsAccount('Sawon', 'mmrsawon@gmail.com', 'asd',
               'Natore, Rajshahi', 'savings', 8)
SavingsAccount('Sumon', 'sumon@gmail.com', 'a',
               'Kolkata, India', 'savings', 7)
SavingsAccount('Gopi', 'gopu@gmail.com', 'asd',
               'Dhaka, Rajshahi', 'savings', 9)
SavingsAccount('Zim', 'zim@gmail.com', 'asd',
               'Bogra, Rajshahi', 'savings', 2)
CurrentAccount('Shokal', 'sokal@gmail.com', 'asd',
               'Rangpur', 'current', 2000)
CurrentAccount('Zillur', 'zillur@gmail.com', 'asd',
               'Naogaon, Rajshahi', 'current', 4000)

# System run from here
bank_user = None

while True:

    if bank_user is None:
        print("\n######## Please login/register to continue! ########")

        print("\nPRESS 'X' TO EXIT!")
        choice = input("\n>>> Register/ Login (R/L): ")
        print("\n")
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
                print("\nPlease  wait...processing...")
                sleep(1)
                print(f"\nLogged in successfully to {name} account!\n")
                bank_user = SavingsAccount(
                    name, email, password, address, ac_type, ir)

            elif ac_type == "cu":
                lm = int(input("Overdraft Limit: "))
                print("\nPlease  wait...processing...")
                sleep(1)
                print(f"\nLogged in successfully to {name} account!\n")
                bank_user = CurrentAccount(
                    name, email, password, address, ac_type, lm)
            else:
                print("\nPlease select a valid account type!\n")

        elif choice == "L":
            user_name = input("User Name: ")
            password = input("Your password: ")
            if user_name == "admin" and password == "123":
                print("\nPlease  wait...Admin login processing...")
                sleep(1)
                print(
                    f"\nLogged in successfully to {user_name} account!\n\n\n")
                print("\nWelcome, MR Mighty Admin!\n")
                bank_user = AdminAccount(
                    "admin", "admin@banglabank.com", "123", "Gulshan, Dhaka", "admin")
                # bank_user.show_admin_panel()
            else:
                flag = 1
                for user in Bank_account.accounts:
                    # print(user.name, user.password)
                    if user.name == user_name and user.password == password:
                        bank_user = user
                        flag = 0
                        print(
                            f"Logging in to {user.name}'s account...Please wait...\n")
                        sleep(1)
                        print("Log in successful!\n")
                        break
                if flag == 1:
                    print("\nNo user found!\n")
        elif choice == 'X' or choice == 'x':
            print(f"Exiting Bank...Please wait...\n")
            sleep(1)
            print(
                "Exited successful!\nHave a nice day and remember to payback your loans!\n")
            break
        else:
            print("\nYou need to login/register to access to the bank\n")

    elif bank_user.ac_type == 'savings' or bank_user.ac_type == 'current':
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
                # print(bank_user.loan_condition)
                if bank_user.loan_condition == True:
                    amount = int(input("Loan amount: "))
                    bank_user.take_loan(amount)
                else:
                    print("\nPlease  wait...processing...")
                    sleep(1)
                    print("\nSorry you can't take any loan right now!\n")

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
                if bank_user.loan_condition == True:
                    amount = int(input("Loan amount: "))
                    bank_user.take_loan(amount)
                else:
                    print("\nPlease  wait...processing...")
                    sleep(1)
                    print("\nSorry you can't take any loan right now!\n")

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

    # Admin panel
    elif bank_user.ac_type == 'admin':
        bank_user.show_admin_panel()
        print(f"\n\n\t\t ############ Admin Panel ############\n")
        print(" \t\t1. Create a new account")
        print(" \t\t2. Delete user account")
        print(" \t\t3. See all user list")
        print(" \t\t4. Total bank balance")
        print(" \t\t5. Total loan")
        print(" \t\t6. Turn on/ off loan feature")
        print(" \t\t7. Add interest to savings account")
        print(" \t\t8. Log out")

        print("\n")
        choice = int(input("Choose option: "))
        print("\n")
        if choice == 1:
            name = input("User name: ")
            email = input("User email: ")
            password = input("User password: ")
            address = input("User address: ")
            ac_type = input("Account type - savings/current (sv/cu): ")
            flag = 1
            for user in Bank_account.accounts:
                if user.name == name:
                    print("\nPlease  wait...processing...")
                    sleep(1)
                    print("\nUser already exists!\n")
                    bank_user = None
                    flag = 0
                    break
            if flag == 0:
                continue
            if ac_type == "sv":
                ir = int(input("Interest rate: "))
                SavingsAccount(
                    name, email, password, address, ac_type, ir)
                print("\nPlease  wait...processing...")
                sleep(1)
                print(f"\nAccount created for {name} successfully!\n")

            elif ac_type == "cu":
                lm = int(input("Overdraft Limit: "))
                CurrentAccount(
                    name, email, password, address, ac_type, lm)
                print("\nPlease  wait...processing...")
                sleep(1)
                print(f"\nAccount created for {name} successfully!\n")
            else:
                print("\nPlease select a valid account type!\n")

        elif choice == 2:
            name = input("Account name, you want to delete: ")
            bank_user.remove_account(name)

        elif choice == 3:
            bank_user.all_accounts()

        elif choice == 4:
            # b = bank_user.bank_balance
            # for user in Bank_account.accounts:
            #     b += user.balance

            # for user in Bank_account.accounts:
            #     b -= user.loan
            # AdminAccount.bank_balance = b
            # print(f"Current Bank Balance: $ {b}")
            print(f'\nBank balance: ${bank_user.cur_bank_balance()}\n')

        elif choice == 5:
            # b = bank_user.total_bank_loan
            # for user in Bank_account.accounts:
            #     b += user.loan
            # AdminAccount.total_bank_loan = b
            # print(f"Current Bank Loan: $ {b}")
            print(f"\nTotal Bank Loan: ${bank_user.cur_bank_loan()}\n")

        elif choice == 6:
            bank_user.loan_feature()

        elif choice == 7:
            for user in Bank_account.accounts:
                # print('cheese')
                # print(user)
                # print(user.ac_type)
                if user.ac_type == "savings":
                    if user.balance == 0:
                        print(f"\n{user.name}'s balance is currently 0!\n")
                        continue
                    b = user.balance*(user.interest_rate/100)
                    user.balance = b+user.balance
                    trn = f"${b} interest has been added to your account.\nYor current interest rate: ${user.interest_rate}"
                    user.transaction.append(trn)
                    print(
                        f"\n${b} interest has been added to account {user.name}\n")

        elif choice == 8:
            print("\nLogging out...Please wait...")
            sleep(1)
            print(f"Have a good day {bank_user.name}!")
            sleep(1)
            print("\nLogged out successfully!")
            bank_user = None
