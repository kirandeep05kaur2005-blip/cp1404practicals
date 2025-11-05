"""
Wimbledon
Estimate: 35 minutes
Actual:   13 minutes
"""
FILENAME = "wimbledon.csv"

def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as f:
        # Year, Champion, Country, Runner-up, Country, Score
        lines = [line.strip().split(",") for line in f if line.strip()]
    return lines

def count_champions(rows):
    counts = {}
    for _, champion, *_ in rows:
        counts[champion] = counts.get(champion, 0) + 1
    return counts

def collect_countries(rows):
    return sorted({rows[i][2] for i in range(len(rows))})

def main():
    rows = load_data(FILENAME)
    champion_counts = count_champions(rows)
    print("Wimbledon Champions:")
    for name, times in sorted(champion_counts.items(), key=lambda x: (x[0])):
        print(f"{name} {times}")

    countries = collect_countries(rows)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

main()
