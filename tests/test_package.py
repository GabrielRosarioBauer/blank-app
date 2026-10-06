"""Smoke tests for the application package architecture."""

from importlib import import_module

from rrd_koden.domain import (
    KodenMeasurement,
    KodenRawMeasurement,
    PanelAcceptanceCriteria,
    PanelDesign,
    SurveySetup,
)

ARCHITECTURAL_PACKAGES = (
    "domain",
    "parsers",
    "processing",
    "services",
    "database",
    "reporting",
    "ui",
    "visualization",
)


def test_package_imports() -> None:
    """The application package can be imported from the src layout."""
    import rrd_koden

    assert rrd_koden.__name__ == "rrd_koden"


def test_architectural_packages_import() -> None:
    """Every package boundary is importable."""
    for package in ARCHITECTURAL_PACKAGES:
        module = import_module(f"rrd_koden.{package}")
        assert module.__name__ == f"rrd_koden.{package}"


def test_panel_design_exposes_design_values() -> None:
    """Panel design geometry retains its supplied reference values."""
    panel = PanelDesign(
        panel_id="P-01",
        center_easting=100.0,
        center_northing=200.0,
        top_elevation=12.5,
        wall_axis_deg=90.0,
        width=1.2,
        length=6.0,
        total_depth=30.0,
    )

    assert panel.panel_id == "P-01"
    assert panel.center_easting == 100.0
    assert panel.center_northing == 200.0
    assert panel.top_elevation == 12.5
    assert panel.wall_axis_deg == 90.0
    assert panel.width == 1.2
    assert panel.length == 6.0
    assert panel.total_depth == 30.0


def test_survey_setup_exposes_control_values() -> None:
    """A unit setup retains control points, sensor placement, and orientation."""
    setup = SurveySetup(
        unit_id="O",
        dp1_easting=100.0,
        dp1_northing=200.0,
        dp1_elevation=12.0,
        dp2_easting=101.0,
        dp2_northing=201.0,
        dp2_elevation=12.1,
        sensor_height=1.5,
        distance_from_dp1=0.75,
        orientation="Y' -> Y",
    )

    assert setup.unit_id == "O"
    assert setup.dp1_easting == 100.0
    assert setup.dp1_northing == 200.0
    assert setup.dp1_elevation == 12.0
    assert setup.dp2_easting == 101.0
    assert setup.dp2_northing == 201.0
    assert setup.dp2_elevation == 12.1
    assert setup.sensor_height == 1.5
    assert setup.distance_from_dp1 == 0.75
    assert setup.orientation == "Y' -> Y"


def test_raw_measurement_exposes_directional_values() -> None:
    """A RAW measurement retains all five source values without interpretation."""
    measurement = KodenRawMeasurement(
        depth_raw=1.0,
        x_raw=2.0,
        x_prime_raw=3.0,
        y_raw=4.0,
        y_prime_raw=5.0,
    )

    assert measurement.depth_raw == 1.0
    assert measurement.x_raw == 2.0
    assert measurement.x_prime_raw == 3.0
    assert measurement.y_raw == 4.0
    assert measurement.y_prime_raw == 5.0


def test_normalized_measurement_exposes_metric_values() -> None:
    """A normalized measurement retains all five metric values."""
    measurement = KodenMeasurement(
        depth_m=1.0,
        x_m=0.2,
        x_prime_m=0.3,
        y_m=0.4,
        y_prime_m=0.5,
    )

    assert measurement.depth_m == 1.0
    assert measurement.x_m == 0.2
    assert measurement.x_prime_m == 0.3
    assert measurement.y_m == 0.4
    assert measurement.y_prime_m == 0.5


def test_acceptance_criteria_expose_specification_values() -> None:
    """Acceptance limits remain explicit and independent of panel geometry."""
    criteria = PanelAcceptanceCriteria(
        parallelism_tolerance=0.1,
        minimum_checking_depth=5.0,
        verticality_limit=0.005,
        max_twist_bauer=0.4,
        max_twist_spec=0.3,
    )

    assert criteria.parallelism_tolerance == 0.1
    assert criteria.minimum_checking_depth == 5.0
    assert criteria.verticality_limit == 0.005
    assert criteria.max_twist_bauer == 0.4
    assert criteria.max_twist_spec == 0.3
