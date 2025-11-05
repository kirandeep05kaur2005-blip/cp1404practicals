"""
CP1404/CP5632 Practical - Client code to use the Car class
Estimate: 5 minutes
Actual:  4  minutes
"""

# If used_cars.py and car.py are in the SAME folder (prac_06), use this:
from car import Car

# If you're running from the project root and car.py is inside prac_06/,
# you can alternatively use:
# from prac_06.car import Car


def main():
    """Demo test code following the Prac 06 modifications."""
    # Create a new Car object called "Limo" initialised with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(limo.fuel)

    # Attempt to drive the car 115 km; print how far it actually drove
    driven = limo.drive(115)
    print(f"Drove {driven}km")

    # Print the car object to check __str__ output
    print(limo)

    # (Optional) Show another example
    my_car = Car("MyCar", 50)
    my_car.drive(30)
    print(my_car)  # -> "MyCar, fuel=20, odometer=30"


main()
