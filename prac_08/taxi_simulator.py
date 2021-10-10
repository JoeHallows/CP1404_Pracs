
from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    current_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available: ")
            taxi_list(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "D":
            drive_taxi(current_bill, current_taxi)
        elif choice != "QCD":
            print("Invalid option")
        print("Bill to Date: $", current_bill)
        print(MENU)
        choice = input(">>> ").upper()
    print("Total trip cost: ${:.2f}".format(current_bill))
    print("Taxis are now:")
    taxi_list(taxis)


def taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def drive_taxi(current_bill, current_taxi):
    current_taxi.initial_fare()
    fare_distance = float(input("Drive how far? "))
    current_taxi.drive(fare_distance)
    total_fare = current_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                 total_fare))
    current_bill += total_fare


main()
