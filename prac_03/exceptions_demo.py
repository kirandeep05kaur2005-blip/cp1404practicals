"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   -> When the user enters something that is not a valid integer (e.g., "abc", 4.5).
2. When will a ZeroDivisionError occur?
   -> When the user enters 0 for the denominator (since you cannot divide by zero).
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   -> Yes, by validating the denominator input (loop until the user enters a non-zero number).
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (non-zero): "))

    # Prevent ZeroDivisionError by checking denominator before dividing
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero integer.")
        denominator = int(input("Enter the denominator (non-zero): "))

    fraction = numerator / denominator
    print(f"Result: {fraction}")

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
