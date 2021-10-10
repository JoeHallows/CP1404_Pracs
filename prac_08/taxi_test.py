
from prac_08.taxi import Taxi

prius_1 = Taxi("Prius 1", 100, 1.23)
prius_1.drive(40)
print("Taxi's fuel: ", prius_1.fuel)
print("Price of current fare:", prius_1.get_fare())
prius_1.start_fare()
prius_1.drive(100)
print("Taxi's fuel: ", prius_1.fuel)
print("Price of current fare:", prius_1.get_fare())
