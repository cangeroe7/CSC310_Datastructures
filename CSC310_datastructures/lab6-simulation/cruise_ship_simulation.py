import random
from collections import deque

# Assigning the deck to the passengers with corresponding passes
deck_assignment = {
    "A": "GREEN",
    "B": "BLUE",
    "C": "ORANGE",
    "D": "RED"
}


class Cruise_Ship:
    # list of passengers is turned into queue so popping at index 0 takes O(1)
    # deck rooms are created and assigned to a dictionary with deck colors as keys.
    def __init__(self, passengers):
        self.passenger_q = deque(passengers)
        self.passengers = []
        self.deck_rooms = {
            "GREEN": [f"Green{i+1}" for i in range(20)],
            "BLUE": [f"Blue{i+1}" for i in range(100)],
            "ORANGE": [f"Orange{i+1}" for i in range(200)],
            "RED": [f"Red{i+1}" for i in range(500)]
            }

    # while there are passengers in the queue the first passenger gets popped from the queue.
    # the room and deck get assigned to the passenger, and a new passenger class is created 
    # that is appended to the Cruise_Ship passengers list.
    def simulate(self):
        while self.passenger_q:
            passenger_color, passenger_name = self.passenger_q.popleft()
            passenger_deck = deck_assignment[passenger_color]
            # Make sure that there are still rooms available
            assert self.deck_rooms[passenger_deck]
            new_room = self.deck_rooms[passenger_deck].pop()
            new_passenger = Passenger(passenger_name, passenger_color, passenger_deck, new_room)
            self.passengers.append(new_passenger)
            print(f"""
Passenger Name: {new_passenger.name}
Passenger Pass: {new_passenger.color}
Passenger Deck: {new_passenger.deck}
Passenger Room: {new_passenger.room}
                  """)
        # Make sure all rooms are popped off and assigned
        assert not self.deck_rooms["GREEN"]
        assert not self.deck_rooms["BLUE"]
        assert not self.deck_rooms["ORANGE"]
        assert not self.deck_rooms["RED"]

class Passenger:
    def __init__(self, name, color, deck, room):
        self.name = name
        self.color = color
        self.deck = deck
        self.room = room

    
        
# create the passengers passes and names, shuffling, and zipping the two together to be pushed turned into a queue   
passengers_color = ["A" for _ in range(20)] + ["B" for _ in range(100)] + ["C" for _ in range(200)] + ["D" for _ in range(500)]
random.shuffle(passengers_color)
passengers_name = [f"Name{i+1}" for i in range(820)]

passengers = list(zip(passengers_color, passengers_name))

if __name__ == "__main__":
    test_ship = Cruise_Ship(passengers)
    test_ship.simulate()