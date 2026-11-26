from collections import deque
import time
import matplotlib.pyplot as plt
import numpy as np
# ==========================
# PUZZLE CONFIGURATION
# ==========================
SIZE = 4  # 4x4 for 15-puzzle
GOAL_STATE = tuple(range(1, SIZE*SIZE)) + (0,)

INITIAL_STATE = (1, 15, 5, 4,8, 6, 2, 7,9, 11, 3, 12,13, 14, 0, 10)
# ==========================
# MOVE GENERATOR
# ==========================
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    r, c = divmod(idx, SIZE)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            new_idx = nr * SIZE + nc
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors

# ==========================
# BFS
# ==========================
def bfs(start):
    queue = deque([(start, [])])
    visited = {start}
    nodes = 0
    start_time = time.time()
    while queue:
        state, path = queue.popleft()
        nodes += 1
        if state == GOAL_STATE:
            return path + [state], nodes, time.time() - start_time
        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None, nodes, time.time() - start_time

# ==========================
# DFS (Depth Limited)
# ==========================
def dfs(start, limit=20):
    stack = [(start, [])]
    visited = set()
    nodes = 0
    start_time = time.time()

    while stack:
        state, path = stack.pop()
        nodes += 1

        if state == GOAL_STATE:
            return path + [state], nodes, time.time() - start_time

        if len(path) < limit:
            visited.add(state)
            for next_state in get_neighbors(state):
                if next_state not in visited:
                    stack.append((next_state, path + [state]))
    return None, nodes, time.time() - start_time
# ==========================
# GRAPHICAL VISUALIZATION
# ==========================
def visualize(solution):
    plt.figure(figsize=(4,4))
    for step, state in enumerate(solution):
        grid = np.array(state).reshape(SIZE, SIZE)
        plt.clf()
        plt.imshow(grid, cmap="Blues")
        plt.title(f"Step {step}")
        plt.axis("off")
        for i in range(SIZE):
            for j in range(SIZE):
                if grid[i][j] != 0:
                    plt.text(j, i, str(grid[i][j]),
                             ha='center', va='center',
                             fontsize=14, color='black')
        plt.pause(0.8)
    plt.show()
# ==========================
# MAIN
# ==========================
print("\n--- 15 PUZZLE USING BFS & DFS ---\n")

bfs_path, bfs_nodes, bfs_time = bfs(INITIAL_STATE)
dfs_path, dfs_nodes, dfs_time = dfs(INITIAL_STATE)

print("BFS RESULTS")
print("-----------")
print("Solution Depth :", len(bfs_path)-1)
print("Nodes Explored :", bfs_nodes)
print("Time Taken    :", round(bfs_time, 4), "seconds\n")

print("DFS RESULTS")
print("-----------")
print("Solution Depth :", len(dfs_path)-1 if dfs_path else "Not Found")
print("Nodes Explored :", dfs_nodes)
print("Time Taken    :", round(dfs_time, 4), "seconds\n")

print("Launching graphical visualization (BFS solution)...")
visualize(bfs_path)