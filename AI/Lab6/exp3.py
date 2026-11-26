import random

N = 0

def conflicts(state):
    c = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j]:
                c += 1
            if abs(state[i] - state[j]) == abs(i - j):
                c += 1
    return c

def random_state():
    return [random.randrange(8) for _ in range(8)]



def best_neighbor(state):
    current_h = conflicts(state)
    best = state[0]
    best_h = current_h

    for col in range(8):
        for row in range(8):
            if row != state[....]:
                neighbor = state[:]
                neighbor[col] = row
                h = conflicts(....)
                if h < best_h:
                    best_h = ....
                    best = ....
    return best, best_h


def hill_climb(max_steps=2000):
    state = random_state()
    h = conflicts(....)

    for _ in range(....):
        next_state, next_h = best_neighbor(....)

        if next_h >= ....:
            return state, ....

        state, h = ...., ....

        if h == ....:
            return state, ....
    return state, ....



def random_restart_hill_climbing(max_restarts=50):
    best_state = ....
    best_h = float('....')

    for _ in range(....):
        state, solved = hill_climb()
        h = conflicts(....)

        if h < ....:
            best_h = ....
            best_state = ....

        if solved:
            return best_state, ....
    return best_state, ....


def print_board(state):
    for r in range(8):
        row = []
        for c in range(8):
            row.append("Q" if state[c] ==  else ".")
        print(" ".join(row))
    print("Conflicts:", conflicts(....))


solution, solved = random_restart_hill_climbing()

print("Solved:", solved)
print_board(solution)