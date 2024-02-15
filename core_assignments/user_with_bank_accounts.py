class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.bank_account = {
                            "checking": BankAccount(int_rate=0.07, balance=500),
                            "savings": BankAccount(int_rate=0.07, balance=500)
                            }
    
    # prints out all of the attributes of the instance
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")
        return self
    
    # checks instance to see if they are a member and if not changes status to True
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} {self.last_name} is already a member")
        else:
            print(f"Welcome, new member {self.first_name} {self.last_name}!")
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    # deducts the amount from instance's current gold card points and checks to see if they have enough
    def spend_points(self, amount):
        if self.is_rewards_member == False:
            print("Not a member!")
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            print(f"you spent {amount} points, you now have {self.gold_card_points} points")
        else:
            print(f"Not enough points, you currently have {self.gold_card_points} points")
        return self

    # increases the account balance by the given amount
    # def deposit(self, amount):
    #     if amount > 0:
    #         self.bank_account.balance += amount
    #         print(f"Your current balance after deposit is ${self.bank_account.balance}")
    #     else:
    #         print("You can't deposit a negative amount")
    #     return self
    
    # decreases the account balance by the given amount if there are sufficient funds
    # def withdraw(self, amount):
    #     if amount < self.bank_account.balance:
    #         self.bank_account.balance -= amount
    #         print(f"Your current balance after withdrawal is ${self.bank_account.balance}")
    #     else:
    #         print("Insufficient funds: Charging a $5 fee")
    #         self.bank_account.balance -= 5
    #         print(f"After deduction your current balance is ${self.bank_account.balance}")
    #     return self
    
    # displays the user's account balance
    def display_user_balance(self):
        print(f"User Balance: ${self.bank_account.balance}")
        return self



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
    

user_1 = User("z", "s", "zs@email.com", 25)
user_2 = User("mango", "papaya", "mp@email.com", 2)

user_1.bank_account["checking"].deposit(50)
user_1.bank_account["savings"].deposit(200)


