import random
from classes.deck import Deck

class Player:

    all_players = []

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_total = 0
        # self.split_hand = []
        Player.all_players.append(self)

    # This line defines the __str__ method for the class.
    # It's a special method in Python classes that defines how the object should be represented as a string.
    def __str__(self):
        hand_cards = ""
        for card in self.hand:
            hand_cards += f"{card.string_val} of {card.suit} "
        return hand_cards

    def draw_cards(self, deck):
        new_card = random.choice(deck)
        deck.remove(new_card)
        self.hand.append(new_card)
        removed_cards.append(new_card)
        return self
    
    def card_points(self):
        total = 0
        has_ace = False
        for card in self.hand:
            total += card.point_val
            if (card.point_val == 1):
                has_ace = True
        if (has_ace == True and total <= 11):
            total += 10
        self.hand_total = total
        return self

    def print_player_info(self):
        print(f"name: {self.name}\nhand: {self.hand}\nhand total: {self.hand_total}")


removed_cards = []

player_1 = Player("Peter")
player_2 = Player("Splungo")


bicycle = Deck().cards
# print(len(bicycle))

# bicycle.show_cards()

player_1.draw_cards(bicycle).draw_cards(bicycle)
# for card in removed_cards:
#     card.card_info()

player_2.draw_cards(bicycle).draw_cards(bicycle)
# for card in removed_cards:
#     card.card_info()


# print(len(bicycle))
# player_1.print_player_info()

for player in Player.all_players:
    # player_state = None
    while True:
        player.card_points()
        print(player)
        print(player.hand_total)
        if (player.hand_total > 21):
            print(f"{player.name} busts")
            # player_state = "Bust"
            break
        elif (player.hand_total  == 21):
            print(f"{player.name} got black jack!!!")
            # player_state = "BlackJack"
            break
        elif (player.hand_total >= 18 and player.hand_total <=20):
            print("I'll stay")
            break
        else:
            player.draw_cards(bicycle)

    # if player_state == "BlackJack":
    #     print("player 1 wins")
    #     break
    # elif player_state == "Bust":
    #     print("player 2 wins")
    #     break

