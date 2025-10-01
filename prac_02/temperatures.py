"""Temperature conversion menu using SRP functions ."""


def main():
    """Display a menu and perform temperature conversions."""
    MENU = "(C)elsius to Fahrenheit  |  (F)ahrenheit to Celsius  |  (Q)uit"
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c_to_f(celsius)
            print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = f_to_c(fahrenheit)
            print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Goodbye!")


def c_to_f(celsius: float) -> float:
    """Return Fahrenheit equivalent of Celsius."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Return Celsius equivalent of Fahrenheit."""
    return (fahrenheit - 32) * 5 / 9


main()
