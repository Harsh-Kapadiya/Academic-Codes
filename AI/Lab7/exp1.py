from math import inf

graph = {
    "S": [ (["A"], 1), (["B"], 1) ],        # OR: choose A or B
    "A": [ (["C","D"], 1) ],                # AND: must solve C and D
    "B": [ (["E"], 1), (["F"], 3) ],        # OR: choose E or F
    "C": [ (["G"], 1) ],                    # OR (single option)
    "D": [ (["H"], 1) ],                    # OR (single option)
    "E": [ ([], 0) ],                       # terminal/goal-like leaf
    "F": [ ([], 0) ],
    "G": [ ([], 0) ],
    "H": [ ([], 0) ],
}

# Heuristic values for leaves or initial estimates for nodes
h = {
    "S": 6, "A": 4, "B": 4,
    "C": 2, "D": 2,
    "E": 1, "F": 3,
    "G": 0, "H": 0
}

#You can change the above graph/ its values

def is_terminal(node):
    # terminal node if it has an option with empty children list ([])
    return any(len(children) == 0 for (children, _) in graph.get(node, []))

def ao_star(start):
    # cost estimates
    cost = {n: h.get(n, 0) for n in graph.keys()}
    solved = {n: False for n in graph.keys()}
    best_choice = {}  # node -> chosen option (children tuple)

    def compute_node_cost(n):
        """Compute cost of node n based on current children costs."""
        options = graph.get(n, [])
        best_val = inf
        best_opt = None 

        for children, edge_cost in options:
            if len(children) == 0:
                val = edge_cost          # terminal
            else:
                val = edge_cost + sum(cost[ch] for ch in children)  # AND inside an option

            if val < best_val:
                best_val = val
                best_opt = children

        cost[n] = best_val
        best_choice[n] = tuple(best_opt) if best_opt is not None else tuple()

    def mark_solved(n):
        chs = best_choice.get(n, tuple())
        if len(chs) == 0:
            solved[n] = True
        else:
            solved[n] = all(solved[ch] for ch in chs)

    def get_best_leaf(n):
        cur = n
        path = [cur]

        while True:
            compute_node_cost(cur)
            mark_solved(cur)

            if solved[cur]:
                return cur, path

            chs = best_choice.get(cur, tuple())
            if len(chs) == 0:
                return cur, path

            # pick first child that is not solved (expand along best subgraph)
            next_child = None
            for ch in chs:
                if not solved[ch]:
                    next_child = ch
                    break

            if next_child is None:
                return cur, path

            cur = next_child
            path.append(cur)

    # Main AO* loop
    while not solved[start]:
        leaf, path = get_best_leaf(start)

        if leaf is None:
            break  # no leaf found; either solved or stuck

        # Expand leaf: compute its cost from its options and propagate updates.
        compute_node_cost(leaf)

        # If terminal, mark solved
        if is_terminal(leaf):
            best_choice[leaf] = tuple()   # terminal best choice
            solved[leaf] = True

        # Backward cost revision along path
        for node in reversed(path):
            compute_node_cost(node)
            mark_solved(node)

    return cost, best_choice, solved

#Print the solution graph
def print_solution_graph(start, best_choice):
    print("\n--- Optimal Solution Subgraph (Marked by AO*) ---")

    visited = set()

    def dfs(n, indent=0):
        if n in visited:
            return
        visited.add(n)

        chs = best_choice.get(n, tuple())
        print("  " * indent + f"{n} -> {list(chs)}")
        for ch in chs:
            dfs(ch, indent + 1)

    dfs(start)


cost, best_choice, solved = ao_star("S")

print("Solved Start Node:", solved["S"])
print("Optimal Cost from Start:", cost["S"])

print_solution_graph("S", best_choice)