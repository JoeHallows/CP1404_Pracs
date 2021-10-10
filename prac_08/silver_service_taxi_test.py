
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    name = input("Car Name: ")
    fanciness = int(input("Fanciness (1 to 5): "))
    fare_distance = (int(input("Fare distance: ")))

    silver_service_taxi = SilverServiceTaxi(name, 200, fanciness)
    silver_service_taxi.drive(fare_distance)

    print("{self.name}, fuel = {self.fuel}, odo = {self.odometer}, {self.current_fare_distance}km on current fare, "
          "${self.initial_fare}/km plus flagfall of ${self.flagfall:.2f}".format(self=silver_service_taxi))

    total_fare = silver_service_taxi.get_fare()
    print("Total fare: ${:.2f}".format(total_fare))


main()
