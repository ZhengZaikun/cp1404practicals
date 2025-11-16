class Project:
    def __init__(self, name, date, priority=0, cost=0.0, completion_percentage=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.completion_percentage}%"


    def __lt__(self, other):
        return self.priority < other.priority

    def get_start_date(self):
        """Return the start_date attribute for use as a sort key."""
        return self.date