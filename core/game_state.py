from dataclasses import dataclass, field
from datetime import datetime, timedelta

@dataclass
class GameState:
    # Time variable
    turn: int = 0
    current_date: datetime = datetime(2019, 12, 1) # Start date of COVID Pandemic

    # Epidemiology variable
    susceptible: int = 97_000_000 # Vietnam's population
    exposed: int = 0
    infectious: int = 10 # The first cases
    recovered: int = 0
    deceased: int = 10

    icu_capacity: int = 5000
    icu_occupied: int = 0

    # Economic & Political variable
    budget_mil_usd: float = 1000.0
    gdp_baseline_percent: float = 100.0

    satisfaction_index: float = 80.0
    trust_index: float = 90.0
    political_capital: int = 50

    # Event log
    event_log: list[str] = field(default_factory=list)