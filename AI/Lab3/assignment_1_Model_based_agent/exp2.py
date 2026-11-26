# LAB 2 – Q2: Taxi with Fuel Constraint

GRID_SIZE = 4
MAX_FUEL = 10
FUEL_STATIONS = [(0, 0), (3, 3)]

class TaxiEnv:
    def __init__(self):
        self.taxi = (0, 0)
        self.fuel = MAX_FUEL

    def move(self, action):
        if self.fuel == 0:
            print("Out of fuel!")
            return

        x, y = self.taxi
        if action == "N" and x > 0:
            self.taxi = (x - 1, y)
        elif action == "S" and x < GRID_SIZE - 1:
            self.taxi = (x + 1, y)
        elif action == "E" and y < GRID_SIZE - 1:
            self.taxi = (x, y + 1)
        elif action == "W" and y > 0:
            self.taxi = (x, y - 1)

        self.fuel -= 1
        self.check_refuel()

    def check_refuel(self):
        if self.taxi in FUEL_STATIONS:
            self.fuel = MAX_FUEL
            print("Refueled!")

env = TaxiEnv()
for _ in range(12):
    env.move("E")
    print("Pos:", env.taxi, "Fuel:", env.fuel)
