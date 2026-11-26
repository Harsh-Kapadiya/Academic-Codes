import heapq
graph = {
    "A": [("B", 2), ("D", 1)],
    "B": [("A", 2), ("C", 2), ("E", 5)],
    "C": [("B", 2), ("F", 3)],
    "D": [("A", 1), ("E", 2)],
    "E": [("B", 5), ("D", 2), ("F", 2)],
    "F": [("C", 3), ("E", 2)]
}

# Heuristic values: estimated distance to goal node "F"
h = {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 5,
    "E": 1,
    "F": 0
}

# ----------- PATH RECONSTRUCTION ----------
def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    if path[0] == start:
        return path
    return None

# ----------- GREEDY BEST FIRST SEARCH ----------
def greedy_best_first_search(graph, h, start, goal):

    pq = []
    heapq.heappush(pq, (h[start], start))

    visited = set()
    parent = {start: None}

    print("\n--- Greedy Best First Search Trace ---")

    while pq:
        _, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print("Expanding:", node)

        if node == goal:
            return reconstruct_path(parent, start, goal)

        for nbr, cost in graph[node]:
            if nbr not in visited and nbr not in parent:
                parent[nbr] = node
                heapq.heappush(pq, (h[nbr], nbr))

    return None

start, goal = "A", "F"

path = greedy_best_first_search(graph, h, start, goal)
visited = greedy_best_first_search(graph, h, start, goal)
print("Path found:", path)
print("Visited nodes:", visited)