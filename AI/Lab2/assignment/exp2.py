import random

# -----------------------------------------
# Environment with Stochastic Dirt
# -----------------------------------------

class StochasticEnvironment:
    def __init__(self):
        self.size = 3
        self.grid = [[0 for _ in range(3)] for _ in range(3)]

    def add_random_dirt(self, probability=0.3):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < probability:
                    self.grid[i][j] = 1

    def display(self):
        for row in self.grid:
            for cell in row:
                print("D" if cell == 1 else "C", end=" ")
            print()


# -----------------------------------------
# Main
# -----------------------------------------
env = StochasticEnvironment()
env.add_random_dirt()
env.display()
