# Q1: A* Search for Taxi Navigation
import heapq
GRID_SIZE = 5
def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def get_neighbors(node):
    x, y = node
    moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(i,j) for i,j in moves if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE]
def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {}
    g_cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for nxt in get_neighbors(current):
            new_cost = g_cost[current] + 1
            if nxt not in g_cost or new_cost < g_cost[nxt]:
                g_cost[nxt] = new_cost
                priority = new_cost + heuristic(nxt, goal)
                heapq.heappush(pq, (priority, nxt))
                came_from[nxt] = current
    return None
# Example
start = (0, 0)
goal = (4, 4)
print("Path:", astar(start, goal))
