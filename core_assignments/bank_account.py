class BankAccount:

    # class attribute
    account_list = []

    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_list.append(self)

    # increases the account balance by the given amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your current balance after deposit is ${self.balance}")
        else:
            print("You can't deposit a negative amount")
        return self

    # decreases the account balance by the given amount if there are sufficient funds
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Your current balance after withdrawal is ${self.balance}")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(f"After deduction your current balance is ${self.balance}")
        return self

    # print to the console
    def display_account_info(self):
        print(f"Balance: ${self.balance}\nInterest Rate: {self.int_rate * 100}%")
        return self

    # increases the account balance by the current balance * the interest rate
    # (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f"Your current balance after yield interest is ${self.balance}")
        else:
            print(f"your current balance is {self.balance} interest rate is not applied")
        return self
    
    # print all instances of a Bank Account's info using a classmethod
    @classmethod
    def get_all_accounts(cls):
        for accounts in cls.account_list:
            accounts.display_account_info()

    # @staticmethod
    # def can_withdraw(amount, balance)

account_1 = BankAccount(0.07, 100)
account_2 = BankAccount(0.03)

account_1.deposit(20).deposit(100).deposit(80).withdraw(50).yield_interest().display_account_info()

account_2.deposit(1000).deposit(-50).withdraw(200).withdraw(250).withdraw(300).withdraw(500).yield_interest().display_account_info()

BankAccount.get_all_accounts()

