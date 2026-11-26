import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("AI/Lab9/car.csv")

data.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

# Separate features and target
x = data.drop(['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'], axis=1)
y = data['class']

# One-hot encoding
encoder = OneHotEncoder()
x_encoded = encoder.fit_transform(x)

# Train-test split  
x_train, x_test, y_train, y_test = train_test_split(x_encoded, y, test_size=0.2, random_state=42)

# KNN model
# selectig best k value
for k in range(1, 5):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)


# Prediction
y_pred = knn.predict(x_test)
# Evaluation
print("predicated table:")
print(pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}))

# accuracy calculation
correct_predictions = (y_test == y_pred).sum()
total_predictions = len(y_test)
accuracy = correct_predictions / total_predictions
print("Accuracy:", accuracy)