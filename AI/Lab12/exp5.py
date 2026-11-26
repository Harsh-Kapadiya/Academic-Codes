# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


# =========================
# 1. LOAD DATASET (IRIS)
# =========================
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\n===== BASE MODEL (GINI) =====")
model_gini = DecisionTreeClassifier(criterion="gini")
model_gini.fit(X_train, y_train)
y_pred_gini = model_gini.predict(X_test)
print("Accuracy (Gini):", accuracy_score(y_test, y_pred_gini))


# =========================
# 2. ENTROPY (ID3)
# =========================
print("\n===== ENTROPY MODEL =====")
model_entropy = DecisionTreeClassifier(criterion="entropy")
model_entropy.fit(X_train, y_train)
y_pred_entropy = model_entropy.predict(X_test)
print("Accuracy (Entropy):", accuracy_score(y_test, y_pred_entropy))


# =========================
# 3. LIMIT TREE DEPTH
# =========================
print("\n===== LIMITED DEPTH =====")
model_depth = DecisionTreeClassifier(max_depth=3)
model_depth.fit(X_train, y_train)
y_pred_depth = model_depth.predict(X_test)
print("Accuracy (Max Depth=3):", accuracy_score(y_test, y_pred_depth))


# =========================
# 4. PRUNING
# =========================
print("\n===== PRUNED TREE =====")
model_pruned = DecisionTreeClassifier(
    max_depth=3, min_samples_split=5, min_samples_leaf=2
)
model_pruned.fit(X_train, y_train)
y_pred_pruned = model_pruned.predict(X_test)
print("Accuracy (Pruned):", accuracy_score(y_test, y_pred_pruned))


# =========================
# 5. COMPARE WITH KNN & LR
# =========================
print("\n===== MODEL COMPARISON =====")

# KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Logistic Regression
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("Decision Tree:", accuracy_score(y_test, y_pred_gini))
print("KNN:", accuracy_score(y_test, y_pred_knn))
print("Logistic Regression:", accuracy_score(y_test, y_pred_lr))


# =========================
# 6. CSV DATASET (OPTIONAL)
# =========================
print("\n===== CSV DATASET (OPTIONAL) =====")
try:
    df = pd.read_csv("your_dataset.csv")
    X_csv = df.iloc[:, :-1]
    y_csv = df.iloc[:, -1]

    X_train_csv, X_test_csv, y_train_csv, y_test_csv = train_test_split(
        X_csv, y_csv, test_size=0.3, random_state=42
    )

    model_csv = DecisionTreeClassifier()
    model_csv.fit(X_train_csv, y_train_csv)
    y_pred_csv = model_csv.predict(X_test_csv)

    print("CSV Accuracy:", accuracy_score(y_test_csv, y_pred_csv))
except:
    print("CSV file not found (skip this part)")


# =========================
# 7. DECISION BOUNDARY (2 FEATURES)
# =========================
print("\n===== DECISION BOUNDARY =====")

X2 = iris.data[:, :2]  # take only 2 features
y2 = iris.target

model_vis = DecisionTreeClassifier()
model_vis.fit(X2, y2)

x_min, x_max = X2[:, 0].min() - 1, X2[:, 0].max() + 1
y_min, y_max = X2[:, 1].min() - 1, X2[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

Z = model_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z)
plt.scatter(X2[:, 0], X2[:, 1], c=y2)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Decision Boundary")
plt.show()
