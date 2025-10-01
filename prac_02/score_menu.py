"""Menu program for working with scores"""

def main():
    score = get_valid_score()
    display_menu()
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").upper()

    print("Farewell!")


def display_menu():
    """Show the menu options."""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Ask the user for a score between 0 and 100."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def get_result(score):
    """Return the result for the given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
