"""
Emails to Names
Estimate: 20 minutes
Actual:   17  minutes
"""
def extract_name(email: str) -> str:
    local = email.split("@", 1)[0]
    parts = [p for p in local.replace(".", " ").replace("_", " ").split() if p]
    return " ".join(parts).title() if parts else "User"

def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email:
        suggested = extract_name(email)
        response = input(f"Is your name {suggested}? (Y/n) ").strip().lower()
        name = suggested if response in ("", "y", "yes") else input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    for e, n in email_to_name.items():
        print(f"{n} ({e})")

main()
