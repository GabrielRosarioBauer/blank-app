# RRD Koden application architecture

## Processing chain

RRD Koden separates each step of the confirmed survey workflow:

```text
RAW -> parser -> normalized measurements -> coordinate transformation -> XYZ
    -> elevation averaging -> Unit O + Unit B combination -> panel geometry
    -> visualization/reporting
```

The parser boundary represents the confirmed five-column RAW structure: depth,
X, X', Y, and Y'. Parsing details, inactive-channel markers, transformation
formulas, and engineering calculations remain undefined until verified against
the historical workflow and source data.

## Domain concepts

- **Panel design geometry** describes the intended panel dimensions, reference
  coordinates, elevation, depth, and wall-axis orientation. It is an input to
  processing and is independent of pass/fail limits.
- **Survey setup** describes one spatial KODEN setup, including its Unit O or
  Unit B identity, DP1 and DP2 coordinates, sensor height, distance from DP1,
  and measurement orientation. A panel survey can have two distinct setups.
- **Processing settings** will control technical processing choices such as
  filtering and elevation averaging. They are not design geometry or acceptance
  limits; concrete settings will be introduced only when confirmed.
- **Acceptance criteria** hold project or equipment specification limits used
  to assess results. They remain separate from both geometry inputs and
  processing settings.

## Package responsibilities

- `domain` contains dependency-free dataclass models.
- `parsers` converts source files into domain objects without engineering logic.
- `processing` owns the staged engineering workflow and may depend on `domain`.
- `services` will orchestrate parsing, processing, persistence, and reporting.
- `database` defines persistence boundaries.
- `reporting` defines report-generation boundaries.
- `visualization` defines plan, profile, and 3D presentation boundaries.
- `ui` remains a thin interaction layer and contains no engineering calculations.
