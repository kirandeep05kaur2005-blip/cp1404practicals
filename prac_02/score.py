"""Simple program to check score status"""

def main():
    # Ask the user for a score
    score = float(input("Enter score: "))
    # Show the result by calling the function
    print(get_result(score))


def get_result(score):
    # Check score and return the result as text
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Run the program
main()
