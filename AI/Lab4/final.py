from collections import deque
# ==========================================================
# EXPERIMENT: 8-PUZZLE USING BFS AND DFS
# 0 represents the blank tile
# ==========================================================

# ---------------- GOAL STATE ----------------
GOAL = ((1,2,3),
        (4,5,6),
        (7,8,0))   # 0 represents blank

# Possible moves of blank (Up, Down, Left, Right)
MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

# ---------------- FIND BLANK ----------------
def find_blank(state):
    """
    TODO:
    Traverse the 3x3 state and return the position of blank (0).
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# ---------------- GENERATE CHILD STATES ----------------
def generate_states(state):
    """
    TODO:
    1. Find blank position.
    2. Move blank in all valid directions.
    3. Generate and return new states.
    """
    children = []
    x, y = find_blank(state)

    for dx, dy in MOVES :
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3 :
            new_state = [list(row) for row in state]

            # swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            children.append(tuple(tuple(row) for row in new_state))

    return children

# ---------------- BREADTH-FIRST SEARCH ----------------
def bfs(start):
    """
    TODO (BFS Algorithm):
    1. Initialize queue with start state.
    2. Use visited set to avoid revisiting states.
    3. Expand nodes level by level.
    """
    queue = deque([(start, [])])      # (state, path)
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        if state == GOAL:
            return path + [state]

        for child in generate_states(state):
            if child not in visited:
                visited.add(child)
                queue.append((child, path + [state]))


# ---------------- DEPTH-FIRST SEARCH ----------------
def dfs(start, depth=20):
    """
    TODO (DFS Algorithm):
    1. Use stack for LIFO behavior.
    2. Expand nodes depth-wise.
    3. Limit depth to avoid infinite loops.
    """
    stack = [(start , [], 0 )]   # (state, path, depth)
    visited = set()

    while stack:
        state, path, d = stack.pop()

        if state == GOAL :
            return path + [state]

        if d < depth :
            visited.add(state)
            for child in generate_states(state):
                if child not in visited :
                    stack.append((child, path + [state], d + 1))


# ---------------- DRIVER CODE ----------------
"""
TODO:
1. Define the initial state.
2. Call BFS and DFS functions.
3. Print the solution path.
"""
start_state = ((1,2,3),
               (4,0,5),
               (6,7,8))

print("BFS Solution:")
solution = bfs(start_state)
for step in solution:
    print(step)


print("\nDFS Solution:")
solution = dfs(start_state, depth=20)
for step in solution :
    print(step)
def print_solution_boards(solution, title="Solution"):
    print(f"\n--- {title} (Board Trace) ---")
    for i, state in enumerate(solution):
        print(f"Step {i}:")
        for row in state:
            print(" ".join("_" if x == 0 else str(x) for x in row))
        print()
    print("Total Moves =", len(solution) - 1)


bfs_solution = bfs(start_state)
print_solution_boards(bfs_solution, title="BFS Solution")


dfs_solution = dfs(start_state)
print_solution_boards(dfs_solution, title="DFS Solution")