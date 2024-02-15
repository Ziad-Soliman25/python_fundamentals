class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    # prints out all of the attributes of the instance
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")
    
    # checks instance to see if they are a member and if not changes status to True
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} {self.last_name} is already a member")
            return False
        else:
            print(f"Welcome, new member {self.first_name} {self.last_name}!")
            self.is_rewards_member = True
            self.gold_card_points = 200

    # deducts the amount from instance's current gold card points and checks to see if they have enough
    def spend_points(self, amount):
        if self.is_rewards_member == False:
            print("Not a member!")
            return
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            print(f"you spent {amount} points, you now have {self.gold_card_points} points")
        else:
            print(f"Not enough points, you currently have {self.gold_card_points} points")

new_user = User("jane", "doe", "jd@email.com", 30)
new_user.enroll()
new_user.spend_points(100)

new_user.enroll()
new_user.display_info()

user_1 = User("ziad", "soliman", "z@email.com", 25)
user_2 = User("max", "feeberman", "feebs@email.com", 1000)

user_1.spend_points(50)

user_2.enroll()
user_2.spend_points(80)
user_2.spend_points(150)

user_1.display_info()
user_2.display_info()