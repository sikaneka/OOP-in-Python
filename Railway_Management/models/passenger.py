import random

class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.pnr = "PNR" + str(random.randint(1000, 9999))

    def display_passenger(self):
        return f"{self.name}, {self.age} yrs, {self.gender}, PNR: {self.pnr}"
