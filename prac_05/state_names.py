"""
State Names
Estimate: 15 minutes
Actual:   10 minutes
"""
SHORT_TO_FULL = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}

def main():
    # print all codes neatly aligned
    max_len = max(len(k) for k in SHORT_TO_FULL)
    for code, name in SHORT_TO_FULL.items():
        print(f"{code:<{max_len}} is {name}")
    print()

    # lookup loop (case-insensitive) using EAFP
    code = input("Enter short state: ").strip()
    while code:
        try:
            print(SHORT_TO_FULL[code.upper()])
        except KeyError:
            print("Invalid short state")
        code = input("Enter short state: ").strip()

main()
