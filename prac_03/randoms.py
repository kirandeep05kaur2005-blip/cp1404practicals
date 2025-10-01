
import random

# Run multiple times to see different results
print(random.randint(5, 20))  # line 1
# Observation: Produces a random integer between 5 and 20 inclusive.
# Smallest = 5, Largest = 20

print(random.randrange(3, 10, 2))  # line 2
# Observation: Produces a random odd number between 3 and 9 (3, 5, 7, 9).
# Smallest = 3, Largest = 9
# Could it produce a 4? -> No, because step=2 gives only odd numbers.

print(random.uniform(2.5, 5.5))  # line 3
# Observation: Produces a random float between 2.5 and 5.5.
# Smallest possible ~2.5, Largest possible ~5.5

# Random number between 1 and 100 inclusive:
random_number = random.randint(1, 100)
print(random_number)
