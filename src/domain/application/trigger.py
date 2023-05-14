from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Trigger:
    name: str
    from_state: str
    to_state: str
