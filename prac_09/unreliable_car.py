from random import randint
from prac_09.car import Car
class UnreliableCar(Car):
    """An unreliable car is one that can only operate under specific conditions."""
    price_per_km = 1.23
    def __init__(self, name = "", fuel=0, reliability = 0.0):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Returns a string representation of UnreliableCar."""
        return super().__str__()

    def drive(self, distance):
        """Based on the vehicle's reliability, drive the vehicle a specified distance."""
        distance = self.judge_reliability(distance)
        distance_driven = super().drive(distance)
        return distance_driven


    def judge_reliability(self, distance):
        """Judge the reliability of the vehicle."""
        if self.reliability <= randint(0,100):
            distance = 0
        return distance
