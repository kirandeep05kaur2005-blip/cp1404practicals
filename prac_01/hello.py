import random

low = int(input("Enter a low number: "))
high = int(input("Enter a high number: "))

# keep asking until high is bigger than low
while high <= low:
    print("High must be greater than low!")
    high = int(input("Enter a high number: "))

n = random.randint(low, high)   # pick a random number
print(":) " * n)                # print n smiley faces
