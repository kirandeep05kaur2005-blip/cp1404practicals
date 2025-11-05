"""
Guitar tests
Estimate: 7 minutes
Actual:   5 minutes
"""
from datetime import date
from guitar import Guitar

def main():
    current_year = date.today().year  # use the real current year dynamically

    l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    expected_l5_age = current_year - 1922
    expected_another_age = current_year - 2013

    print(f"{l5.name} get_age() - Expected {expected_l5_age}. Got {l5.get_age(current_year)}")
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age(current_year)}")

    print(f"{l5.name} is_vintage() - Expected {expected_l5_age >= 50}. Got {l5.is_vintage(current_year)}")
    print(f"{another.name} is_vintage() - Expected {expected_another_age >= 50}. Got {another.is_vintage(current_year)}")

main()
