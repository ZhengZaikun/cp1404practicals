class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name = "", year = 0, cost = 0):
        """Initialise a Guitar instance.
        name: string, name of the guitar
        year: integer, The year of guitar making
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost
    def get_age(self, year_of_now = 0):
        """Return the age of the Guitar."""
        return year_of_now - self.year

    def is_vintage(self, year_of_now = 0):
        """Determine if the year is greater than 50 years"""
        return self.get_age(year_of_now) >= 50

    def __lt__(self, other):
        """
        Determine if this Guitar is less than another Guitar based on year.
        """
        return self.year < other.year

    def __str__(self):
        """Return the guitar's name, year, and price."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"