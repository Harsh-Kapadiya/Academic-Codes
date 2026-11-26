# LAB 2 – Q1: Taxi with Walls / Blocked Roads

GRID_SIZE = 4

# blocked roads: ((x1,y1),(x2,y2))
WALLS = {
    ((1, 1), (1, 2)),
    ((2, 2), (2, 3)),
    ((0, 2), (1, 2))
}

def is_blocked(a, b):
    return (a, b) in WALLS or (b, a) in WALLS

class TaxiEnv:
    def __init__(self):
        self.taxi = (0, 0)

    def move(self, action):
        x, y = self.taxi
        new_pos = self.taxi

        if action == "N" and x > 0:
            new_pos = (x - 1, y)
        elif action == "S" and x < GRID_SIZE - 1:
            new_pos = (x + 1, y)
        elif action == "E" and y < GRID_SIZE - 1:
            new_pos = (x, y + 1)
        elif action == "W" and y > 0:
            new_pos = (x, y - 1)

        if not is_blocked(self.taxi, new_pos):
            self.taxi = new_pos
        else:
            print("Blocked by wall!")

env = TaxiEnv()
env.move("S")
env.move("E")
env.move("E")