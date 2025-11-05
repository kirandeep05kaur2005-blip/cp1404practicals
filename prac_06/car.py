"""
CP1404/CP5632 Practical - Car class
Estimate: 10 minutes
Actual:   15 minutes
"""
class Car:
    """Represent a Car object with a name, fuel, and odometer."""

    def __init__(self, name="Car", fuel=0):
        """
        Initialise a Car instance.

        :param name: str, car name/label
        :param fuel: int|float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a nice string like: Limo, fuel=42, odometer=277."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel (must be >= 0)."""
        if amount < 0:
            raise ValueError("Fuel amount must be >= 0")
        self.fuel += amount

    def drive(self, distance):
        """
        Drive the car up to the available fuel.
        :param distance: int|float requested distance (>= 0)
        :return: distance actually driven
        """
        if distance < 0:
            raise ValueError("Distance must be >= 0")

        actual = min(distance, self.fuel)
        self.odometer += actual
        self.fuel -= actual
        return actual
