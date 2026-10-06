"""Acceptance criteria kept separate from panel design geometry."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PanelAcceptanceCriteria:
    """Project specification limits used to assess processed panel geometry."""

    parallelism_tolerance: float
    minimum_checking_depth: float
    verticality_limit: float
    max_twist_bauer: float
    max_twist_spec: float
