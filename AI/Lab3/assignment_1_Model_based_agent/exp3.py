# LAB 2 – Q3: Sensor Noise in passenger_here

import random

NOISE_PROB = 0.2  # 20% sensor error

class TaxiEnv:
    def __init__(self):
        self.taxi = (1, 1)
        self.passenger = (2, 2)

    def sense_passenger(self):
        actual = self.taxi == self.passenger

        # add noise
        if random.random() < NOISE_PROB:
            return not actual  # wrong reading
        return actual

env = TaxiEnv()

for i in range(10):
    print("Sensor says passenger_here:", env.sense_passenger())
