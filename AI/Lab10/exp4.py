# loading data from the csv file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("Lab10/advertising.csv")

# random dataset
x = df[["TV"]]
y = df[["Sales"]]

# here 70% data is training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=101
)


# train the model
model = LinearRegression()
model.fit(X_train, y_train)

# View the learned parameters
print("Intercept (c):", model.intercept_)
print("Coefficient (m):", model.coef_)


# predicting y
y_pred = model.predict(X_test)

# Evaluate
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
print("R-squared:", r2_score(y_test, y_pred))


# Plot
plt.scatter(X_test, y_test, color="blue", label="Actual Sales")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Regression Line")
plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")
plt.title("TV Advertising vs Sales")
plt.legend()
plt.show()
