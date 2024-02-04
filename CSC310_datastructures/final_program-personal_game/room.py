from random import sample
import random
from time import sleep


class Room:
    # initialize every room with a question and an answer
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    # Asks the player the question corresponding to the room. 
    # if the game is on simulation mode it picks a random answer (75% of the time it's correct).
    # Otherwise it's up to the player to respond with the answer
    # Bunch of sleeps to make it look a little smoother, both for playing and simulating
    # If correct 1 is returned, otherwise 0, which will be added to the players escaped rooms 
    def ask_question(self, simulate=False):
        print(self.question)
        if simulate: 
            sleep(1)
            response = random.choice(["A", "B", "C", "D", self.answer, self.answer, self.answer, self.answer, self.answer, ])
            print(f"Answer: {response}")
        else:
            response = input("Answer: ").upper()
        print("")
        sleep(1)

        if response == self.answer:
            print("Correct!\n")
            sleep(1)
            return 1
        else:
            print("Wrong!\n")
            sleep(1)
            return 0