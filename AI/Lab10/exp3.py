# loading data from the csv file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("Lab10/advertising.csv")

# Features and target
x = df[["TV"]]
y = df[["Sales"]]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=101
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Parameters
print("Intercept (c):", model.intercept_[0])
print("Coefficient (m):", model.coef_[0][0])

# Predictions
y_pred = model.predict(X_test)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)
print("R-squared:", r2_score(y_test, y_pred))

# --- FIX: Sort values for proper line plotting ---
X_test_sorted = X_test.sort_values(by="TV")
y_pred_sorted = model.predict(X_test_sorted)

# Plot
plt.scatter(X_test, y_test, color="blue", label="Actual Sales")
plt.plot(X_test_sorted, y_pred_sorted, color="red", linewidth=2, label="Regression Line")

plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")
plt.title("TV Advertising vs Sales")
plt.legend()
plt.show()