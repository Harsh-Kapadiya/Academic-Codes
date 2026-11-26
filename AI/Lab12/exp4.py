import pandas as pd

# Load your CSV file
df = pd.read_csv("your_dataset.csv")

# Assume last column is target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy (CSV):", accuracy_score(y_test, y_pred))