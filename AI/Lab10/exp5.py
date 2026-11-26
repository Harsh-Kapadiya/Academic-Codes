# Load required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
data = pd.read_csv("AI/Lab10/advertising.csv")

# Step 2: Basic checks
print(data.head())
print(data.info())

# Step 3: Define features and target
# Using only one feature for simplicity (you can expand later)
X = data[['TV']].values
y = data['Sales'].values

# Step 4: Convert continuous target into binary (classification)
threshold = np.mean(y)
y = np.array([1 if val > threshold else 0 for val in y])

# Step 5: Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 7: Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Step 8: Custom Logistic Regression
class LogisticRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = sigmoid(linear_model)

            # Gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            # Update
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_model)
        return np.array([1 if i > 0.5 else 0 for i in y_pred])

# Step 9: Train model
model = LogisticRegression(learning_rate=0.01, epochs=500)
model.fit(X_train, y_train)

# Step 10: Predictions
y_pred = model.predict(X_test)

# Step 11: Evaluation
print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))