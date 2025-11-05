"""
Guitars program
Estimate: 15 minutes
Actual:   10 minutes
"""
from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # --- Normal interactive input ---
    name = input("Name: ").strip()
    while name:
        year = int(input("Year: ").strip())
        cost = float(input("Cost: $").strip())
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ").strip()

    # --- Programmer Efficiency (for quick testing) ---
    # Comment the input block above and uncomment these lines to avoid retyping:
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_tag}")

if __name__ == "__main__":
    main()
