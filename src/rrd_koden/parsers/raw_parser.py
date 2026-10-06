"""Parser contract for five-column directional KODEN RAW data."""

from collections.abc import Iterable
from typing import TextIO

from rrd_koden.domain.measurement import KodenRawMeasurement


def parse_raw_measurements(source: TextIO) -> Iterable[KodenRawMeasurement]:
    """Parse depth, X, X-prime, Y, and Y-prime values from a RAW source.

    The concrete file syntax and channel-validity rules have not yet been
    established, so this architecture-level stub performs no parsing.
    """
    del source
    raise NotImplementedError
