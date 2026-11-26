# Q2: Multiple Passengers using A*
from exp1 import astar
PASSENGERS = [(1, 3), (3, 1)]
DESTINATION = (4, 4)

taxi_pos = (0, 0)

for passenger in PASSENGERS:
    print("\nGoing to passenger at", passenger)
    path = astar(taxi_pos, passenger)
    for step in path:
        taxi_pos = step
        print("Taxi at", taxi_pos)

    print("Picked passenger")

    print("Going to destination")
    path = astar(taxi_pos, DESTINATION)
    for step in path:
        taxi_pos = step
        print("Taxi at", taxi_pos)

    print("Dropped passenger at destination")
