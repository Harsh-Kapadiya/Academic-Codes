import random

class RandomVacuumAgent:
    # Useful for testing the simulator in 1(a)
    def __init__(self):
        self.actions = ["LEFT", "RIGHT", "SUCK", "NOOP"]
    def program(self, percept):
        return random.choice(self.actions)

class SimpleReflexVacuumAgent:
    # For 1(b)
    def __init__(self, n_locations=2):
        self.n = n_locations
    def program(self, percept):
        pos, status = percept
        if status == "DIRTY":
            return "SUCK"
        # Sweep strategy
        if pos < self.n - 1:
            return "RIGHT"
        return "LEFT"
