
from prac_08.unreliable_car import UnreliableCar


def main():
    name = input("Car Name: ")
    reliability = int(input("Reliability: "))

    # while 1 > reliability > 100:
    #     print("Reliability must be between 1 and 100")
    #     reliability = int(input("Reliability: "))
    # while reliability == "":
    #     print("Reliability must not be blank")
    #     reliability = int(input("Reliability: "))

    unreliable_car = UnreliableCar(name, 100, reliability)
    distance_to_drive = int(input("Kms to Drive: "))
    unreliable_car.drive(distance_to_drive)

    print("{self.name}, fuel={self.fuel}, odometer={self.odometer}".format(self=unreliable_car))


main()


