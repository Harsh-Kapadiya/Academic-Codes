# hill climbing algorithm for 8 puzzle problem
import random

# ---------------- OBJECTIVE FUNCTION ----------------
def f(x):
    """
    Define the evaluation (heuristic) function.
    Higher value means better state.
    """
    return x


# ---------------- GENERATE NEIGHBORS ----------------
def neighbors(x, step=1, low=0, high=10):
    """
    Generate neighboring states of x within given limits.
    """
    cand = []

    if x - step >= low:
        cand.append(x - step)

    if x + step <= high:
        cand.append(x + step)

    return cand


# ---------------- HILL CLIMBING ----------------
def hill_climbing(start, step=1, low=0, high=10):
    current = start

    print("\n--- Hill Climbing Trace ---")
    print("Start State:", current, "Value:", f(current))

    while True:
        neigh = neighbors(current, step=step, low=low, high=high)

        if not neigh:
            break

        # choose neighbor with maximum heuristic value
        next_state = max(neigh, key=f)

        if f(next_state) <= f(current):
            print("STOP at", current, "(Local Maximum Reached)")
            break

        current = next_state
        print("Move to:", current, "Value:", f(current))

    return current


# ---------------- RUN PROGRAM ----------------
start = 5
best = hill_climbing(start, step=1, low=0, high=20)

print("\nBest solution found:", best)
print("Value of best solution:", f(best))