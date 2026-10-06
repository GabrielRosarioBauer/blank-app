"""Raw and normalized directional KODEN measurements."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KodenRawMeasurement:
    """One unmodified five-column directional measurement from a RAW source."""

    depth_raw: float
    x_raw: float
    x_prime_raw: float
    y_raw: float
    y_prime_raw: float


@dataclass(frozen=True, slots=True)
class KodenMeasurement:
    """One normalized directional measurement expressed in metres."""

    depth_m: float
    x_m: float
    x_prime_m: float
    y_m: float
    y_prime_m: float
