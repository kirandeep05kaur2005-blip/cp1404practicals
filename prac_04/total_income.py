def main():
    """Collect monthly incomes and display a cumulative income report."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Print an income report with cumulative totals for the given list of incomes."""
    print("\nIncome Report")
    print("-------------")
    total = 0.0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
