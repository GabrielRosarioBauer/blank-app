"""Parser contract for historical KODEN CSV output."""

from typing import TextIO


def parse_koden_csv(source: TextIO) -> None:
    """Parse historical XYZ/global-coordinate CSV data when its schema is defined."""
    del source
    raise NotImplementedError
