class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name = "", year = 0, cost = 0):
        """Initialise a Car instance.
        year: int, Storage Year
        cost: float"""
        self.name = name
        self.year = year
        self.cost = cost
    def get_age(self, year_of_now = 0):
        """Return the age of the Guitar."""
        return year_of_now - self.year

    def is_vintage(self, year_of_now = 0):
        """Determine if the year is greater than 50 years"""
        return self.get_age(year_of_now) >= 50

    def __str__(self):
        """Return the guitar's name, year, and price."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"