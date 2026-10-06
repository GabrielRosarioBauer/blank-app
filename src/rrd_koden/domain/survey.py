"""Spatial setup for an individual KODEN survey unit."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SurveySetup:
    """Survey control points and sensor placement for one KODEN unit."""

    unit_id: str
    dp1_easting: float
    dp1_northing: float
    dp1_elevation: float
    dp2_easting: float
    dp2_northing: float
    dp2_elevation: float
    sensor_height: float
    distance_from_dp1: float
    orientation: str
