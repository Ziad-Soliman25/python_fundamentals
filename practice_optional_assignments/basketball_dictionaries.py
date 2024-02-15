players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:

    player_list = []

    def __init__(self, player_info):
        self.player_info = player_info
    
    def display_player_info(self):
        print(f"{self.player_info}")
        return self
    
    @classmethod

kevin = players[0]
jason = players[1]
kyrie = players[2]
# damian = players[3]
# joel = players[4]
# demar = players[5]

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)