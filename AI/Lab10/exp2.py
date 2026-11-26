# implementing multiple linear regressions

import numpy as np
import matplotlib.pyplot as plt
import random as rn

# random dataset
x = np.array([rn.randint(1, 50) for _ in range(20)])
y = np.array([rn.randint(2, 50) for _ in range(20)])

n = len(x)

# Mean values
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate slope (b1)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
b1 = numerator / denominator
b2 = numerator / denominator
b3 = numerator / denominator


# Calculate intercept (b0)
b01 = y_mean - b1 * x_mean
b02 = y_mean - b1 * x_mean

print("Intercept (b0):", round(b01, 2))
print("Intercept (b0):", round(b02, 2))
print("Slope (b1):", round(b1, 2))
print("Slope (b1):", round(b2, 2))
print("Slope (b1):", round(b3, 2))

# Predictions
y1_pred = b01 + b1 * x
y2_pred = b02 + b1 * x + b2 * x + b3 * x

# Predict for new value
x_new = 10
y1_new = b01 + b1 * x_new
y2_new = b02 + b1 * x_new + b2 * x_new + b3 * x_new
print(f"Predicted y for x = {x_new} is {round(y1_new, 2)}")
print(f"Predicted y for x = {x_new} is {round(y2_new, 2)}")

# Plot
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y1_pred, color="red", label="Regression Line for 1st equation")
plt.plot(x, y2_pred, color="green", label="Regression Line for 2nd equation")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()