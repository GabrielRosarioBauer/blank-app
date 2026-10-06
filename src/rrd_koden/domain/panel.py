"""Panel design geometry."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PanelDesign:
    """Design dimensions and reference position for a diaphragm-wall panel."""

    panel_id: str
    center_easting: float
    center_northing: float
    top_elevation: float
    wall_axis_deg: float
    width: float
    length: float
    total_depth: float
