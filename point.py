
class Point:
    def __init__(self, row, col, dependent_values=0):
        self.row = row
        self.col = col
        self.dependent_values = dependent_values

    def __lt__(self, other):
        return self.dependent_values < other.dependent_values

    def __gt__(self, other):
        return self.dependent_values > other.dependent_values

    def __eq__(self, other):
        return self.dependent_values == other.dependent_values
