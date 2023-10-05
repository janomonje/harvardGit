class Point():
    def __init__(self, input1, input2):
        self.x = input1 # the inputs are being stored in properties called x nad y
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addPassenger(self, name):
        if not self.openSeats(): # if openseats == 0
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)    

flight = Flight(3)

people = ["Harry", "Ale", "Carlos", "Alberto"]

for person in people:
    if flight.addPassenger(person): #this return true or false
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
