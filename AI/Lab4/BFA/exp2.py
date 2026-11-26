# 8 puzzle problem using the BFA
from collections import deque
goal = ((1,2,3), (4,5,6), (7,8,0))
intial_state = ((5,8,6), (4,7,1), (2,0,3))

moves = [(1,0), (-1,0), (0,-1), (0,1)]  # Down, Up, Left, Right


def blank_position(intial_state):
    for i in range(3):
        for j in range(3):
            if intial_state[i][j] == 0:
                return (i, j)

blank_pos = blank_position(intial_state)

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

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
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
    queue = deque([(state, moves)])      # (state, path)
    visited = set([])

    while queue:
        state, path = queue.popleft()

        if state == :
            return path + [state]

        for child in generate_states(state):
            if child not in visited:
                visited.add(child)
                queue.append((child, path + [state]))


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
solution = bfs(....)
for step in ....:
    print(step)

print("\nDFS Solution:")
solution = dfs(, depth=20)
for step in :
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