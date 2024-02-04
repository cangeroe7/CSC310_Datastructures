from linkedlist import Stack
from random import sample
from string import ascii_letters
from time import sleep
from room import Room

# list of questions and answers stored in tuples
qna = [("What city am I from? \nA) Utrecht \nB) Amsterdam \nC) Rotterdam \nD) The Hague\n", "A"),
       ("How tall am I? \nA) 6'6 \nB) 6'7 \nC) 6'8 \nD) 6'9\n", "A"),
       ("What is my favorite color? \nA) Blue\nB) Orange\nC) Pink\nD) Yellow\n", "A"),
       ("Who am I named after? \nA) Grandpa\nB) The Cat\nC) Dad\nD) Uncle\n", "B"),
       ("What is my minor? \nA) Geospatial Technology\nB) Mathematics\nC) Web and Mobile App Design\nD) Computer Information Systems\n", "B"),
       ("What sport did I NOT play in highschool\nA) Track\nB) Football\nC) Basketball\nD) I didn't play highschool sports\n", "B"),
       ("What sport did I play in college? \nA) Soccer\nB) Football\nC) Basketball\nD) Baseball\n", "C"),
       ("How old am I? \nA) 19\nB) 20\nC) 21\nD) 22\n", "C"),
       ("What is my favorite fruit? \nA) Apple\nB) Watermelon\nC) Blueberry\nD) Strawberry\n", "C"),
       ("Where did I go to highschool in America? \nA) Omaha, NE\nB) York, NE\nC) Cedar Bluffs, IA\nD) Lincoln, NE\n", "D"),
       ("What is my favorite meal? \nA) Pizza\nB) BBQ\nC) Hamburger\nD) Sushi\n", "D"),
       ("What college did I go to before WSC? \nA) I did not transfer\nB) Peru State\nC) UNL\nD) York College\n", "D")]

class Player:
    # init with player number, stack of rooms created from random sample from the questions and answers
    # if the game is a simulation simulate is set to true, otherwise False
    # While loop to create the names, by random generation if on simulation, otherwise by input
    def __init__(self, i, simulate=False):
        self.num = i
        self.rooms = Stack([Room(q, a) for q, a in sample(qna, 5)])
        self.name = ""
        self.simulate = simulate
        
        while self.name == "":
            if simulate: 
                self.name = "".join(sample(ascii_letters, 10))
            else:
                self.name = input(f"Player {self.num}, Enter Your Name: ")

    # pops 1 room of the stack. 
    # prints the players number, and it's name
    # it calls the Room class function ask_question() with simulation option
    # if the answer was wrong the room is pushed back onto the stack
    def play_room(self):
        room = self.rooms.pop()
        
        print(f"Player {self.num}'s turn: {self.name}\n")
        sleep(1)
        answer = room.ask_question(self.simulate)
        if not answer:
            self.rooms.push(room)
        return answer