from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    """This represents a SilverServiceTaxi object, which is a special type of taxi service."""
    def __init__(self, name, fuel, fanciness):
        """Initialize a Taxi instance based on the parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = 0.0
        self.price_per_km = fanciness * Taxi.price_per_km
        self.flagfall = 4.5

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def calculate_total_price(self):
        """calculate total price."""
        return round(super().get_fare() + self.flagfall, 1)
