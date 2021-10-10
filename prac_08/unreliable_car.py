
from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if (random.randint(1, 101)) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            print("The car broke down - this car is unreliable!")
            return distance == 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

