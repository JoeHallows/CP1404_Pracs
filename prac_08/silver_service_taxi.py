from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    price_per_km = 1.23
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0
        self.initial_fare = SilverServiceTaxi.price_per_km * self.fanciness

    def get_fare(self):
        fare_result = SilverServiceTaxi.price_per_km * self.fanciness * self.current_fare_distance + SilverServiceTaxi.flagfall
        return fare_result
