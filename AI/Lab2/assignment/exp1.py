# -----------------------------------------
# 3x3 Grid Vacuum Environment with Obstacles
# -----------------------------------------

class GridEnvironment:
    def __init__(self):
        self.size = 3
        self.agent_pos = (0, 0)

        # 0 = Clean, 1 = Dirty
        self.grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        # Obstacle at center
        self.obstacles = [(1, 1)]

    def is_dirty(self):
        x, y = self.agent_pos
        return self.grid[x][y] == 1

    def clean(self):
        x, y = self.agent_pos
        self.grid[x][y] = 0

    def move(self, direction):
        x, y = self.agent_pos

        moves = {
            "UP": (x - 1, y),
            "DOWN": (x + 1, y),
            "LEFT": (x, y - 1),
            "RIGHT": (x, y + 1)
        }

        if direction in moves:
            nx, ny = moves[direction]
            if 0 <= nx < self.size and 0 <= ny < self.size:
                if (nx, ny) not in self.obstacles:
                    self.agent_pos = (nx, ny)

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_pos:
                    print("A", end=" ")
                elif (i, j) in self.obstacles:
                    print("X", end=" ")
                elif self.grid[i][j] == 1:
                    print("D", end=" ")
                else:
                    print("C", end=" ")
            print()


# -----------------------------------------
# Main
# -----------------------------------------
env = GridEnvironment()
env.display()
