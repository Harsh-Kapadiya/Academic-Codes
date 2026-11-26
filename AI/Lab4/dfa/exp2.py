goal = ((1,2,3), (4,5,6), (7,8,0))
intial_state = ((5,8,6), (4,7,1), (2,0,3))

moves = [(1,0), (-1,0), (0,-1), (0,1)]  # Down, Up, Left, Right


def blank_position(intial_state):
    for i in range(3):
        for j in range(3):
            if intial_state[i][j] == 0:
                return (i, j)
blank_pos = blank_position(intial_state)

def dfa(intial_pos, blank_pos, moves):
    x, y = blank_pos          # FIXED HERE
    next_state = []

    for move in moves:
        dx, dy = move
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in intial_pos]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            next_state.append(tuple(tuple(row) for row in new_state))

    return next_state

next_states = dfa(intial_state, blank_pos, moves)

print("Initial State:")
for row in intial_state:
    print(row)

print("\nPossible Next States:")
for state in next_states:
    for row in state:
        print(row)
    print()

if goal == next_states:
    print("Goal State Reached!")