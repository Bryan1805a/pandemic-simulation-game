from core.game_state import GameState

class EpidemicEngine:
    def __init__(self, state: GameState):
        self.state = state

        # Initialization parameters for the Wild-type (WH-01) virus strain
        self.R0 = 2.5
        self.incubation_period = 5.0  # Day
        self.infectious_period = 10.0 # Day
        self.ifr = 0.02               # Infection Fatality (2%)
    
    def simulate_one_week(self):
        sigma = 1.0 / self.incubation_period
        gamma = 1.0 / self.infectious_period
        beta = self.R0 * gamma

        # Loop 7 days
        for _ in range(7):
            S = self.state.susceptible
            E = self.state.exposed
            I = self.state.infectious
            R = self.state.recovered
            D = self.state.deceased

            N = S + E + I + R
            if N <= 0:
                continue

            new_exposed = (beta * S * I) / N
            new_infectious = sigma * E
            resolved_cases = gamma * I

            new_deaths = resolved_cases * self.ifr
            new_recovered = resolved_cases * (1 - self.ifr)

            # Update GameState
            self.state.susceptible = max(0.0, S - new_exposed)
            self.state.exposed = max(0.0, E + new_exposed - new_infectious)
            self.state.infectious = max(0.0, I + new_infectious - resolved_cases)
            self.state.recovered += new_recovered
            self.state.deceased += new_deaths