# Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=40
)

# Create Decision Tree model
model = DecisionTreeClassifier(criterion="gini")

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Decision Tree:", accuracy)

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Sample Predictions
print("\nSample Predictions:")
for i in range(5):
    print(
        "Actual:",
        iris.target_names[y_test[i]],
        "| Predicted:",
        iris.target_names[y_pred[i]],
    )


# data visualization
X_vis = X[:, :2]
plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y, cmap="viridis")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Iris Dataset Visualization")
plt.show()

# Visualize Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
print("\nDecision Tree Visualization:")
plt.show()