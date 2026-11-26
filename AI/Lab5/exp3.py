import heapq

# ---------------- GOAL STATE ----------------
GOAL = ((0,1,2),
        (3,4,5),
        (6,7,8))      # 0 represents blank

# Possible moves: Up, Down, Left, Right
MOVES = [(-1,0),(1,0),(0,-1),(0,1)]


# ---------------- FIND BLANK POSITION ----------------
def find_blank(state):
    """
    TODO:
    Traverse the 3x3 board and return the (row, column)
    position of the blank tile (0).
    """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# ---------------- GENERATE SUCCESSOR STATES ----------------
def generate_states(state):
    """
    TODO:
    1. Find blank position.
    2. Apply all valid moves.
    3. Swap blank with adjacent tile.
    4. Return list of new states.
    """
    children = []
    x, y = find_blank(state)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            children.append(tuple(tuple(row) for row in new_state))
    return children


# ---------------- HEURISTIC 1: MISPLACED TILES ----------------
def h_misplaced(state):
    """
    TODO:
    Count number of tiles that are not in their goal position.
    Ignore the blank tile.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                count += 1
    return count

# ---------------- HEURISTIC 2: MANHATTAN DISTANCE ----------------
def h_manhattan(state):
    """
    TODO:
    Sum of Manhattan distances of each tile from its goal position.
    Ignore the blank tile.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                # find goal position of tile
                for r in range(3):
                    for c in range(3):
                        if GOAL[r][c] == tile:
                            distance += abs(i - r) + abs(j - c)
    return distance

# ---------------- A* SEARCH ALGORITHM ----------------
def astar(start, heuristic=h_manhattan):
    """
    TODO (A* Algorithm):
    1. Use priority queue ordered by f(n) = g(n) + h(n)
    2. Store g-cost for each state
    3. Stop when goal state is reached
    """
    pq = []
    g_cost = {start: 0}
    parent = {start: None}

    f_start = heuristic(start)
    heapq.heappush(pq, (f_start, 0, start))   # (f, g, state)  #middle me zero aaye ga g_cost ke jagah

    closed = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        if state in closed:
            continue
        closed.add(state)

        if state == GOAL:
            # reconstruct solution path
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()
            return path, g

        for child in generate_states(state):
            new_g = g + 1
            if child not in g_cost or new_g < g_cost[child]:
                g_cost[child] = new_g
                parent[child] = state
                new_f = new_g + heuristic(child)
                heapq.heappush(pq, (new_f, new_g, child))




# ---------------- PRINT SINGLE BOARD ----------------
def print_board(state):
    """
    TODO:
    Print a 3x3 puzzle board.
    Replace 0 with '_' while printing.
    """
    for row in state:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


# ---------------- PRINT COMPLETE SOLUTION PATH ----------------
def print_solution(solution, title="Solution"):
    """
    TODO:
    1. Print solution title.
    2. Print each step number.
    3. Print the board at each step.
    4. Print total number of moves.
    """
    print(f"\n--- {title} ---")

    for i, s in enumerate(solution):
        print(f"Step {i}:")
        print_board(s)

    print("Total moves =", len(solution) - 1)


# ---------------- INITIAL STATE ----------------
start_state = ((1,4,2),
               (6,5,8),
               (7,0,3))


# ---------------- RUN A* WITH MISPLACED TILES ----------------
sol1, cost1 = astar(start_state, heuristic=h_misplaced)

print_solution(sol1, title="A* with Misplaced Tiles (h1)")
print("Cost:", cost1)


# ---------------- RUN A* WITH MANHATTAN DISTANCE ----------------
# sol2, cost2 = astar(start_state, heuristic=h_manhattan)

# print_solution(sol2, title="A* with Manhattan Distance (h2)")
# print("Cost:", cost2)