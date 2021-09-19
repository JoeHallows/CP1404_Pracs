"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""

    name = input("Car Name: ")

    my_car = Car(name, 319)
    my_car.name = name
    my_car.drive(277)

    # print(my_car.__str__)

    print("{self.name}'s fuel = {self.fuel}".format(self=my_car))
    print("{}'s odo = {}".format(my_car.name, my_car.odometer))

    print("{}, fuel={}, odometer={}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{self.name}, fuel={self.fuel}, odometer={self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("Limo's fuel: ", limo.fuel)
    limo.drive(115)
    print("Limo's Odometer:", limo.odometer)
    print("Limo's fuel after {} drive: {}".format(limo.odometer, limo.fuel))




main()

