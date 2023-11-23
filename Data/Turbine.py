from dataclasses import dataclass
from typing import Optional


@dataclass
class Turbine:
    TurbineID: str  # Property, writable
    Alert: bool  # Property, writable
    TimeInterval: Optional[str] = None  # Telemetry
    Description: Optional[str] = None  # Telemetry
    Code: Optional[int] = None  # Telemetry
    WindSpeed: Optional[float] = None  # Telemetry
    Ambient: Optional[float] = None  # Telemetry
    Rotor: Optional[float] = None  # Telemetry
    Power: Optional[float] = None  # Telemetry
