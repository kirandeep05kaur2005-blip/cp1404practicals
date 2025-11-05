"""
ProgrammingLanguage class
Estimate: 10 minutes
Actual:   ___ minutes
"""

class ProgrammingLanguage:
    """Represent a programming language with typing, reflection, and first-appeared year."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        """
        Create a ProgrammingLanguage.
        :param name: language name (e.g., "Python")
        :param typing: "Dynamic" or "Static"
        :param reflection: True if supports reflection; otherwise False
        :param year: first appeared year (e.g., 1991)
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        """Return True if this language is dynamically typed."""
        return self.typing.strip().lower() == "dynamic"

    def __str__(self) -> str:
        """Human-friendly string like: Python, Dynamic Typing, Reflection=True, First appeared in 1991"""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
