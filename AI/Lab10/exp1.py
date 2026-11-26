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

# Calculate intercept (b0)
b0 = y_mean - b1 * x_mean

print("Intercept (b0):", round(b0, 2))
print("Slope (b1):", round(b1, 2))

# Predictions
y_pred = b0 + b1 * x

# Predict for new value
x_new = 10
y_new = b0 + b1 * x_new
print(f"Predicted y for x = {x_new} is {round(y_new, 2)}")

# Plot
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_pred, color="red", label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()