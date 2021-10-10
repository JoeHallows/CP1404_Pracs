
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    name = input("Car Name: ")
    fuel = int(input("Amount of fuel: "))
    fanciness = int(input("Fanciness (1 to 5): "))

    silver_service_taxi = SilverServiceTaxi(name, fuel, fanciness)

    print("{self.name}, fuel = {self.fuel}, odo = {self.odometer}, {self.current_fare_distance}km on current fare, "
          "${self.initial_fare}/km plus flagfall of ${self.flagfall:.2f}".format(self=silver_service_taxi))


main()