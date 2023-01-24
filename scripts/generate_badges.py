"""Generate badges with amounts for Bluetooth numbers."""
from pathlib import Path

from bluetooth_numbers import characteristic, company, descriptor, oui, service

README_FILE = "README.rst"
BEFORE_NUMBERS = ".. inclusion-marker-before-numbers\n"
AFTER_NUMBERS = ".. inclusion-marker-after-numbers\n"
REPO = "https://github.com/koenvervloesem/bluetooth-numbers/"


def create_badges() -> str:
    """Generate badges with amounts for Bluetooth numbers.

    Returns:
        str: Code for the badges in RST syntax.
    """
    badges = create_badge("Companies", len(company))
    badges += create_badge("Services", len(service))
    badges += create_badge("Characteristics", len(characteristic))
    badges += create_badge("Descriptors", len(descriptor))
    badges += create_badge("OUIs", len(oui))
    return badges


def create_badge(description: str, number: int) -> str:
    """Create custom shields.io badge with a description, number and link.

    Args:
        description (str): Description shown in the badge
        number (int): Amount shown in the badge

    Returns:
        str: Code for the badge in RST syntax
    """
    image = f".. image:: https://img.shields.io/badge/{description}-{number}-blue\n"
    alt = f"    :alt: {description}\n"
    target = f"    :target: {REPO}blob/main/src/bluetooth_numbers/_{description.lower()}.py\n"
    return image + alt + target


if __name__ == "__main__":
    with Path(README_FILE).open(encoding="utf-8") as readme_file:
        readme_text = readme_file.readlines()

    before_numbers = readme_text.index(BEFORE_NUMBERS) + 1
    after_numbers = readme_text.index(AFTER_NUMBERS)

    with Path(README_FILE).open("w", encoding="utf-8") as readme_file:
        readme_file.write("".join(readme_text[:before_numbers]))
        readme_file.write("\n")
        readme_file.write(create_badges())
        readme_file.write("\n")
        readme_file.write("".join(readme_text[after_numbers:]))
