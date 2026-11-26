from dataclasses import dataclass
from itertools import product

# -------------------- STATE --------------------
@dataclass(frozen=True)
class VacuumState:
    agent_pos: int        # 0..n-1
    dirt: tuple           # length n, values 0/1 (1=dirty, 0=clean)

# -------------------- ENVIRONMENT --------------------
class VacuumEnvironment:
    def __init__(self, n_locations=2, initial_state=None):
        self.n = n_locations
        self.state = initial_state if initial_state else VacuumState(0, tuple([1]*self.n))

    def is_dirty(self, pos: int) -> bool:
        return self.state.dirt[pos] == 1

    def all_clean(self) -> bool:
        return all(d == 0 for d in self.state.dirt)

    def clean_current(self):
        dirt = list(self.state.dirt)
        dirt[self.state.agent_pos] = 0
        self.state = VacuumState(self.state.agent_pos, tuple(dirt))

    def move_left(self):
        new_pos = max(0, self.state.agent_pos - 1)
        self.state = VacuumState(new_pos, self.state.dirt)

    def move_right(self):
        new_pos = min(self.n - 1, self.state.agent_pos + 1)
        self.state = VacuumState(new_pos, self.state.dirt)

# -------------------- SENSOR --------------------
class VacuumSensor:
    def sense(self, env: VacuumEnvironment):
        pos = env.state.agent_pos
        status = "DIRTY" if env.is_dirty(pos) else "CLEAN"
        return (pos, status)

# -------------------- ACTUATOR --------------------
class VacuumActuator:
    def apply(self, env: VacuumEnvironment, action: str):
        # returns env, event dictionary (for performance module)
        event = {"cleaned": False, "moved": False}

        if action == "SUCK":
            if env.is_dirty(env.state.agent_pos):
                env.clean_current()
                event["cleaned"] = True

        elif action == "LEFT":
            old = env.state.agent_pos
            env.move_left()
            event["moved"] = (env.state.agent_pos != old)

        elif action == "RIGHT":
            old = env.state.agent_pos
            env.move_right()
            event["moved"] = (env.state.agent_pos != old)

        elif action == "NOOP":
            pass

        else:
            raise ValueError("Unknown action: " + action)

        return env, event

# -------------------- PERFORMANCE MEASURE --------------------
class VacuumPerformance:
    def __init__(self, reward_clean=10, cost_move=1):
        self.reward_clean = reward_clean
        self.cost_move = cost_move

    def update(self, score: int, action: str, event: dict) -> int:
        if event.get("cleaned"):
            score += self.reward_clean
        if action in ("LEFT", "RIGHT"):
            score -= self.cost_move
        return score

# -------------------- SIMULATOR (WITH PRINTING) --------------------
class Simulator:
    def __init__(self, env, agent, sensor, actuator, performance):
        self.env = env
        self.agent = agent
        self.sensor = sensor
        self.actuator = actuator
        self.performance = performance

    def run(self, max_steps=20, verbose=True):
        score = 0

        if verbose:
            print("\n--- Vacuum World Simulation (Experiment 1a) ---")
            print("Initial State:", self.env.state)
            print("------------------------------------------------")
            print(f"{'Step':<5}{'Percept':<20}{'Action':<10}"
                  f"{'State After Action':<35}{'Score':<6}")
            print("------------------------------------------------")

        for t in range(1, max_steps + 1):
            percept = self.sensor.sense(self.env)
            action = self.agent.program(percept)
            self.env, event = self.actuator.apply(self.env, action)
            score = self.performance.update(score, action, event)

            if verbose:
                print(f"{t:<5}{str(percept):<20}{action:<10}"
                      f"{str(self.env.state):<35}{score:<6}")

            if self.env.all_clean():
                if verbose:
                    print("------------------------------------------------")
                    print("All locations clean. Simulation stopped.")
                break

        return score
