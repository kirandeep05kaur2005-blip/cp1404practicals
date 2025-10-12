import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        numbers = []
        while len(numbers) < NUMBERS_PER_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:  # make sure it's not repeated
                numbers.append(number)
        numbers.sort()
        for num in numbers:
            print(f"{num:2}", end=" ")
        print()  # move to next line

main()
