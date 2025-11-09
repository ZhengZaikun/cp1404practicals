class ProgrammingLanguage:
    """Represent a Programming Language object."""
    def __init__(self, name = "", typing = "", reflection = True, year = 0):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.year = year
        self.reflection = reflection

    def is_dynamic(self):
        """Determine if it is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"