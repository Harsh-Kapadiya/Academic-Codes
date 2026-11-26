# exp3.py
# Q3: Stochastic Road Blockage with Re-planning

import random
from exp1 import astar

GRID_SIZE = 5      # ← ADD THIS LINE
BLOCK_PROB = 0.3

blocked_cells = set()

def update_blockages():
    blocked_cells.clear()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < BLOCK_PROB:
                blocked_cells.add((i, j))

def valid_path(path):
    if path is None:
        return False
    for cell in path:
        if cell in blocked_cells:
            return False
    return True

taxi_pos = (0, 0)
goal = (4, 4)

while taxi_pos != goal:
    update_blockages()
    print("\nBlocked cells:", blocked_cells)

    path = astar(taxi_pos, goal)
    if not valid_path(path):
        print("Path blocked, re-planning...")
        continue

    taxi_pos = path[0]
    print("Taxi moved to", taxi_pos)

print("\nReached destination!")
