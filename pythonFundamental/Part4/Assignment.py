# Answer 1----------------------------------------

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("amount withdrawn successfully")
        else:
            print("insufficient balance")

    def check_balance(self):
        print(f"your current bank balance is {self.balance}")

acc1 = BankAccount("11122", "Samay", 50_000)
acc1.deposit(10_000)
acc1.withdraw(20_000)
acc1.check_balance()

