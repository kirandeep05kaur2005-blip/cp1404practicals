"""
Languages client program
Estimate: 8 minutes
Actual:   6 minutes
"""
from programming_language import ProgrammingLanguage


def main():
    # Create objects per the prac instructions
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print single object to demonstrate __str__
    print(python)

    # Store them in a list
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages using the is_dynamic() method
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
