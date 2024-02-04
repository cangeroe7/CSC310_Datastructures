# https://www.geeksforgeeks.org/ for syntax 

from player import Player
from collections import deque
from time import sleep
import json

class Game:
    # initialize the game as a simulation or an actual game
    # players are made with the player class and put into a queue
    # dict starts with all 0's
    # json file is reset to all 0's 
    def __init__(self, simulate=False):
        self.players = deque([Player(i+1, simulate) for i in range(5)])
        self.stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        with open("stats.json", "w") as file:
            file.write(json.dumps(self.stats, indent=4))
        self.rank = []
    
    # as long as there are players in the queue the players keep cycling
    # If a player answered all questions in the rooms correctly a congratulation screen is printed
    # and the player is pushed to the rank list, and removed from the queue
    # if the player didn't get through all rooms the player is added to the back of the queue
    # after the room is played the stats are updated
    # self.final is a final print function that shows who ranked where
    # response is either 0 if wrong, and 1 if correct
    def play_game(self):
        while self.players:
            player = self.players.popleft()
            response = player.play_room()
            self.update_stats(player, response)
            if self.stats[player.num] == 5:
                self.congratulate(player)
                self.rank.append(player)
            else:
                self.players.append(player)
        self.final()

    # the game dict is updated, and the json is updated too
    def update_stats(self, player, response):
        self.stats[player.num] += response
        with open("stats.json", "w") as file:
            file.write(json.dumps(self.stats, indent=4))
    
    def congratulate(self, player):
        print(f"Congratulations {player.name}!!! Your rank is: {5 - len(self.players)}\n")
        sleep(3)

    # prints every players rank
    def final(self):
        for i in range(5):
            player = self.rank[i]
            print(f"Rank {i+1}: Player {player.num}, {player.name}")

# test the game, if the argument for Game() is True it runs a simulation, 
# otherwise it runs the game as if it has 5 players putting in names, and answers
if __name__ == "__main__":
    test = Game()
    test.play_game()    
