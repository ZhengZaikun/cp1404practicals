from prac_09.musician import Musician

class Band:
    """Represent a Bund"""
    def __init__(self, name):
        """Initialise a Bund"""
        self.name = name
        self.informations_of_musicians = []

    def __str__(self):
        """Return a string representation of the Bund"""
        musicians_strings = [str(musician) for musician in self.informations_of_musicians]
        return f"{self.name} ({",".join(musicians_strings)})"

    def add(self, musician):
        """Add a list of Musicians."""
        self.informations_of_musicians.append(musician)

    def play(self):
        """Play the Bund"""
        for musician in self.informations_of_musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs an instrument!")

