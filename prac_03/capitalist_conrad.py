import random

# ---------------- CONSTANTS ---------------- #
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

# ---------------- SETUP ---------------- #
price = INITIAL_PRICE
number_of_days = 0

# ---------------- FILE OUTPUT ---------------- #
with open(FILENAME, 'w') as out_file:
    print(f"Starting price: ${price:,.2f}", file=out_file)

    # ---------------- LOOP ---------------- #
    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1

        # 50% chance of increase or decrease
        if random.randint(1, 2) == 1:
            # random increase between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # random decrease between 0 and MAX_DECREASE
            price_change = random.uniform(-MAX_DECREASE, 0)

        # update the price
        price *= (1 + price_change)

        # write to file
        print(f"On day {number_of_days}, price is: ${price:,.2f}", file=out_file)

    # ---------------- FINAL MESSAGE ---------------- #
    print(f"Simulation ended after {number_of_days} days at price ${price:,.2f}", file=out_file)
