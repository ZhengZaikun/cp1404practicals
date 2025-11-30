"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, is_reflection, year, is_pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year
        self.is_pointer_arithmetic = is_pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        reflection_text = "Yes" if self.is_reflection else "No"
        pointer_text = ", Pointer Arithmetic" if self.is_pointer_arithmetic == "Yes" else ""
        return f"{self.name}, {self.typing} Typing, Reflection={reflection_text}, First appeared in {self.year}{pointer_text}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer_arithmetic(self):
        """Determine if language is pointer arithmetic."""
        return self.is_pointer_arithmetic == "Yes"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, "No")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, "No")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, "Yes")

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()