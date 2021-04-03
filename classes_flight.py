class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): # equivalent to if self.open_seats == 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):   
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["Harry", "Anna", "Brian", "Bernard"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to the flight succesfully!")
    else:
        print(f"Couldn't add {person} to the flight...")