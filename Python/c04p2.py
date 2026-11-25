class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be greater than 0.")
        else:
            self.balance += amount
            print("Deposited:", amount)
            print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current balance:", self.balance)

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number :", self.account_number)
        print("Name           :", self.name)
        print("Account Type   :", self.account_type)
        print("Balance        :", self.balance)


acc = BankAccount(101001, "Anil Kumar", "Savings", 5000)

acc.display()
acc.deposit(2000)
acc.withdraw(1500)
acc.withdraw(10000)      
acc.display()
