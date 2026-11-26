# This code is an extension of the Naïve Bayes classifier implementation. It includes the following tasks:
# 1. Read the weather dataset from a .csv file.
# 2. Use a larger categorical dataset such as the Car Evaluation dataset.
# 3. Compare simple Naïve Bayes with Decision Tree classifier.
# 4. Add confusion matrix and classification accuracy for a separate test set.
# 5. Extend the classifier to handle both categorical and numerical data.


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# =========================
# Step 1: Load Dataset
# =========================
data = pd.read_csv("AI/Lab13/car.csv")

print("\nFirst 5 rows:\n", data.head())
print("\nDataset Info:\n")
print(data.info())

# =========================
# Step 2: Preprocessing
# =========================
# Remove spaces (very important)
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Force encode ALL columns
from sklearn.preprocessing import LabelEncoder

label_encoders = {}

for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column].astype(str))
    label_encoders[column] = le


# =========================
# Step 3: Train-Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# Step 4: Train Models
# =========================

# Naïve Bayes
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

# Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# =========================
# Step 5: Predictions
# =========================
y_pred_nb = nb_model.predict(X_test)
y_pred_dt = dt_model.predict(X_test)


# =========================
# Step 6: Evaluation Function
# =========================
def evaluate_model(name, y_test, y_pred):
    print(f"\n{name} Results:")
    print("-" * 30)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("Accuracy:", accuracy_score(y_test, y_pred))


# =========================
# Step 7: Evaluate Models
# =========================
evaluate_model("Naïve Bayes", y_test, y_pred_nb)
evaluate_model("Decision Tree", y_test, y_pred_dt)
