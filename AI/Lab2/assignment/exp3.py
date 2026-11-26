# -----------------------------------------
# Performance Comparison for Movement Cost
# -----------------------------------------

class Performance:
    def __init__(self, move_cost):
        self.score = 0
        self.move_cost = move_cost

    def move(self):
        self.score -= self.move_cost

    def clean(self):
        self.score += 10


def simulate(move_cost):
    performance = Performance(move_cost)

    # Simulated actions
    for _ in range(5):
        performance.move()
    for _ in range(2):
        performance.clean()

    return performance.score


# -----------------------------------------
# Main
# -----------------------------------------
movement_costs = [1, 2, 5]

for cost in movement_costs:
    score = simulate(cost)
    print(f"Movement Cost = {cost}, Final Score = {score}")
