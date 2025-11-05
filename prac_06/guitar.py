"""
Guitar class
Estimate: 12 minutes
Actual:   ___ minutes
"""
from datetime import date

VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar with name, year and cost."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        """Create a Guitar with defaults name="", year=0, cost=0."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        """Return 'Name (Year) : $X,XXX.XX'."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year: int | None = None) -> int:
        """
        Return how old the guitar is in years.
        If current_year is not provided, use today's year.
        """
        if current_year is None:
            current_year = date.today().year
        return current_year - self.year

    def is_vintage(self, current_year: int | None = None) -> bool:
        """Return True if the guitar is VINTAGE_AGE years or older."""
        return self.get_age(current_year) >= VINTAGE_AGE
