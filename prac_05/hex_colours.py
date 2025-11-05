"""
Hex Colours
Estimate: 15 minutes
Actual:   18 minutes
"""
NAME_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUAMARINE": "#7fffd4",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "BLUEVIOLET": "#8a2be2",
    "CORNFLOWERBLUE": "#6495ed",
    "CRIMSON": "#dc143c",
    "DARKORANGE": "#ff8c00",
    "GOLD": "#ffd700",
}

def main():
    name = input("Colour name: ").strip()
    while name:
        code = NAME_TO_HEX.get(name.replace(" ", "").upper())
        print(code if code else "Invalid colour name")
        name = input("Colour name: ").strip()

main()
