import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv("AI/Lab10/advertising.csv")

print(data.head())
print(data.info())
print(data.describe())

# Convert Sales into binary (above average = 1, else 0)
data["Target"] = (data["Sales"] > data["Sales"].mean()).astype(int)

# Features and target
X = data[["TV", "Radio", "Newspaper"]]
y = data["Target"]

# visualizing the data
plt.figure()
plt.scatter(data["TV"], data["Sales"])
plt.xlabel("TV Advertising Spend")
plt.ylabel("Sales")
plt.title("TV vs Sales")
plt.show()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)


# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# Logistic Regression
class LogisticRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.losses = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = sigmoid(linear_model)

            # Binary Cross Entropy Loss
            loss = -(1 / n_samples) * np.sum(
                y * np.log(y_predicted + 1e-9)
                + (1 - y) * np.log(1 - y_predicted + 1e-9)
            )
            self.losses.append(loss)

            # Gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = sigmoid(linear_model)
        return np.array([1 if i > 0.5 else 0 for i in y_predicted])


# Train Model
model = LogisticRegression(learning_rate=0.01, epochs=500)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

# Confusion Matrix Heatmap
plt.figure()
sns.heatmap(conf_matrix, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()