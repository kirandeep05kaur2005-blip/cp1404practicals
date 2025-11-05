"""
Word Occurrences
Estimate: 20 minutes
Actual:   19 minutes
"""
def main():
    text = input("Text: ").strip()
    counts = {}
    for word in text.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1

    words = sorted(counts.keys())
    width = max((len(w) for w in words), default=1)
    for w in words:
        print(f"{w:{width}} : {counts[w]}")

main()
