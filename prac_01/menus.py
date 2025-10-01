"""
Menu-driven program
"""

# Get the user's name
name = input("Enter name: ")

# Display the menu
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)

# Get the first choice
choice = input(">>> ").upper()

# Loop until the user chooses to quit
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Show the menu again and get the next choice
    print(MENU)
    choice = input(">>> ").upper()

# After quitting
print("Finished.")
